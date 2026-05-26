# ============================================================================
# rec5_3_nlr_non_poly.py --- Recipe 100 to 103 --- Non-linear Regression with Curve Fitting
# PROGRAM: Non-linear Regression with Curve Fitting
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
#   • scikit-learn - Machine learning algorithms (optional for this script)
#
# To verify installation, run:
#   python3 -c "import numpy, scipy, matplotlib; print('✓ All libraries installed')"
#
# ============================================================================

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress

import matplotlib.pyplot as plt

# Generate data in a dictionary
data = {
    'x': np.linspace(0, 10, 50),
    'y': None
}

# Create non-linear relationship: y = 2*x^2 + 3*x + noise
np.random.seed(42)
data['y'] = 2 * data['x']**2 + 3 * data['x'] + np.random.normal(0, 5, len(data['x']))

# Define non-linear function (quadratic)
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model
params, covariance = curve_fit(quadratic, data['x'], data['y'])
a, b, c = params

# Calculate R-squared
y_pred = quadratic(data['x'], a, b, c)
ss_res = np.sum((data['y'] - y_pred)**2)
ss_tot = np.sum((data['y'] - np.mean(data['y']))**2)
r_squared = 1 - (ss_res / ss_tot)

# Print model details
print("=" * 50)
print("NON-LINEAR REGRESSION MODEL DETAILS")
print("=" * 50)
print(f"Model: y = a*x² + b*x + c")
print(f"\nParameters:")
print(f"  a (x² coefficient): {a:.6f}")
print(f"  b (x coefficient):  {b:.6f}")
print(f"  c (intercept):      {c:.6f}")
print(f"\nModel Performance:")
print(f"  R-squared: {r_squared:.6f}")
print(f"  Residual Sum of Squares: {ss_res:.6f}")
print("=" * 50)

# Plot
plt.scatter(data['x'], data['y'], label='Data points')
plt.plot(data['x'], y_pred, 'r-', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Non-linear Regression')
plt.show()

# Test the model with sample data points
test_data = {
    'set1': {'x': np.array([2, 5, 8]), 'y': np.array([16, 68, 150])},
    'set2': {'x': np.array([1, 3, 7]), 'y': np.array([8, 36, 115])}
}

# Calculate predictions and errors for each test set
results = []
for set_name, test_set in test_data.items():
    y_test_pred = quadratic(test_set['x'], a, b, c)
    mse = np.mean((test_set['y'] - y_test_pred)**2)
    mae = np.mean(np.abs(test_set['y'] - y_test_pred))
    results.append(f"{set_name.upper()}:\n  Predictions: {y_test_pred}\n  Actual: {test_set['y']}\n  MSE: {mse:.4f}\n  MAE: {mae:.4f}\n")

# Display results in a pop-up window
test_result_text = "MODEL TEST RESULTS\n" + "=" * 40 + "\n\n" + "\n".join(results)
print(test_result_text)

plt.figure(figsize=(8, 6))
plt.text(0.1, 0.5, test_result_text, fontsize=12, family='monospace', verticalalignment='center')
plt.axis('off')
plt.title('Model Test Results')
plt.tight_layout()
plt.show()

# Interpret test results in layman's terms
interpretations = []
for set_name, test_set in test_data.items():
    y_test_pred = quadratic(test_set['x'], a, b, c)
    mse = np.mean((test_set['y'] - y_test_pred)**2)
    mae = np.mean(np.abs(test_set['y'] - y_test_pred))
    
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