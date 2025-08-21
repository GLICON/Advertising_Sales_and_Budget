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
- Excel (Data cleaning)
- pgSQL (Data querying)
- Statistical analysis and Panda Lib for data aggregation
- Power BI (Data Visualization)

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

## Exploratory Data Analysis (Python/Pandas)
Q1: TV Advertising Across Budget Ranges (Low, Medium, High, Very High)
Percentile is used to categorizxe the budget ranges:

Lower Quartile = QUARTILE.INC(B2:B201, 3) = 74.375 
Median = QUARTILE.INC(B2:B201, 3) = 149.75
Upper Quartile = QUARTILE.INC(B2:B201, 3) = 218.825

**Low**: less than $74.4
**Medium**: from $74.4 to $149.8
**High**: from $149.8 to $218.8
**Very High**: more than $218.8

Q2: TV and Radio/TV Effect (Newspaper < 10)
When Newspaper Ad Budget is minimal (less than $10), there are 42 relevant data points for analysis.



