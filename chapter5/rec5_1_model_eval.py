import numpy as np
from scipy import stats

#!/usr/bin/env python3
# rec5_1_model_eval.py --- Recipe 89 to 94 --- Test the null hypothesis of zero slope in simple linear regression
# Simple linear regression example: Education vs Salary
# Dataset: 15 random professionals stored as dictionaries with keys "Education" and "Salary"

import matplotlib.pyplot as plt

np.random.seed(42)

# Base average salaries by education (in dollars)
base_salary = {
    "High School": 25000,
    "Associate": 40000,
    "Bachelor": 70000,
    "Master": 110000,
    "PhD": 230000,
}

# Ordered encoding of education levels for regression
edu_order = ["High School", "Associate", "Bachelor", "Master", "PhD"]
edu_to_num = {e: i + 1 for i, e in enumerate(edu_order)}  # 1..5

# Generate 15 random professionals (keeps the stated averages but adds small noise)
n = 15
educations = np.random.choice(edu_order, size=n, p=[0.2, 0.15, 0.35, 0.2, 0.1])
professionals = []
for edu in educations:
    # add realistic noise around the base salary
    noise = int(np.random.normal(loc=0, scale=8000))
    salary = max(10000, base_salary[edu] + noise)  # ensure salary non-negative
    professionals.append({"Education": edu, "Salary": salary})

# Prepare data for regression
x = np.array([edu_to_num[p["Education"]] for p in professionals], dtype=float)
y = np.array([p["Salary"] for p in professionals], dtype=float)

# Fit simple linear regression (y = slope * x + intercept)
slope, intercept = np.polyfit(x, y, 1)
y_pred = slope * x + intercept

# Calculate R^2
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot

# Print dataset and regression summary
print("Dataset (15 professionals):")
for i, p in enumerate(professionals, 1):
    print(f"{i:2d}. Education: {p['Education']:<12}  Salary: ${p['Salary']:,.0f}")

print("\nEncoding:", edu_to_num)
print(f"\nLinear regression: Salary = {slope:,.2f} * EducationLevel + {intercept:,.2f}")
print(f"R^2 = {r2:.3f}")
print("\nInterpretation: positive slope indicates higher education level is associated with higher average salary.")

# Plot scatter (with x jitter for readability) and fitted line
jitter = (np.random.rand(n) - 0.5) * 0.12
x_jitter = x + jitter
plt.figure(figsize=(8, 5))
plt.scatter(x_jitter, y, color="tab:blue", label="Observed salaries")
# plot predicted line across the continuous education axis
x_line = np.linspace(1, 5, 100)
plt.plot(x_line, slope * x_line + intercept, color="tab:red", label="Fitted line")
plt.xticks(list(edu_to_num.values()), edu_order)
plt.xlabel("Education level")
plt.ylabel("Salary (USD)")
plt.title("Simple Linear Regression: Education (encoded) vs Salary")
plt.grid(alpha=0.2)
plt.legend()
plt.tight_layout()
plt.show()

def test_null_hypothesis(x, y, alpha=0.05, two_sided=True):
    """
    Test H0: slope == 0 for simple linear regression of y on x.
    Returns a dict with slope, intercept, se_slope, t_stat, df, p_value, and reject (bool).
    """
    # FIX: Use the global stats import, don't shadow it
    global stats
    
    n = len(x)
    if n < 3:
        raise ValueError("Need at least 3 observations to perform the test")

    slope, intercept = np.polyfit(x, y, 1)
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    s_xx = np.sum((x - np.mean(x)) ** 2)
    se_slope = np.sqrt(ss_res / (n - 2) / s_xx)
    t_stat = slope / se_slope
    df = n - 2

    # FIX: stats is now the global scipy.stats import
    if two_sided:
        p_value = 2.0 * stats.t.sf(abs(t_stat), df)
    else:
        p_value = stats.t.sf(t_stat, df)
    reject = p_value < alpha

    # Print a concise assertion/result
    print("Null hypothesis: slope = 0")
    print(f"Estimated slope = {slope:.6f}, SE = {se_slope:.6f}, t = {t_stat:.3f}, df = {df}")
    side = "two-sided" if two_sided else "one-sided"
    print(f"p-value ({side}) = {p_value:.4g}; alpha = {alpha}")
    print("Decision:", "Reject H0 ✓" if reject else "Fail to reject H0")

    return {
        "slope": slope,
        "intercept": intercept,
        "se_slope": se_slope,
        "t_stat": t_stat,
        "df": df,
        "p_value": p_value,
        "reject": reject,
    }

# Run the test on the current dataset
test_result = test_null_hypothesis(x, y, alpha=0.05)
print("-"*20+"\nTest result:", test_result)

# Print comprehensive model performance metrics
print("\n\n\n\n" + "="*50)
print("MODEL PERFORMANCE METRICS")
print("="*50)

# Basic regression metrics
print(f"\nSlope (coefficient): {slope:,.2f}")
print(f"Intercept: {intercept:,.2f}")
print(f"R-squared (R²): {r2:.4f}")
print(f"Adjusted R²: {1 - (1 - r2) * (n - 1) / (n - 2):.4f}")

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(np.mean((y - y_pred) ** 2))
print(f"RMSE: ${rmse:,.2f}")

# Mean Absolute Error (MAE)
mae = np.mean(np.abs(y - y_pred))
print(f"MAE: ${mae:,.2f}")

# Correlation coefficient
correlation = np.corrcoef(x, y)[0, 1]
print(f"Correlation coefficient (r): {correlation:.4f}")

# Statistical significance from test_null_hypothesis
print("\n" + "-"*50)
print("STATISTICAL SIGNIFICANCE TEST")
print("-"*50)
print(f"t-statistic: {test_result['t_stat']:.4f}")
print(f"Degrees of freedom: {test_result['df']}")
print(f"p-value (two-sided): {test_result['p_value']:.6f}")
print(f"Significance level (α): 0.05")
print(f"Result: {'*** SIGNIFICANT ***' if test_result['reject'] else 'Not significant'}")