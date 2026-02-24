--NULL CHECKS--

SELECT *
FROM `driiiportfolio.tvc_grants.performance_reports`
WHERE grantee_id IS NULL
   OR reporting_month IS NULL;

--Negative Value Checks--

SELECT *
FROM `driiiportfolio.tvc_grants.performance_reports`
WHERE veterans_served < 0
   OR funds_expended < 0;

--Duplicate Detection--

SELECT
  grantee_id,
  reporting_month,
  COUNT(*) AS duplicate_count
FROM `driiiportfolio.tvc_grants.performance_reports`
GROUP BY grantee_id, reporting_month
HAVING COUNT(*) > 1;
