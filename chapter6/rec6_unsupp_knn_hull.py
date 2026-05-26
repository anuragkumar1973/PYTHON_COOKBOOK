# ============================================================================
# PROGRAM: K-Nearest Neighbors (KNN) Classification with ConvexHull Visualization
# filepath: /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/rec6_1_KNN.py
# ============================================================================
#
# PURPOSE:
#   Demonstrate K-Nearest Neighbors (KNN) classification algorithm by predicting
#   income categories (high, medium, low) for unknown zip codes based on their
#   demographic characteristics (population, low-income residents, mid-income residents).
#
# PROBLEM STATEMENT:
#   You have demographic data for 7 known zip codes with established income categories.
#   Three new unknown zip codes need to be classified into one of three income categories
#   (high, medium, or low). The challenge: How can you automatically predict which
#   category each unknown zip code belongs to based on similarity to known zip codes?
#
# SOLUTION APPROACH:
#   Use K-Nearest Neighbors (KNN) - a simple but powerful classification algorithm:
#   1. For each unknown zip code, find the 3 closest "neighbors" from known data
#   2. Look at what categories those 3 neighbors belong to
#   3. Assign the unknown zip code to the most common category among its neighbors
#   4. Visualize the results using 2D scatter plots with ConvexHull boundaries
#
# HOW IT WORKS (SIMPLE ANALOGY):
#   Imagine you move to a new neighborhood and want to know if it's wealthy, middle-class,
#   or low-income. You look at the 3 nearest neighborhoods you know well:
#   • If 2 of them are wealthy and 1 is middle-class → Your new neighborhood is wealthy
#   • The KNN algorithm does exactly this, but with demographic data!
#
# KEY FEATURES:
#   ✓ Trains KNN classifier on 7 known zip codes with income labels
#   ✓ Normalizes data using StandardScaler for fair distance calculations
#   ✓ Predicts income category for 3 test zip codes
#   ✓ Shows nearest neighbors and their distances for each prediction
#   ✓ Visualizes results in 3 different 2D plots (3 different feature combinations)
#   ✓ Draws ConvexHull boundaries showing spatial regions of each income category
#   ✓ Displays explanatory popup with interpretation
#   ✓ Handles Ctrl+C gracefully without crashing
#
# INSTALLATION:
#   Before running, install required libraries:
#
#   pip install numpy pandas scikit-learn scipy matplotlib
#
#   Verify installation:
#   python3 -c "import numpy, pandas, sklearn, scipy, matplotlib; print('✓ All libraries installed')"
#
# EXECUTION:
#   Method 1: Direct execution
#   $ python3 rec6_1_KNN.py
#
#   Method 2: From parent directory
#   $ python3 chapter6/rec6_1_KNN.py
#
#   Method 3: With activated virtual environment (recommended)
#   $ cd /Users/anuragkumar1973/Downloads/book_py_cookbk
#   $ source env/bin/activate
#   $ cd chapter6
#   $ python3 rec6_1_KNN.py
#
# EXPECTED OUTPUT:
#   • Test Sample Results (text output showing predictions and nearest neighbors)
#   • 3 visualization plots with ConvexHull boundaries
#   • Explanation popup describing the KNN clustering analysis
#   • Saved PNG file: knn_clusters_with_hull.png
#
# GRACEFUL SHUTDOWN:
#   Press Ctrl+C at any time to exit gracefully:
#   • All matplotlib windows will close properly
#   • No error messages or stack traces
#   • Program exits cleanly with status code 0
#
# VISUALIZATION EXPLAINED:
#   Plot 1 (Population vs Low Income):
#   Shows how zip codes cluster based on total population and low-income count.
#   Green boundary = High income category zone
#   Orange boundary = Medium income category zone
#   Red boundary = Low income category zone
#   Blue stars = Test samples being classified
#
#   Plot 2 (Population vs Mid Income):
#   Shows relationship between population and middle-income residents.
#   Same color coding as Plot 1.
#
#   Plot 3 (Low Income vs Mid Income):
#   Direct comparison of low and mid-income populations.
#   Best plot for understanding income distribution patterns.
#
# TECHNICAL CONCEPTS:
#   • KNN (K-Nearest Neighbors): Classification based on similarity to neighbors
#   • Normalization: Scaling features so all have equal importance
#   • Distance Metric: Euclidean distance (straight-line distance)
#   • ConvexHull: Geometric boundary enclosing a set of points
#   • Supervised Learning: Learning from labeled training data
#
# LEARNING OBJECTIVES:
#   ✓ Understand how KNN classification algorithm works
#   ✓ Learn why data normalization is important
#   ✓ Visualize multi-dimensional data in 2D projections
#   ✓ Interpret nearest neighbor results
#   ✓ Use ConvexHull for boundary visualization
#   ✓ Implement signal handling for graceful shutdown
#
# ============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler 
import random
from scipy.spatial import ConvexHull
import matplotlib.patches as patches
import signal
import sys

# ============================================================================
# SIGNAL HANDLER FOR GRACEFUL SHUTDOWN
# ============================================================================

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print("\n\n✓ Exiting gracefully... Closing plots.")
    plt.close('all')
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

# ============================================================================
# DATA PREPARATION
# ============================================================================

'''
random.seed(42)  # For reproducibility
data = {}

for i in range(1, 51):
    zip_code = f'1000{i:02d}'
    
    # Randomly divide population into 3 income categories
    low_income = random.randint(30000, 60000)
    mid_income = random.randint(30000, 60000)
    high_income = random.randint(30000, 60000)
    population = low_income + mid_income + high_income
    
    data[zip_code] = {
        'population': population,
        'low_income': low_income,
        'mid_income': mid_income,
        'high_income': high_income
    }
'''
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
    [50000, 9000, 24000],   # Sample 2  
    [25000, 40000, 30000]   # Sample 3
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
# CONVEX HULL HELPER FUNCTION
# ============================================================================

def compute_convex_hull(points):
    """Compute convex hull for a set of 2D points."""
    if len(points) < 3:
        return None
    try:
        hull = ConvexHull(points)
        return hull
    except:
        return None

def plot_convex_hull(ax, hull, color, alpha=0.2):
    """Plot convex hull boundary on the axis."""
    if hull is not None:
        # Get the vertices of the hull
        vertices = hull.points[hull.vertices]
        # Create polygon and add to plot
        polygon = Polygon(vertices, closed=True, 
                         edgecolor=color, facecolor=color, 
                         alpha=alpha, linewidth=2, linestyle='--')
        ax.add_patch(polygon)

# ============================================================================
# VISUALIZATION WITH CONVEX HULL BOUNDARIES
# ============================================================================

def create_knn_plots_with_hull(X_train, y_train, test_samples, show_popup=True):
    """Create KNN clustering plots with ConvexHull boundaries around income categories."""
    
    colors = {'high': 'green', 'medium': 'orange', 'low': 'red'}
    plot_configs = [
        (0, 1, 'Population', 'Low Income'),
        (0, 2, 'Population', 'Mid Income'),
        (1, 2, 'Low Income', 'Mid Income')
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    
    for plot_idx, (x_col, y_col, x_label, y_label) in enumerate(plot_configs):
        ax = axes[plot_idx]
        
        # Plot training data by category and compute convex hulls
        for category in ['high', 'medium', 'low']:
            mask = y_train == category
            # FIX: Use mask first, then select columns
            category_points = X_train[mask][:, [x_col, y_col]]
            
            # Plot scatter points
            ax.scatter(category_points[:, 0], category_points[:, 1], 
                      label=category, s=100, alpha=0.7, 
                      color=colors[category], edgecolors='black', linewidth=0.5)
            
            # Compute and plot convex hull
            hull = compute_convex_hull(category_points)
            plot_convex_hull(ax, hull, colors[category], alpha=0.15)
        
        # Transform test samples to original scale for plotting
        test_samples_orig = scaler.inverse_transform(X_test_scaled)
        
        # Plot test samples
        ax.scatter(test_samples_orig[:, x_col], test_samples_orig[:, y_col], 
                  marker='*', s=800, color='blue', label='Test samples', 
                  edgecolor='black', zorder=5, linewidth=2)
        
        # Annotate test sample values
        for i, sample in enumerate(test_samples_orig):
            ax.annotate(f'S{i+1}\n({sample[x_col]:.0f}, {sample[y_col]:.0f})',
                       xy=(sample[x_col], sample[y_col]),
                       xytext=(15, 15), textcoords='offset points',
                       bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.8),
                       fontsize=9, fontweight='bold',
                       arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        
        ax.set_xlabel(x_label, fontsize=12, fontweight='bold')
        ax.set_ylabel(y_label, fontsize=12, fontweight='bold')
        ax.set_title(f'KNN Clustering: {x_label} vs {y_label}\n(with ConvexHull Boundaries)', 
                    fontsize=13, fontweight='bold')
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3, linestyle=':')
    
    plt.tight_layout()
    
    # FIX: Save plot before showing
    try:
        plt.savefig('/Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/knn_clusters_with_hull.png', 
                    dpi=300, bbox_inches='tight')
        print("✓ Plot saved as: knn_clusters_with_hull.png")
    except Exception as e:
        print(f"Warning: Could not save plot: {e}")
    
    # FIX: Use try-except to handle Ctrl+C gracefully
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\n✓ Plot window closed by user.")
        plt.close('all')
    
    print("\n✓ Model trained and visualized successfully with ConvexHull boundaries!")
    
    if show_popup:
        try:
            show_explanation()
        except KeyboardInterrupt:
            print("\n✓ Explanation window closed by user.")
            plt.close('all')

# ============================================================================
# EXPLANATION POPUP
# ============================================================================

def show_explanation():
    """Display explanation of KNN analysis using matplotlib."""
    
    explanation_text = """EXPLANATION OF TEST RESULTS WITH CONVEX HULL BOUNDARIES
═══════════════════════════════════════════════════════════════════════════

📊 Plot 1: Population vs Low Income
This chart shows how zip codes cluster based on total population and
low-income residents. Dashed boundary lines (ConvexHull) enclose each
income category, showing their spatial distribution.

📊 Plot 2: Population vs Mid Income
This chart examines the relationship between population size and
middle-income residents. ConvexHull boundaries highlight the distinct
regions where each income category is concentrated.

📊 Plot 3: Low Income vs Mid Income
This chart focuses directly on the relationship between low and mid-income
populations. The ConvexHull polygons show how the three categories
(high, medium, low) separate in 2D income space.

🎯 ConvexHull Boundaries Explained:
• GREEN boundary: Zip codes with HIGH income potential
• ORANGE boundary: Zip codes with MEDIUM income potential
• RED boundary: Zip codes with LOW income potential
• BLUE stars: Test samples being classified

💡 How the Model Uses These Boundaries:
1. When a new test sample is plotted, the model finds the 3 nearest
   neighbors from existing zip codes
2. The category of those neighbors determines the prediction
3. ConvexHull boundaries help visualize which category each test sample
   is closest to

✓ Analysis Complete!"""
    
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.axis('off')
    ax.text(0.05, 0.95, explanation_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, pad=1))
    
    plt.tight_layout()
    
    # FIX: Handle Ctrl+C gracefully in explanation window
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\n✓ Explanation window closed by user.")
        plt.close('all')

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    try:
        create_knn_plots_with_hull(X_train, y_train, test_samples, show_popup=True)
    except KeyboardInterrupt:
        print("\n\n✓ Program interrupted by user. Exiting gracefully.")
        plt.close('all')
        sys.exit(0)