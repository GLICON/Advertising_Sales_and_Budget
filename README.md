# Advertising_Sales_and_Budget
This data analyses the impact of different means of advertisement on the product sales

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
This projects aims to analyze the relationship between advertising budgets across different media channels (TV, Radio, Newspaper) and their impact on sales. The objective is to unconer insights intonhow budget allocations influence sales outcomes, identoify trends and provide actionabe recommendations for optimizing advertising strategies.

## Data Sources
The primare dataset is provided in the file "Advertising Budget and Sales.csv" containing 200 rows and 4 columns:
- TV Ad Budget ($): Budget allocated to TV advertising.
- Radio Ad Budget ($): Budget allocated to Radio advertising.
- Newspaper Ad Budget ($): Budget allocated to Newspaper advertising.
- Sales ($): Sales figures associated with the advertising budgets.

### Questions
1. How does the TV advertising vary across different budget ranges (e.g. Low, Medium or High)?
   
2. What is the combined effect of TV and Radio advertising on sales when Newspaper spending is minimal (e.g. < 10)?
  
3. Are there specific combinations of advertising budgets that consistently lead to high sales (e.g. Sales > 20)?

### Tools
- Excel (Data cleaning, sorting, statistical analysis and Visualization)
- pgSQL (Data querying)

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

1. Import "Advertising Budget and Sales.csv" into Excel
2. Checked for missing or null values
3. Ensured the numerical columns (e.g., TV Ad Budget, Radio Ad Budget, Newspaper Ad Budget and Sales) were kept as float for accurate computations
4. Checked for outliers using z-scores:
   - TV Ad Budget ($): No extreme outliers
   - Radio Ad Budget ($): No extreme outliers
   - Newspaper Ad Budget ($): One outlier (144)
   - Sales ($): No extreme outliers
All outliers are demmed plausible.

### Data Extraction and Querying
The dataset is imported into pgSQL using the following query:
<img width="487" height="138" alt="Screenshot 2025-08-09 at 12 33 24" src="https://github.com/user-attachments/assets/1ee6323b-709e-4a26-8ec3-424fd13c96d8" />

1. TV Budget Ranges (Low: <100, Medium: 100-200, High: >200)
<img width="512" height="354" alt="Screenshot 2025-08-19 at 12 54 04" src="https://github.com/user-attachments/assets/04cf2e2a-e942-477a-89f5-973ff9affee6" />

<img width="624" height="121" alt="Screenshot 2025-08-19 at 12 51 26" src="https://github.com/user-attachments/assets/88526529-e34a-4fd5-b1e8-211f27e61072" />

2. Combined effect of TV and Radio only (Newspaper_Budget < 10)
<img width="410" height="93" alt="Screenshot 2025-08-19 at 13 05 39" src="https://github.com/user-attachments/assets/b60e05d3-8746-4f8e-b7bd-0bf7576416d6" />

3. Budget Combinations (Sales > 20)
<img width="570" height="91" alt="Screenshot 2025-08-19 at 13 37 04" src="https://github.com/user-attachments/assets/f32d1caa-23b7-4cfb-9a17-b0912825f9f6" />

## Exploratory Data Analysis (Statistical Analysis)
1. TV Advertising Across Budget Ranges (Low, Medium, High, Very High)
Percentile is used to categorizxe the budget ranges:

Lower Quartile = QUARTILE.INC(B2:B201, 3) = 74.375 
Median = QUARTILE.INC(B2:B201, 3) = 149.75
Upper Quartile = QUARTILE.INC(B2:B201, 3) = 218.825

2. TV and Radio/TV Effect (Newspaper < 10)
When Newspaper Ad Budget is minimal (less than $10), there are 42 relevant data points for analysis.
The csv file 'newspaperlessthan10.csv' contains this dataset.

3: Budget Combinations (Sales > 20)

## Results and Findings
1.
**Low**: less than $74.4
**Medium**: from $74.4 to $149.8
**High**: from $149.8 to $218.8
**Very High**: more than $218.8

2.
<img width="743" height="460" alt="Screenshot 2025-08-23 at 22 52 56" src="https://github.com/user-attachments/assets/c4c6622e-e874-4f83-baaa-2f10cbf6e6cf" />

The regression output provides a model of how TV and Radio budgets together predict sales, with Newspaper spending < $10. The model is:
Sales = 2.4702 + 0.0483 × TV_ad_budget + 0.1737 × Radio_ad_budget

Key points from the regression:
a.	R-squared: 0.84 (84%) - TV and Radio together explain 84% of the variance in sales, indicating a strong combined effect and the adjusted R-squared (0.8325) confirms the model’s goodness of fit, accounting for the number of predictors.

b.	Coefficients:
Intercept: 2.4702 (p = 0.0062, significant) Baseline sales when TV and Radio budgets are zero.

- TV_ad_budget: 0.0483 (p = 4.93E-15, highly significant)
	For each $1 increase in TV budget, sales increase by 0.0483 units, holding Radio constant.

- Radio_ad_budget: 0.1737 (p = 5.59E-09, highly significant) (i.e. for each $1 increase in Radio budget, sales increase by 0.1737 units, holding TV constant). Therefore, Radio has a higher per-dollar impact on sales compared to TV (0.1737 vs. 0.0483).
  
c.	Model Significance:
The F-statistic (100.43, p = 6.78E-16) indicates the overall model is highly significant, meaning TV and Radio budgets together reliably predict sales.

d.	Standard Error and Confidence Intervals:
- TV coefficient: 0.0483 ± 0.0078 (95% CI: 0.0405 to 0.0561)
- Radio coefficient: 0.1737 ± 0.0470 (95% CI: 0.1267 to 0.2207)
- Both coefficients are precise, with narrow confidence intervals, reinforcing their reliability.
Combined Effect of TV and Radio

**Individual Contributions**:
- TV has a stronger correlation with sales (0.7916) than Radio (0.4584), suggesting TV ads is a more dominant driver of sales in this dataset.

A correlation of 0.79 for TV advertising indicates a strong linear relationship, meaning higher TV ad budgets are closely tied to increased sales. In contrast, a correlation of 0.46 for radio advertising suggests a moderate linear relationship, where higher radio ad budgets are associated with higher sales, but the connection is less robust than for TV. These correlations highlight TV's stronger impact on sales compared to radio.

**Combined Impact**:
- The high R-squared (0.8409) shows that TV and Radio together account for most of the variation in sales when Newspaper spending is minimal. R-squared value of 0.85 indicates that 85% of the variation in sales can be explained by the combined effect of TV and radio advertising budgets. This suggests a strong relationship between TV and Radio ad spendings and sales when Newspapar ad is budgeted less than $10. The regression model suggests that both variables are significant predictors, and their combined effect is substantial, with no evidence of multicollinearity (TV and Radio correlation is near zero at -0.0159).

Coeffiicients for TV ad budgdet: 0.048 and
Coefficients for Radio ad budget: 0.174

On the other hand, for each $1 increase in TV budget, sales increase by about 0.047 units, holding Radio ad budget constant while for each $1 increase in Radio budget, sales increase by about 0.176 units, holding TV ad budget constant.

3. 


