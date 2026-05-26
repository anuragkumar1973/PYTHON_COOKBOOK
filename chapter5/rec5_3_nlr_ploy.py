# ============================================================================
# rec5_3_nlr_poly.py --- Recipe 104 to 111 --- Non-linear Regression with Polynomial Features
# PROGRAM: Non-linear Regression with Polynomial Features
# SETUP INSTRUCTIONS: Install Required Libraries
# ============================================================================
#
# Before running this program, install the required Python packages by
# running the following command in your terminal:
#
#   pip install numpy scipy matplotlib scikit-learn
#
# This installs:
#   • numpy       - Numerical computations and arrays
#   • scipy       - Scientific computing (curve fitting, optimization)
#   • matplotlib  - Data visualization and plotting
#   • scikit-learn - Machine learning algorithms (for linear regression)
#
# To verify installation, run:
#   python3 -c "import numpy, sklearn, matplotlib; print('✓ All libraries installed')"
#
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ============================================================================
# GENERATE DATA
# ============================================================================

np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1)  # Reshape for sklearn
y = 2 * X.flatten()**2 + 3 * X.flatten() + np.random.normal(0, 5, 50)

# ============================================================================
# BUILD POLYNOMIAL REGRESSION MODEL (QUADRATIC)
# ============================================================================

# Create polynomial features (x, x^2)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Train linear regression on polynomial features
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
y_pred = model.predict(X_poly)

# Calculate R-squared
r_squared = r2_score(y, y_pred)

# ============================================================================
# PRINT MODEL DETAILS
# ============================================================================

print("=" * 50)
print("NON-LINEAR REGRESSION MODEL DETAILS")
print("=" * 50)
print(f"Model: y = a*x² + b*x + c")
print(f"\nParameters:")
print(f"  a (x² coefficient): {model.coef_[2]:.6f}")
print(f"  b (x coefficient):  {model.coef_[1]:.6f}")
print(f"  c (intercept):      {model.intercept_:.6f}")
print(f"\nModel Performance:")
print(f"  R-squared: {r_squared:.6f}")
ss_res = np.sum((y - y_pred)**2)
print(f"  Residual Sum of Squares: {ss_res:.6f}")
print("=" * 50)

# ============================================================================
# PLOT TRAINING DATA AND FITTED CURVE
# ============================================================================

plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Data points', alpha=0.6)
plt.plot(X, y_pred, 'r-', linewidth=2, label='Fitted curve')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(fontsize=11)
plt.title('Non-linear Regression (Polynomial Degree 2)', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================================
# TEST THE MODEL WITH SAMPLE DATA POINTS
# ============================================================================

test_data = {
    'set1': {'x': np.array([2, 5, 8]), 'y': np.array([16, 68, 150])},
    'set2': {'x': np.array([1, 3, 7]), 'y': np.array([8, 36, 115])}
}

# Calculate predictions and errors for each test set
results = []
for set_name, test_set in test_data.items():
    X_test = test_set['x'].reshape(-1, 1)
    X_test_poly = poly_features.transform(X_test)
    y_test_pred = model.predict(X_test_poly)
    
    mse = mean_squared_error(test_set['y'], y_test_pred)
    mae = mean_absolute_error(test_set['y'], y_test_pred)
    
    results.append(f"{set_name.upper()}:\n  Predictions: {y_test_pred}\n  Actual: {test_set['y']}\n  MSE: {mse:.4f}\n  MAE: {mae:.4f}\n")

# Display results
test_result_text = "MODEL TEST RESULTS\n" + "=" * 40 + "\n\n" + "\n".join(results)
print(test_result_text)

plt.figure(figsize=(8, 6))
plt.text(0.1, 0.5, test_result_text, fontsize=12, family='monospace', verticalalignment='center')
plt.axis('off')
plt.title('Model Test Results')
plt.tight_layout()
plt.show()

# ============================================================================
# INTERPRET TEST RESULTS IN LAYMAN'S TERMS
# ============================================================================

interpretations = []
for set_name, test_set in test_data.items():
    X_test = test_set['x'].reshape(-1, 1)
    X_test_poly = poly_features.transform(X_test)
    y_test_pred = model.predict(X_test_poly)
    
    mse = mean_squared_error(test_set['y'], y_test_pred)
    mae = mean_absolute_error(test_set['y'], y_test_pred)
    
    # Interpret MSE and MAE
    if mae < 5:
        interpretation = "Excellent! The model predictions are very close to actual values."
    elif mae < 15:
        interpretation = "Good! The model predictions are reasonably close to actual values."
    elif mae < 30:
        interpretation = "Fair. The model has moderate prediction errors."
    else:
        interpretation = "Poor. The model predictions differ significantly from actual values."
    
    interpretations.append(f"{set_name.upper()}:\n  Predictions: {y_test_pred}\n  Actual: {test_set['y']}\n  MSE: {mse:.4f}\n  MAE: {mae:.4f}\n  Interpretation: {interpretation}\n")

# Display results with interpretations
interpreted_text = "MODEL TEST RESULTS & INTERPRETATIONS\n" + "=" * 50 + "\n\n" + "\n".join(interpretations)
print(interpreted_text)

plt.figure(figsize=(10, 8))
plt.text(0.05, 0.95, interpreted_text, fontsize=10, family='monospace', verticalalignment='top', wrap=True)
plt.axis('off')
plt.title('Model Test Results with Interpretations')
plt.tight_layout()
plt.show()