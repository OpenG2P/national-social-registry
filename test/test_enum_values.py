"""Guard: every enum-backed value the seeder writes, and the views read, is real.

The columns involved are plain `String`, not native Postgres enums, so an invalid
value INSERTs without complaint. It surfaces much later and somewhere else: the
API rejects the row when it deserialises it against the Pydantic schema, the
attribute metadata has no matching `value_id`, and a dashboard groups by a
category that does not exist.

That is how eleven invalid values survived in the sample generator — `HEAD` where
the enum says `SELF`, `SETTLED` where it says `HOST_COMMUNITY`, `LPG` for `GAS`,
`GRID_ELECTRICITY` for `GRID`, and so on. They went unnoticed because
`reporting_views.sql` hardcoded the *same* invented names, so the two agreed with
each other and the dashboards looked correct while the rows were unusable.

Three things are checked, and the third is the one that is easy to miss:

  1. every value the generator writes is a member of the matching enum
  2. every literal the views compare against is a member of the matching enum
  3. every literal the views compare against is a value the generator can
     actually produce — otherwise the predicate is silently always-false, which
     is exactly what would have happened had the generator been fixed on its own

This test is only possible because the generator now lives in this repo beside
the enums it depends on. While it sat in openg2p-data there was no way to import
or parse them from the same place.

Stdlib + pytest only, like test_rp_pin_lockstep.py — runs wherever those do.
"""

import ast
import pathlib
import re

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
ENUMS = (REPO / "nsr-extension" / "src" / "openg2p_registry_nsr_extension"
         / "register_domain" / "models" / "enums.py")
GENERATOR = REPO / "docker" / "db-seed" / "generate_nsr_bulk_sample.py"
VIEWS = REPO / "docker" / "db-seed" / "reporting_views.sql"

# Generator constant -> the enum its members must belong to.
ENUM_BACKED_CONSTANTS = {
    "TENURE": "TenureStatusEnum",
    "HEADSHIP": "HeadshipTypeEnum",
    "PROGRAMS": "ProgramEnum",
    "DISPLACEMENT": "DisplacementStatusEnum",
    "PASTORALIST": "PastoralistClassificationEnum",
    "RELATIONSHIPS": "RelationshipToHeadEnum",
}

# HOUSING ladder key -> enum. The dwelling/roof/wall/floor materials in that same
# dict are free text and deliberately absent here.
ENUM_BACKED_HOUSING = {
    "water_source_type": "WaterSourceTypeEnum",
    "sanitation_type": "SanitationTypeEnum",
    "lighting_source": "LightingSourceEnum",
    "cooking_fuel_type": "CookingFuelEnum",
}

# Values written as inline literals rather than via a named constant.
ENUM_BACKED_INLINE = {
    "age_method": "AgeMethodEnum",
    "citizenship_category": "CitizenshipCategoryEnum",
    "identity_evidence_type": "IdentityEvidenceTypeEnum",
}

# Column -> enum, for literals appearing in the reporting views.
VIEW_COLUMNS = {
    "relationship_to_head": "RelationshipToHeadEnum",
    "displacement_status": "DisplacementStatusEnum",
    "water_source_type": "WaterSourceTypeEnum",
    "sanitation_type": "SanitationTypeEnum",
    "cooking_fuel_type": "CookingFuelEnum",
    "lighting_source": "LightingSourceEnum",
    "headship_type": "HeadshipTypeEnum",
    "program_name": "ProgramEnum",
}


def enum_members():
    """{EnumName: {members}} parsed from enums.py.

    Parsed rather than imported so this runs without installing the extension or
    its dependencies, matching how the other repo-level test behaves.
    """
    out = {}
    for node in ast.parse(ENUMS.read_text()).body:
        if not isinstance(node, ast.ClassDef):
            continue
        members = {n.value.value for n in node.body
                   if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
                   and isinstance(n.value.value, str)}
        if members:
            out[node.name] = members
    return out


def _strings(node):
    """Every string constant under an AST node, including inside tuples."""
    return {n.value for n in ast.walk(node)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)}


def generator_values():
    """{enum_name: {values the generator writes}}."""
    tree = ast.parse(GENERATOR.read_text())
    found = {}

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue

        if target.id in ENUM_BACKED_CONSTANTS:
            # Plain lists and (name, weight) pair lists both reduce to strings;
            # the integer weights are not Constants of type str.
            found.setdefault(ENUM_BACKED_CONSTANTS[target.id], set()).update(
                _strings(node.value))

        if target.id == "HOUSING" and isinstance(node.value, ast.Dict):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and k.value in ENUM_BACKED_HOUSING:
                    found.setdefault(ENUM_BACKED_HOUSING[k.value], set()).update(
                        _strings(v))

    src = GENERATOR.read_text()
    for column, enum in ENUM_BACKED_INLINE.items():
        # e.g.  "age_method": "DOCUMENTED" if ... else "ESTIMATED",
        for m in re.finditer(rf'"{column}":\s*\(?([^\n]*)', src):
            vals = set(re.findall(r'"([A-Z][A-Z_]+)"', m.group(1)))
            if vals:
                found.setdefault(enum, set()).update(vals)
    return found


def view_literals():
    """{enum_name: {literals the views compare that column against}}."""
    # Strip -- comments first: the explanatory notes in that file name the old
    # wrong values on purpose, and matching those would fail the test forever.
    sql = "\n".join(line.split("--")[0] for line in VIEWS.read_text().splitlines())
    found = {}
    for column, enum in VIEW_COLUMNS.items():
        for m in re.finditer(rf"\b{column}\b\s*(?:=|<>|IN)\s*(\([^)]*\)|'[A-Z_]+')",
                             sql, re.I):
            vals = set(re.findall(r"'([A-Z][A-Z_]+)'", m.group(1)))
            if vals:
                found.setdefault(enum, set()).update(vals)
    return found


ENUM_SETS = enum_members()


def test_enums_file_parsed():
    """A rename or move must fail loudly, not silently make the checks vacuous."""
    assert ENUM_SETS, f"no enums parsed from {ENUMS}"
    missing = sorted(set(ENUM_BACKED_CONSTANTS.values())
                     | set(ENUM_BACKED_HOUSING.values())
                     | set(ENUM_BACKED_INLINE.values())
                     | set(VIEW_COLUMNS.values()))
    missing = [e for e in missing if e not in ENUM_SETS]
    assert not missing, (
        f"this test references enums that no longer exist: {missing}. "
        f"They were renamed or removed — update the maps in this file and check "
        f"whether the generator and reporting_views.sql still write valid values."
    )


@pytest.mark.parametrize("enum,values", sorted(generator_values().items()))
def test_generator_writes_only_real_enum_members(enum, values):
    invalid = sorted(values - ENUM_SETS.get(enum, set()))
    assert not invalid, (
        f"generate_nsr_bulk_sample.py writes {invalid} for {enum}, which are not "
        f"members of it. Valid: {sorted(ENUM_SETS.get(enum, set()))}. The column "
        f"is a plain String so these INSERT silently, then fail on read."
    )


@pytest.mark.parametrize("enum,values", sorted(view_literals().items()))
def test_views_compare_only_real_enum_members(enum, values):
    invalid = sorted(values - ENUM_SETS.get(enum, set()))
    assert not invalid, (
        f"reporting_views.sql compares against {invalid} for {enum}, which are not "
        f"members of it. Valid: {sorted(ENUM_SETS.get(enum, set()))}."
    )


@pytest.mark.parametrize("enum,values", sorted(view_literals().items()))
def test_views_compare_values_the_generator_can_produce(enum, values):
    """A view predicate on a value never seeded is silently always-false.

    This is the check that matters when only one side gets fixed: aligning the
    generator to the enums while the views still said 'HEAD' would have made
    is_head false for every household, with nothing anywhere reporting an error.
    """
    produced = generator_values().get(enum, set())
    if not produced:
        pytest.skip(f"generator writes no {enum} values to compare against")
    unreachable = sorted(values - produced)
    assert not unreachable, (
        f"reporting_views.sql tests {enum} against {unreachable}, which the sample "
        f"generator never produces — the predicate is always false on seeded data. "
        f"Generator writes: {sorted(produced)}."
    )
