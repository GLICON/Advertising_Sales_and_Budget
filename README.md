# Advertising_Sales_and_Budget
This data analysis evaluates the impacts of different advertising methods, including TV, Radio, and Newspaper campaigns on driving product sales, highlighting optimal strategies that will yield effective sales.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Questions](#questions)
- [Tools](#tools)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Data Extraction and Querying](#data-extraction-and-querying)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Results and Findings](#results-and-findings)
- [Recomendations](#recommendations)
- [Limitations](#limitations)
- [References](#references)

# Project Overview
This projects aims to analyze the relationship between advertising budgets across different media channels (TV, Radio, Newspaper) and their impact on sales. The objective is to uncover insights into how budget allocations influence sales outcomes, identify trends and provide actionabe recommendations for optimizing advertising strategies.

## Data Sources
The primary dataset is provided in the file "Advertising Budget and Sales.csv" containing 200 rows and 4 columns:
- TV Ad Budget ($): Budget allocated to TV advertising.
- Radio Ad Budget ($): Budget allocated to Radio advertising.
- Newspaper Ad Budget ($): Budget allocated to Newspaper advertising.
- Sales ($): Sales outcome from the advertising budgets combinations.

### Questions
1. How does the TV advertising vary across different budget ranges (e.g. Low, Medium or High)?

2. What is the combined effect of TV and Radio advertising on Sales when Newspaper spending is minimal (e.g. < $10)?

3. Are there specific combinations of advertising budgets that consistently lead to high sales (e.g. Sales > $20)?

### Tools
- Excel (Data Cleaning and Sorting)
- SQL (Data Querying)
- Excel (Statistical analysis and Data Visualization)

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

1. Imported "Advertising Budget and Sales.csv" into Excel
2. Checked for missing or null values
3. Ensured the numerical columns (e.g., TV Ad Budget, Radio Ad Budget, Newspaper Ad Budget and Sales) were kept as float for accurate computations
4. Checked for outliers using z-scores:
   - TV Ad Budget($): No extreme outliers
   - Radio Ad Budget($): No extreme outliers
   - Newspaper Ad Budget($): One outlier ($144)
   - Sales($): No extreme outliers
All outliers are deemed plausible.

### Data Extraction and Querying
The dataset is imported into pgSQL using the following query:
```sql
CREATE Table Advertisement_Budget_and_Sales (
      ID INTEGER PRIMARY KEY,
      tv_ad_budget FLOAT NOT NULL,
      radio_ad_budget FLOAT NOT NULL,
      newspaper_ad_budget FLOAT NOT NULL,
      sales FLOAT NOT NULL
);
```

1. **TV Budget Ranges (Low: < $100, Medium: $100-200, High: > $200)**:
This SQL query processes data from an advertising table, focusing on the TV Ad budget. It groups the data into three budget ranges, calculates aggregate statistics, and orders the results

```sql
SELECT
   CASE
      WHEN tV_ad_budget < 100 THEN 'Low'
      WHEN tV_ad_budget BETWEEN 100 AND 200 THEN 'Medium'
      ELSE 'High'
   END AS Budget_Range,
   COUNT (*) AS Count, AVG (tv_ad_budget) AS Avg_TV_Budget,
   MIN(TV_ad_budget) AS Min_TV_Budget,
   MAX (TV_ad_budget) AS Max_TV_Budget
FROM advertising
GROUP BY
   CASE
      WHEN TV_ad_budget < 100 THEN 'Low'
      WHEN TV_ad_budget BETWEEN 100 AND 200 THEN 'Medium'
      ELSE 'High'
   END
ORDER BY Avg_TV_Budget;
```
<img width="624" height="121" alt="Screenshot 2025-08-19 at 12 51 26" src="https://github.com/user-attachments/assets/88526529-e34a-4fd5-b1e8-211f27e61072" />

2. **Combined effect of TV and Radio only (Newspaper_Budget < 10)**:
The SQL query selects TV ad budget, radio ad budget, and sales ffrom the advertising dataset, filtering rows where Newspaper_ad_budget is less than $10, isolating TV and Radio's combined effect on sales.

```sql
SELECT tv_ad_budget, radio_ad_budget, sales
FROM advertising
WHERE Newspaper_ad_Budget < 10
```

3. **Budget Combinations (Sales > 20)**:
Budget combinations of TV, Radio and Newspaper ad budgets for a sales outcome greater than $20 are filtered using the query below.

```sql
SELECT tV_ad_budget, radio_ad_budget, newspaper_ad_budget, sales
FROM advertising
WHERE Sales > 20
ORDER BY Sales DESC;
```

## Exploratory Data Analysis
1. **TV Advertising across budget ranges (Low, Medium, High, Very High)**:
Alternatively, Quartile function on MS Excel is used to categorize the budget ranges:

Lower Quartile = QUARTILE.INC(B2:B201, 3) = 74.375, Median = QUARTILE.INC(B2:B201, 3) = 149.75, Upper Quartile = QUARTILE.INC(B2:B201, 3) = 218.825

2. **TV and Radio/TV Effect (Newspaper < 10)**:

When Newspaper Ad Budget is minimal (less than $10), there are 42 relevant data points for analysis.
The csv file 'newspaperlessthan10.csv' contains this dataset.

3. **Budget Combinations (Sales > 20)**:
The ad budgets combination that produced sales greater than $20 were evaluated to checj for consistency which may have led to high sales.

### Results and Findings
1.
**Low**: less than $74.4
**Medium**: from $74.4 to $149.8
**High**: from $149.8 to $218.8
**Very High**: more than $218.8

2.
<img width="743" height="460" alt="Screenshot 2025-08-23 at 22 52 56" src="https://github.com/user-attachments/assets/c4c6622e-e874-4f83-baaa-2f10cbf6e6cf" />

The regression output provides a model of how TV and Radio budgets both predict sales, with Newspaper spending < $10. The model is:
Sales = 2.4702 + 0.0483 × TV_ad_budget + 0.1737 × Radio_ad_budget

Key points from the regression:

a.	R-squared: 0.84 (84%) - TV and Radio together explain 84% of the variance in sales, indicating a strong combined effect and the adjusted R-squared (0.8325) confirms the model’s goodness of fit, accounting for the number of predictors.

b.	Coefficients:
Intercept: 2.4702 (p = 0.0062, significant) - Baseline sales when TV and Radio budgets are zero.

- TV_ad_budget: 0.0483 (p = 4.93E-15, highly significant). For each $1 increase in TV budget, sales increase by $0.0483, holding Radio constant.

- Radio_ad_budget: 0.1737 (p = 5.59E-09, highly significant) (i.e. for each $1 increase in Radio budget, sales increase by $0.1737, holding TV constant). Therefore, Radio has a higher per-dollar impact on sales compared to TV (0.1737 vs. 0.0483).
  
c.	Model Significance:
The F-statistic (100.43, p = 6.78E-16) indicates the overall model is highly significant, meaning TV and Radio budgets together reliably predict sales.

d.	Standard Error and Confidence Intervals:
- TV coefficient: 0.0483 ± 0.0078 (95% CI: 0.0405 to 0.0561)
- Radio coefficient: 0.1737 ± 0.0470 (95% CI: 0.1267 to 0.2207)
- Both coefficients are precise, with narrow confidence intervals, reinforcing their reliability.

**Effect of TV and Radio ads on Sales**

-**Individual Contributions**:
TV has a stronger correlation with sales (0.7916) than Radio (0.4584), suggesting TV ads is a more dominant driver of sales in this dataset.

A correlation of 0.79 for TV advertising indicates a strong linear relationship, meaning higher TV ad budgets are closely tied to increased sales. In contrast, a correlation of 0.46 for radio advertising suggests a moderate linear relationship, where higher radio ad budgets are associated with higher sales, but the connection is less robust than for TV. These correlations highlight TV's stronger impact on sales compared to radio.

-**Combined Impact**:
The high R-squared (0.8409) shows that TV and Radio together account for most of the variation in sales when Newspaper spending is minimal. R-squared value of 0.85 indicates that 85% of the variation in sales can be explained by the combined effect of TV and radio advertising budgets. This suggests a strong relationship between TV and Radio ad. spendings and sales when Newspapar ad is budgeted less than $10. The regression model suggests that both variables are significant predictors, and their combined effect is substantial, with no evidence of multicollinearity (TV and Radio correlation is near zero at -0.0159).

<img width="2007" height="1452" alt="newspaperlessthan10" src="https://github.com/user-attachments/assets/fc473da8-d43b-43d0-a265-842a429d27ba" />

Coefficients for TV ad budgdet: 0.048 and
Coefficients for Radio ad budget: 0.174

On the other hand, for each $1 increase in TV budget, sales increase by about 0.047 units, holding Radio ad budget constant while for each $1 increase in Radio budget, sales increase by about 0.176 units, holding TV ad budget constant.

3.
<img width="759" height="473" alt="Screenshot 2025-08-25 at 21 54 13" src="https://github.com/user-attachments/assets/dfc651b6-0d3e-4da8-9544-3e76a8012725" />

The regression output provides a model of how TV and Radio budgets together predict sales, with Newspaper spending < $10. The model is: Sales = -1.5015 + 0.0486 × TV_ad_budget + 0.3087 × Radio_ad_budget + 0.0011 × Newspaper

Key points from the regression:

a. R-squared: 0.9687 (96.87%) - The model explains 96.87% of sales variance, ensuring reliable predictions for identifying budget combinations that consistently achieve Sales > 20. The adjusted R-squared (0.9651) confirms the model’s robustness, supporting its use for optimizing TV and radio budgets.

b. Coefficients:
   - Intercept: -1.5015 (p = 0.112, not significant) - Baseline sales without advertising are negligible, requiring substantial TV and radio budgets to exceed Sales > 20. This emphasizes the need for active investment in effective channels like radio.
   - TV_ad_budget: 0.0486 (p = 1.69E-17, highly significant) - Each $1 in TV increases sales by 0.0486, contributing modestly to high sales when paired with radio. Combinations like TV = $300 + Radio = $30 (Sales ≈ $22.34) rely on TV as a secondary driver.
   - Radio_ad_budget: 0.3087 (p = 4.54E-20, highly significant) - Radio’s strong effect (0.3087 units per $1) drives Sales > 20 efficiently, as in Radio = 70 + TV = 10 (Sales ≈ 20.59). It’s the primary lever for consistent high sales due to its outsized impact.
   - Newspaper_ad_budget: 0.0011 (p = 0.705, not significant) - Newspaper has negligible impact, so excluding it from combinations maximizes budget efficiency. Resources are better allocated to radio and TV for Sales > 20.

c. Model Significance: F-statistic (268.61, p = 1.12E-19) shows the model is highly significant, validating its use for predicting high sales. This ensures combinations derived from the equation (e.g., 0.0486·TV + 0.3087·Radio > 21.5015) are reliable.

d. Standard Error and Confidence Intervals:
   - **TV**: 0.0486 ± 0.0024 (95% CI: 0.0436–0.0535) - The precise TV coefficient supports consistent contributions in combinations like TV = 200 + Radio = 50 (Sales ≈ 23.65). Narrow CI ensures reliability for planning high-sales strategies.
   - **Radio**: 0.3087 ± 0.0119 (95% CI: 0.2841–0.3332) - Radio’s large, precise effect confirms its dominance in achieving Sales > 20, as in Radio = 60 + TV = 100 (Sales ≈ 21.88). The tight CI reinforces confidence in radio-heavy budgets.
   - **Newspaper**: 0.0011 ± 0.0028 (95% CI: -0.0048–0.0069) - The CI spanning zero confirms newspaper ad’s irrelevance, so budgets should focus on radio and TV. This avoids wasting resources on ineffective channels for high sales.

**Combined trio effect**: To consistently achieve sales > 20, prioritize radio budgets ($50–70) with moderate TV budgets ($100–200), e.g., TV = $100, Radio = $60 (Sales ≈ $21.88) or TV = $10, Radio = $70 (Sales ≈ $20.59). Minimizing newspaper spending optimizes resources, as its effect is trivial. The equation 0.0486·TV + 0.3087·Radio > 21.5015 guides effective combinations, leveraging radio's  6.3x stronger per-dollar impact. The model’s reliability supports strategic planning, though linearity assumptions need further validation.

### Recommendations
The analysis shows that TV advertising has a strong positive correlation with sales (0.79), making it a critical channel. However, the marginal effect per $1 of TV spend (≈0.048) is smaller than the radio’s. This suggests that while TV should remain a cornerstone for brand visibility, allocating excessively high budgets to TV beyond the “High” range ($150–$220) yields diminishing returns. Therefore, businesses should focus on maintaining TV budgets in the medium-to-high range ($100–$200), ensuring consistent visibility while freeing resources for other impactful channels.

When newspaper spending is minimal (like less than $10), the regression shows TV and radio together explain 84% of sales variance. Radio delivers a stronger per-dollar impact (0.174 vs. 0.048 for TV). Hence, balancing TV for reach and radio for cost-effective sales lift is recommended. Firms should adopt a dual-focus strategy: maintain steady TV investment for broad market exposure, while strategically scaling radio to amplify immediate sales responses.

For sales over $20, the regression confirms radio as the dominant driver ($0.309 per $1 vs. $0.049 for TV). Firms should prioritize radio-heavy budgets (50–70 units) supported by moderate TV spend ($100–200) to consistently achieve Sales greater than $20, while minimizing newspaper ad spendings. This combination provides the most reliable path to strong sales performance.

### Limitations
The analysis has three main limitations. First, the dataset only covers TV, Radio, and Newspaper advertising, leaving out other influential factors such as digital marketing, pricing, competitor activity, or seasonality. Including these variables would provide a more complete understanding of what drives sales. Additionally, the regression models assume a strictly linear relationship between advertising spend and sales. In practice, the effect of advertising may follow patterns of diminishing returns or thresholds, which could be better captured through non-linear models. Third, the findings are specific to this dataset and may not generalize to other industries or markets. Testing the approach on larger, industry-specific datasets would improve the reliability and applicability of the results.

### References
- Dataset gotten from Kaggle uploaded by MUHAMMAD SAAD
