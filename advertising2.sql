SELECT
  CASE
    WHEN tV_ad_budget ‹ 100 THEN 'Low'
    WHEN tV_ad_budget BETWEEN 100 AND 200 THEN 'Medium'
    ELSE 'High'
  END AS Budget_Range,
  COUNT (*) AS Count, 
  AVG (tv_ad_budget) AS Avg_TV_Budget, 
  MIN(TV_ad_budget) AS Min_TV_Budget,
  MAX (TV_ad_budget) AS Max_TV_Budget
FROM advertising
GROUP BY
  CASE
    WHEN TV_ad_budget ‹ 100 THEN 'Low'
    WHEN TV_ad_budget BETWEEN 100 AND 200 THEN 'Medium'
    ELSE 'High'
  END
ORDER BY Avg_TV_Budget;
