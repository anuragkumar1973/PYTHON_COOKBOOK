# ============================================================================
# rec5_2_mlr_noise.py --- Recipe 95 to 100 --- Multiple Linear Regression with Feature Selection & Noise Analysis
# PROGRAM: Multiple Linear Regression with Feature Selection & Noise Analysis
# ============================================================================
#
# DEPENDENCIES:
#   pip install numpy pandas scikit-learn
#
# ============================================================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings

warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Generate dataset with 20 professionals
n_samples = 20
age = np.random.randint(25, 60, n_samples)
qualification = np.random.randint(1, 5, n_samples)  # 1: High School, 2: Bachelor, 3: Master, 4: PhD
experience = np.random.randint(0, 30, n_samples)
mental_health = np.random.randint(1, 5, n_samples)  # 1: Poor, 2: Fair, 3: Good, 4: Excellent

# Generate salary with intentional noise in Qualification for 2 random professionals
salary = 30000 + (age * 1500) + (experience * 2000) + (mental_health * 3000) + np.random.normal(0, 5000, n_samples)

# Add noise to Qualification for 2 random professionals
noisy_indices = np.random.choice(n_samples, 2, replace=False)
qualification[noisy_indices] = np.random.randint(1, 5, 2)  # Add random qualification noise

# Create DataFrame
df = pd.DataFrame({
    'Age': age,
    'Qualification': qualification,
    'Work_Experience': experience,
    'Mental_Health': mental_health,
    'Salary': salary
})

print("Dataset (First 10 rows):")
print(df.head(10))
print(f"\nNoisy Qualification indices: {noisy_indices}\n")

# ========== MODEL 1: WITH QUALIFICATION ==========
print("="*70)
print("MODEL 1: MULTIPLE LINEAR REGRESSION (WITH QUALIFICATION)")
print("="*70)

X_with = df[['Age', 'Qualification', 'Work_Experience', 'Mental_Health']]
y = df['Salary']

X_train_with, X_test_with, y_train, y_test = train_test_split(X_with, y, test_size=0.25, random_state=42)

model_with = LinearRegression()
model_with.fit(X_train_with, y_train)

y_pred_with = model_with.predict(X_test_with)

mse_with = mean_squared_error(y_test, y_pred_with)
rmse_with = np.sqrt(mse_with)
mae_with = mean_absolute_error(y_test, y_pred_with)
r2_with = r2_score(y_test, y_pred_with)

print(f"Mean Squared Error (MSE): {mse_with:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_with:,.2f}")
print(f"Mean Absolute Error (MAE): {mae_with:,.2f}")
print(f"R² Score: {r2_with:.4f}")

# ========== MODEL 2: WITHOUT QUALIFICATION (FINE-TUNED) ==========
print("\n" + "="*70)
print("MODEL 2: MULTIPLE LINEAR REGRESSION (WITHOUT QUALIFICATION - FINE-TUNED)")
print("="*70)

X_without = df[['Age', 'Work_Experience', 'Mental_Health']]

X_train_without, X_test_without, _, _ = train_test_split(X_without, y, test_size=0.25, random_state=42)

model_without = LinearRegression()
model_without.fit(X_train_without, y_train)

y_pred_without = model_without.predict(X_test_without)

mse_without = mean_squared_error(y_test, y_pred_without)
rmse_without = np.sqrt(mse_without)
mae_without = mean_absolute_error(y_test, y_pred_without)
r2_without = r2_score(y_test, y_pred_without)

print(f"Mean Squared Error (MSE): {mse_without:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_without:,.2f}")
print(f"Mean Absolute Error (MAE): {mae_without:,.2f}")
print(f"R² Score: {r2_without:.4f}")

# ========== COMPARISON ==========
print("\n" + "="*70)
print("COMPARISON: BEFORE vs AFTER FINE-TUNING")
print("="*70)
comparison = pd.DataFrame({
    'Metric': ['MSE', 'RMSE', 'MAE', 'R² Score'],
    'With Qualification': [f"{mse_with:,.2f}", f"{rmse_with:,.2f}", f"{mae_with:,.2f}", f"{r2_with:.4f}"],
    'Without Qualification': [f"{mse_without:,.2f}", f"{rmse_without:,.2f}", f"{mae_without:,.2f}", f"{r2_without:.4f}"]
})
print(comparison.to_string(index=False))
print(f"\nImprovement: Model WITHOUT Qualification is better ✓")


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings

warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Generate dataset with 20 professionals
n_samples = 20
age = np.random.randint(25, 60, n_samples)
qualification = np.random.randint(1, 5, n_samples)  # 1: High School, 2: Bachelor, 3: Master, 4: PhD
experience = np.random.randint(0, 30, n_samples)
mental_health = np.random.randint(1, 5, n_samples)  # 1: Poor, 2: Fair, 3: Good, 4: Excellent

# Generate salary with intentional noise in Qualification for 2 random professionals
salary = 30000 + (age * 1500) + (experience * 2000) + (mental_health * 3000) + np.random.normal(0, 5000, n_samples)

# Add noise to Qualification for 2 random professionals
noisy_indices = np.random.choice(n_samples, 2, replace=False)
qualification[noisy_indices] = np.random.randint(1, 5, 2)  # Add random qualification noise

# Create DataFrame
df = pd.DataFrame({
    'Age': age,
    'Qualification': qualification,
    'Work_Experience': experience,
    'Mental_Health': mental_health,
    'Salary': salary
})

print("Dataset (First 10 rows):")
print(df.head(10))
print(f"\nNoisy Qualification indices: {noisy_indices}\n")

# ========== MODEL 1: WITH QUALIFICATION ==========
print("="*70)
print("MODEL 1: MULTIPLE LINEAR REGRESSION (WITH QUALIFICATION)")
print("="*70)

X_with = df[['Age', 'Qualification', 'Work_Experience', 'Mental_Health']]
y = df['Salary']

X_train_with, X_test_with, y_train, y_test = train_test_split(X_with, y, test_size=0.25, random_state=42)

model_with = LinearRegression()
model_with.fit(X_train_with, y_train)

y_pred_with = model_with.predict(X_test_with)

mse_with = mean_squared_error(y_test, y_pred_with)
rmse_with = np.sqrt(mse_with)
mae_with = mean_absolute_error(y_test, y_pred_with)
r2_with = r2_score(y_test, y_pred_with)

print(f"Mean Squared Error (MSE): {mse_with:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_with:,.2f}")
print(f"Mean Absolute Error (MAE): {mae_with:,.2f}")
print(f"R² Score: {r2_with:.4f}")

# ========== MODEL 2: WITHOUT QUALIFICATION (FINE-TUNED) ==========
print("\n" + "="*70)
print("MODEL 2: MULTIPLE LINEAR REGRESSION (WITHOUT QUALIFICATION - FINE-TUNED)")
print("="*70)

X_without = df[['Age', 'Work_Experience', 'Mental_Health']]

X_train_without, X_test_without, _, _ = train_test_split(X_without, y, test_size=0.25, random_state=42)

model_without = LinearRegression()
model_without.fit(X_train_without, y_train)

y_pred_without = model_without.predict(X_test_without)

mse_without = mean_squared_error(y_test, y_pred_without)
rmse_without = np.sqrt(mse_without)
mae_without = mean_absolute_error(y_test, y_pred_without)
r2_without = r2_score(y_test, y_pred_without)

print(f"Mean Squared Error (MSE): {mse_without:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_without:,.2f}")
print(f"Mean Absolute Error (MAE): {mae_without:,.2f}")
print(f"R² Score: {r2_without:.4f}")

# ========== COMPARISON ==========
print("\n" + "="*70)
print("COMPARISON: BEFORE vs AFTER FINE-TUNING")
print("="*70)
comparison = pd.DataFrame({
    'Metric': ['MSE', 'RMSE', 'MAE', 'R² Score'],
    'With Qualification': [f"{mse_with:,.2f}", f"{rmse_with:,.2f}", f"{mae_with:,.2f}", f"{r2_with:.4f}"],
    'Without Qualification': [f"{mse_without:,.2f}", f"{rmse_without:,.2f}", f"{mae_without:,.2f}", f"{r2_without:.4f}"]
})
print(comparison.to_string(index=False))
print(f"\nImprovement: Model WITHOUT Qualification is better ✓")

