-- Poverty-quintile composition of each zone, for a 100% stacked bar.
--
-- Long format (one row per zone per quintile) because that is what a stacked
-- series wants. Quintile 1 is ALWAYS the poorest — see reporting_views.sql, where
-- a higher computed score means poorer and the ntile is therefore ordered
-- descending.
--
-- Shares are safe here without suppression: a zone holds ~120 households, well
-- above the ~30 a percentage needs before one household stops swinging it.
select
    h.geo_3_id  as pcode,
    h.geo_3     as area_name,
    h.geo_2_id  as parent_pcode,
    'Q' || h.poverty_quintile::text as quintile,
    count(*)    as households
from nsr_rpt_household h
where h.geo_3_id is not null and h.poverty_quintile is not null
group by 1, 2, 3, 4
