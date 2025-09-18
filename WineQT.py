import pandas as pd
from scipy.stats import ttest_ind

# Load the filtered dataset
df = pd.read_csv("wineQT_filtered.csv")

# Compute Pearson correlations between chemical properties and quality
chemical_columns = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'density', 
                    'ph', 'sulphates', 'alcohol']
correlation = df[chemical_columns + ['quality']].corr()['quality'].drop('quality')
print("Correlation with Quality (Sorted by Absolute Value):")
print(correlation.abs().sort_values(ascending=False))
print("\nCorrelation Details:")
print(correlation.sort_values(ascending=False))

# Group wines by quality categories: High-Quality (7+) and Standard (5-6)
high_quality = df[df['quality'] >= 7][chemical_columns]
standard_quality = df[(df['quality'] >= 5) & (df['quality'] <= 6)][chemical_columns]

# Compute mean values for each group
high_quality_means = high_quality.mean()
standard_quality_means = standard_quality.mean()

# Combine means into a DataFrame for comparison
mean_comparison = pd.DataFrame({
    'High-Quality (7+) Mean': high_quality_means,
    'Standard (5-6) Mean': standard_quality_means,
    'Difference (High - Standard)': high_quality_means - standard_quality_means
})
print("\nMean Chemical Properties Comparison:")
print(mean_comparison)

# 3. Perform t-tests to check significance of differences
print("\nT-test p-values (High-Quality vs. Standard):")
for column in chemical_columns:
    t_stat, p_value = ttest_ind(high_quality[column], standard_quality[column], nan_policy='omit')
    print(f"{column}: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")

# 4. Count wines in each quality category for context
quality_counts = df['quality'].value_counts().sort_index()
print("\nQuality Distribution:")
print(quality_counts)
