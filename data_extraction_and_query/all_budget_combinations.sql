SELECT tV_ad_budget, radio_ad_budget, newspaper_ad_budget, sales
FROM advertising
WHERE Sales > 20
ORDER BY Sales DESC;
