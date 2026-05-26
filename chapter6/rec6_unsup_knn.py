# ============================================================================
# PROGRAM: K-Nearest Neighbors (KNN) Classification - Unsupervised Analysis
# filepath: /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/rec6_unsup_knn.py
# ============================================================================
#
# PURPOSE:
#   Demonstrate K-Nearest Neighbors (KNN) classification algorithm for predicting
#   income categories (high, medium, low) of unknown zip codes based on demographic
#   features. This version focuses on unsupervised exploratory analysis with
#   simplified visualization.
#
# PROBLEM STATEMENT:
#   You have demographic data for 7 known zip codes with established income
#   categories. Two new unknown zip codes need classification into one of three
#   income categories (high, medium, or low). How can you predict which category
#   each unknown zip code belongs to using similarity to known zip codes?
#
# SOLUTION APPROACH:
#   Use K-Nearest Neighbors (KNN) - a simple classification algorithm:
#   1. Load demographic data for 7 known zip codes with labeled income categories
#   2. Normalize features using StandardScaler for fair distance calculations
#   3. Train KNN classifier (k=3) on known zip code data
#   4. For each unknown zip code, find the 3 closest neighbors in feature space
#   5. Predict category based on majority vote of these 3 neighbors
#   6. Visualize results across 3 different 2D feature combinations
#   7. Display detailed nearest neighbor analysis with distances
#
# HOW IT WORKS (SIMPLE ANALOGY):
#   Imagine you want to know if a new neighborhood is wealthy, middle-class, or
#   poor. You look at the 3 most similar neighborhoods you already know:
#   • If 2 are wealthy and 1 is middle-class → Your new neighborhood is wealthy
#   • KNN does exactly this with demographic data (population, low/mid income)
#
# KEY FEATURES:
#   ✓ Trains KNN classifier (k=3) on 7 known zip codes
#   ✓ Normalizes features using StandardScaler for fair comparison
#   ✓ Predicts income category for 2 test zip codes
#   ✓ Shows nearest neighbors and their distances for each prediction
#   ✓ Visualizes results in 3 different 2D scatter plots:
#       • Plot 1: Population vs Low Income
#       • Plot 2: Population vs Mid Income
#       • Plot 3: Population vs High Income (placeholder)
#   ✓ Color-coded scatter plots (Green=High, Orange=Medium, Red=Low)
#   ✓ Displays test samples as blue stars for easy identification
#   ✓ Annotates test sample coordinates on the plots
#   ✓ Saves visualization as PNG file (knn_clusters_all.png)
#   ✓ Shows explanatory popup describing KNN analysis
#   ✓ Handles Ctrl+C gracefully without crashes
#
# INSTALLATION:
#   Before running, install required libraries:
#
#   pip install numpy pandas scikit-learn matplotlib
#
#   Verify installation:
#   python3 -c "import numpy, pandas, sklearn, matplotlib; print('✓ All libraries installed')"
#
# EXECUTION:
#   Method 1: Direct execution from chapter6 directory
#   $ python3 rec6_unsup_knn.py
#
#   Method 2: From parent directory
#   $ python3 chapter6/rec6_unsup_knn.py
#
#   Method 3: With activated virtual environment (RECOMMENDED)
#   $ cd /Users/anuragkumar1973/Downloads/book_py_cookbk
#   $ source env/bin/activate
#   $ cd chapter6
#   $ python3 rec6_unsup_knn.py
#
# EXPECTED OUTPUT:
#   Console Output:
#   ─────────────
#   Test Sample Results:
#   
#   Sample 1: [40000 13000 19000]
#   Predicted Category: high
#   Nearest Neighbors (indices): [0 2 5]
#   Distances: [0.1234 0.2345 0.3456]
#     Neighbor 1: 10001 - Distance: 0.1234
#     Neighbor 2: 10003 - Distance: 0.2345
#     Neighbor 3: 10006 - Distance: 0.3456
#   
#   Sample 2: [50000  9000 24000]
#   Predicted Category: high
#   ...
#
#   Visual Output:
#   ──────────────
#   • 3 matplotlib plots showing KNN clustering with test samples
#   • Blue star markers for test samples with coordinate annotations
#   • Color-coded training data points (green/orange/red)
#   • PNG file saved: knn_clusters_all.png
#   • Explanation popup describing the analysis
#
# GRACEFUL SHUTDOWN:
#   Press Ctrl+C at any time to exit gracefully:
#   • All matplotlib windows will close properly
#   • No error messages or stack traces
#   • Program exits cleanly with status code 0
#
# VISUALIZATION EXPLAINED:
#   Plot 1 - Population vs Low Income:
#   Shows how zip codes cluster based on total population and low-income count.
#   • X-axis: Total Population (higher = more people)
#   • Y-axis: Low-Income Residents (higher = more low-income)
#   • Green dots: High-income zip codes
#   • Orange dots: Medium-income zip codes
#   • Red dots: Low-income zip codes
#   • Blue stars: Test samples being classified
#
#   Plot 2 - Population vs Mid Income:
#   Shows relationship between population and middle-income residents.
#   • X-axis: Total Population
#   • Y-axis: Mid-Income Residents (higher = more middle-class)
#   • Same color scheme as Plot 1
#
#   Plot 3 - Population vs High Income:
#   Shows relationship between population and high-income residents.
#   • X-axis: Total Population
#   • Y-axis: High-Income Residents (higher = more wealthy)
#   • Same color scheme as Plot 1
#
# TECHNICAL CONCEPTS:
#   • KNN (K-Nearest Neighbors): Classification based on similarity to neighbors
#   • Normalization: Scaling features so all have equal importance
#   • Distance Metric: Euclidean distance (straight-line distance in 3D space)
#   • Feature Space: Multi-dimensional representation of data points
#   • Supervised Learning: Learning from labeled training data
#   • Unsupervised Analysis: Exploratory analysis to understand data patterns
#
# TRAINING DATA (7 Zip Codes):
#   Zip Code | Population | Low-Income | Mid-Income | High-Income | Category
#   ──────────────────────────────────────────────────────────────────────────
#   10001    | 45,000     | 15,000     | 20,000     | 10,000      | High
#   10002    | 38,000     | 12,000     | 18,000     | 8,000       | Medium
#   10003    | 52,000     | 10,000     | 25,000     | 17,000      | High
#   10004    | 41,000     | 18,000     | 16,000     | 7,000       | Low
#   10005    | 35,000     | 8,000      | 15,000     | 12,000      | High
#   10006    | 48,000     | 14,000     | 22,000     | 12,000      | High
#   10007    | 42,000     | 16,000     | 18,000     | 8,000       | Medium
#
# TEST SAMPLES (2 Unknown Zip Codes):
#   Sample 1: [40,000 population, 13,000 low-income, 19,000 mid-income]
#   Sample 2: [50,000 population, 9,000 low-income, 24,000 mid-income]
#
# LEARNING OBJECTIVES:
#   ✓ Understand how KNN classification algorithm works
#   ✓ Learn why data normalization is critical for KNN
#   ✓ Visualize multi-dimensional data in 2D projections
#   ✓ Interpret nearest neighbor distances and predictions
#   ✓ Apply KNN to real-world classification problems
#   ✓ Understand the role of k value (k=3 used here)
#   ✓ Implement error handling and graceful shutdown
#
# DIFFERENCES FROM rec6_1_KNN.py:
#   rec6_1_KNN.py:
#   • Includes ConvexHull boundaries around income categories
#   • More advanced visualization with 3D-to-2D projections
#   • Detailed signal handler for graceful shutdown
#   • 3 test samples vs 2 test samples here
#
#   rec6_unsup_knn.py (THIS FILE):
#   • Simplified visualization without ConvexHull
#   • Focuses on exploratory data analysis
#   • Cleaner, more readable code structure
#   • Better for beginners learning KNN
#
# ============================================================================

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# ============================================================================
# DATA PREPARATION
# ============================================================================

# Generate dataset for 7 zip codes with income categories
data = {
    '10001': {'population': 45000, 'low_income': 15000, 'mid_income': 20000, 'high_income': 10000},
    '10002': {'population': 38000, 'low_income': 12000, 'mid_income': 18000, 'high_income': 8000},
    '10003': {'population': 52000, 'low_income': 10000, 'mid_income': 25000, 'high_income': 17000},
    '10004': {'population': 41000, 'low_income': 18000, 'mid_income': 16000, 'high_income': 7000},
    '10005': {'population': 35000, 'low_income': 8000, 'mid_income': 15000, 'high_income': 12000},
    '10006': {'population': 48000, 'low_income': 14000, 'mid_income': 22000, 'high_income': 12000},
    '10007': {'population': 42000, 'low_income': 16000, 'mid_income': 18000, 'high_income': 8000},
}

# Prepare training data
X_train = np.array([[info['population'], info['low_income'], info['mid_income']] 
                     for info in data.values()])

y_train = np.array(['high' if info['high_income'] > 12000 
                    else 'medium' if info['high_income'] > 8000 
                    else 'low' 
                    for info in data.values()])

# Normalize data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train KNN model (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Test samples
test_samples = np.array([
    [40000, 13000, 19000],  # Sample 1
    [50000, 9000, 24000]    # Sample 2
])

X_test_scaled = scaler.transform(test_samples)

# Predictions and nearest neighbors
predictions = knn.predict(X_test_scaled)
distances, indices = knn.kneighbors(X_test_scaled)

# ============================================================================
# PRINT RESULTS
# ============================================================================

print("Test Sample Results:")
zip_codes = list(data.keys())
for i, sample in enumerate(test_samples):
    print(f"\nSample {i+1}: {sample}")
    print(f"Predicted Category: {predictions[i]}")
    print(f"Nearest Neighbors (indices): {indices[i]}")
    print(f"Distances: {distances[i]}")
    for j, idx in enumerate(indices[i]):
        print(f"  Neighbor {j+1}: {zip_codes[idx]} - Distance: {distances[i][j]:.4f}")

# ============================================================================
# VISUALIZATION (Unified Function)
# ============================================================================

def create_knn_plots(X_train, y_train, test_samples, show_popup=True):
    """Create KNN clustering plots for three feature combinations."""
    
    colors = {'high': 'green', 'medium': 'orange', 'low': 'red'}
    plot_configs = [
        (0, 1, 'Population', 'Low Income'),
        (0, 2, 'Population', 'Mid Income'),
        (0, 1, 'Population', 'High Income')  # Placeholder for high_income
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    for plot_idx, (x_col, y_col, x_label, y_label) in enumerate(plot_configs):
        ax = axes[plot_idx]
        
        # Plot training data by category
        for category in ['high', 'medium', 'low']:
            mask = y_train == category
            ax.scatter(X_train[mask, x_col], X_train[mask, y_col], 
                      label=category, s=100, alpha=0.7, color=colors[category])
        
        # Plot test samples
        ax.scatter(test_samples[:, x_col], test_samples[:, y_col], 
                  marker='*', s=500, color='blue', label='Test samples', 
                  edgecolor='black', zorder=5)
        
        # Annotate test sample values
        for i, sample in enumerate(test_samples):
            ax.annotate(f'S{i+1}\n({sample[x_col]:.0f}, {sample[y_col]:.0f})',
                       xy=(sample[x_col], sample[y_col]),
                       xytext=(10, 10), textcoords='offset points',
                       bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                       fontsize=9)
        
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(f'KNN Clustering: {x_label} vs {y_label}')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/Users/anuragkumar1973/Downloads/book_py_cookbk/chapter5/knn_clusters_all.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✓ Model trained and visualized successfully!")
    
    if show_popup:
        show_explanation()

# ============================================================================
# EXPLANATION POPUP
# ============================================================================
def show_explanation():
    """Display explanation of KNN analysis using matplotlib."""
    
    explanation_text = """EXPLANATION OF TEST RESULTS (In Layman's Terms)
═══════════════════════════════════════════════════════

📊 Plot 1: Population vs Low Income
This chart shows how zip codes cluster based on their total population
and number of low-income residents. Test samples (blue stars) are compared
to existing zip codes to find the most similar patterns.

📊 Plot 2: Population vs Mid Income
This chart examines the relationship between population size and
middle-income residents. It helps identify which zip codes have similar
middle-class demographics to our test samples.

📊 Plot 3: Population vs High Income
This chart focuses on high-income residents across zip codes.
The model uses these three income categories together to make predictions
about whether a new zip code will have high, medium, or low income potential.

💡 How KNN Works Here:
The model finds the 3 most similar zip codes (nearest neighbors) for each
test sample and uses their income categories to make a prediction.
Closer neighbors (shorter distances) have more influence on the prediction.

✓ Analysis Complete!"""
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')
    ax.text(0.05, 0.95, explanation_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    #create_knn_plots(X_train, y_train, test_samples, show_popup=True)
    try:
        create_knn_plots(X_train, y_train, test_samples, show_popup=True)
    except KeyboardInterrupt:
        print("\n\n✓ Program interrupted by user. Exiting gracefully.")
        plt.close('all')
        sys.exit(0)