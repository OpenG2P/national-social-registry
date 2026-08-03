# NSR — Maps content for G2P Insights.
#
# The same split the db-seed image uses: the platform ships the MACHINERY, this
# image adds NSR's CONTENT.
#
#   openg2p-insights-evidence-builder   Evidence toolchain, node_modules, the
#                                       country-pack boundary sync, the build
#                                       script, and the `registry` connection
#   this image                          NSR's queries and its map page
#
# Why the content lives here and not in Insights: what a map DRAWS belongs to a
# registry. These queries read nsr_rpt_household and nsr_rpt_individual, and
# plot a poverty score — none of which exists in a Farmer Registry. Insights
# installed beside a different registry needs that registry's queries, exactly
# as Superset needs its dashboards. Keeping them in the platform would have made
# every Insights install silently assume NSR.
#
# The Insights chart runs this image as a Job after install and on a schedule:
# it extracts the SQL against the live registry into parquet, builds the static
# site, and publishes it to the volume the serving pods read.
#
#   insightMaps.build.image.repository = openg2p/openg2p-nsr-maps
#
# Build context = repo root (so docker/maps/ is reachable).
# Pinned to a published build, not a floating tag — the same convention the
# db-seed image uses for its registry-platform base. `0.0.0-develop` without a
# build number is not a tag that exists: CI publishes `0.0.0-develop.<n>` and
# `develop`, so the unnumbered form fails the pull.
ARG INSIGHTS_VERSION=0.0.0-develop.49
FROM registry.gitlab.com/openg2p/g2p-insights/openg2p-insights-evidence-builder:${INSIGHTS_VERSION}

# Replace the reference content wholesale rather than merging: a leftover
# reference query would run against NSR's database and fail the build, or worse
# succeed and put a meaningless panel on the page.
USER 0
RUN rm -f /app/sources/registry/*.sql /app/pages/*.md

COPY docker/maps/sources/ /app/sources/registry/
COPY docker/maps/pages/   /app/pages/

# sources/registry/connection.yaml is NOT copied — it comes from the base image
# and is the same for every registry: "the registry's database", with host and
# credentials supplied per environment at build time.
USER 1000
