--Quarterly Aggregation View--

CREATE OR REPLACE VIEW `driiiportfolio.tvc_grants.quarterly_performance` AS
SELECT
  grantee_id,
  county,
  program_type,
  EXTRACT(QUARTER FROM reporting_month) AS quarter,
  SUM(veterans_served) AS total_served,
  SUM(funds_expended) AS total_expended,
  SUM(benchmark_target) AS total_benchmark,
  SAFE_DIVIDE(
    SUM(veterans_served) - SUM(benchmark_target),
    SUM(benchmark_target)
  ) AS percent_variance
FROM `driiiportfolio.tvc_grants.performance_reports`
GROUP BY grantee_id, county, program_type, quarter;
