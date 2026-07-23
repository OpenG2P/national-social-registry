# National Social Registry — sanity tests (field-specific, Set 2)

The NSR does **not** carry its own copy of the sanity suite. The registry-platform
publishes the whole suite as an image, `openg2p/openg2p-registry-sanity-tests`,
containing:

- the **harness** — signing, DCI envelope building, PM/CM/Keycloak/AWE seeding,
  DB helpers, step logging, and the `conftest.py` banners/fixtures;
- **Set 1 (extension-independent tests)** — `test_smoke.py` and
  `test_e2e_negative.py`: liveness, wiring, and the fail-closed cases (search
  without consent / bad signature / wrong audience is rejected). These are
  identical for every registry and run unchanged.

This directory holds only **Set 2 — the NSR's field-specific parts**, which
`docker/sanity-tests/Dockerfile` layers onto that base image (overwriting the
reference registry's versions at the same paths):

| File | What is NSR-specific |
|---|---|
| `sanity/fixtures.py`  | the seeded record + the `g2p_register_individuals` tables |
| `sanity/data_seed.py` | idempotent injection into `g2p_register_individuals` |
| `tests/test_e2e_dci.py` | assertions against the NSR DCI template |
| `tests/test_e2e_change_request.py` | the register/history rows are verified in the NSR tables |

Everything else (register id, DCI reg-type, search text, consent scopes, CR
tab/section) is **configuration**, supplied as env by the Helm chart's `sanity.*`
values — not baked here.

## A note on inherited names

`cfg.farmer_register_id` and the `farmer_seeded` pytest fixture are names owned by
the **inherited** harness and `conftest.py`. They are not NSR concepts — here they
simply carry NSR's Individual register and its seeded record.

## Extending

NSR's Individual register currently matches the platform's reference registry (the
reference was derived from NSR), so these files are close to the platform's own.
Owning them here means NSR's fields can diverge — new registers, a changed DCI
template, different UI coordinates — without touching the platform.
