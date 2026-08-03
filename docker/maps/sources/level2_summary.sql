-- Aggregates for the Maps surface at the second level below country (zone in ETH, district in XKM).
--
-- Named by DEPTH, not by level name. The reporting views unpack geography
-- positionally into geo_3/geo_3_id, so this query is identical for every
-- country; naming the file region/zone/woreda instead baked Ethiopia's
-- hierarchy into a surface that is supposed to work for any pack.
--
-- `pcode` joins to level<N>.geojson. Nothing is called `name`: Evidence's
-- map input proxy is a callable and a `name` field collides with
-- Function.name, which kills the map outright.
select
    h.geo_3_id       as pcode,
    h.geo_3    as area_name,
    h.geo_2_id   as parent_pcode,
    count(*)                                                              as households,
    sum(size_total)                                                       as individuals,
    round(avg(poverty_score)::numeric, 1)                                 as poverty_score,
    round(100.0 * avg(case when is_enrolled then 1 else 0 end), 1)        as pct_enrolled,
    round(100.0 * avg(case when is_female_headed then 1 else 0 end), 1)   as pct_female_headed,
    round(100.0 * avg(case when has_improved_water then 1 else 0 end), 1) as pct_improved_water,
    -- COUNTS, not rates. A rate needs a denominator big enough to survive one
    -- household moving; a count is exact whether the unit holds 17 households or
    -- 17,000, needs no suppression, and sums up the hierarchy. It is also the
    -- form an administrator can act on: "28 poorest households, none enrolled"
    -- is a work order, "12.4% covered" is not.
    count(*) filter (where poverty_quintile = 1 and not is_enrolled)      as poorest_not_enrolled,
    count(*) filter (where is_enrolled)                                   as enrolled_hh,
    count(*) filter (where ind.with_id = 0)                               as no_id_hh,
    -- Coverage of the poorest quintile: the headline targeting measure.
    round(100.0 * avg(case when poverty_quintile = 1 and is_enrolled then 1.0
                           when poverty_quintile = 1 then 0.0 end), 1)    as pct_poorest_covered,
    -- Payment readiness. A household whose members have no foundational ID
    -- cannot be paid even once it is enrolled, so this is an exclusion risk
    -- rather than a data-quality nicety.
    round(100.0 * avg(case when ind.with_id = 0 then 1 else 0 end), 1)    as pct_no_id
from nsr_rpt_household h
left join (
    select household_id,
           count(*) filter (where has_foundational_id) as with_id
    from nsr_rpt_individual
    group by household_id
) ind on ind.household_id = h.household_id
where h.geo_3_id is not null
group by 1, 2, 3
