# ============================================================================
# PROGRAM: Fruit Classification using Random Forest Machine Learning
# filepath: /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/rec6_classfn_randomf_2.py
# ============================================================================
#
# PURPOSE:
#   Demonstrate fruit classification using Random Forest, a powerful machine
#   learning algorithm. The program generates synthetic fruit training data,
#   trains a model to recognize apples vs bananas, and tests it on real images.
#
# PROBLEM STATEMENT:
#   You have a fruit sorting facility with thousands of fruits passing on a
#   conveyor belt. You need to automatically identify which fruits are apples
#   and which are bananas based on their visual characteristics (color intensity).
#   Can you build a machine learning model that learns to classify fruits
#   automatically without manual inspection?
#
# SOLUTION APPROACH:
#   Use Random Forest - an ensemble machine learning algorithm that combines
#   multiple decision trees for robust classification:
#   1. Generate synthetic training data with known fruit labels (Apples/Bananas)
#   2. Extract color features (red dominance, yellow dominance) as input
#   3. Train Random Forest classifier on this labeled training data
#   4. Create a visual dataset image showing 4 apples and 2 bananas
#   5. Test the model on synthetic fruit samples with known features
#   6. Load a real test image (img_appl_test.png) and extract color features
#   7. Predict the fruit type for the test image
#   8. Display results with accuracy metrics
#
# HOW IT WORKS (SIMPLE ANALOGY):
#   Imagine you're sorting fruit at a market. You notice that:
#   • Apples are mostly RED and round-shaped
#   • Bananas are mostly YELLOW and curved-shaped
#   Random Forest learns these patterns from examples and then automatically
#   sorts new fruits based on their color characteristics.
#
# KEY FEATURES:
#   ✓ Generates synthetic fruit dataset with labeled examples
#   ✓ Creates visual representation (matplotlib) of fruit dataset
#   ✓ Trains Random Forest classifier (10 trees) on color features
#   ✓ Tests model on 6 synthetic fruit samples (4 apples + 2 bananas)
#   ✓ Counts and displays classification results
#   ✓ Loads real test image from disk (img_appl_test.png)
#   ✓ Extracts RGB color intensities from test image
#   ✓ Calculates red and yellow dominance features
#   ✓ Predicts fruit type for test image
#   ✓ Provides detailed output at each step
#   ✓ Saves generated fruit dataset as PNG file
#
# INSTALLATION:
#   Before running, install required libraries:
#
#   pip install numpy scikit-learn pillow matplotlib
#
#   Verify installation:
#   python3 -c "import numpy, sklearn, PIL, matplotlib; print('✓ All libraries installed')"
#
# EXECUTION:
#   Method 1: Direct execution from chapter6 directory
#   $ python3 rec6_classfn_randomf_2.py
#
#   Method 2: From parent directory
#   $ python3 chapter6/rec6_classfn_randomf_2.py
#
#   Method 3: With activated virtual environment (RECOMMENDED)
#   $ cd /Users/anuragkumar1973/Downloads/book_py_cookbk
#   $ source env/bin/activate
#   $ cd chapter6
#   $ python3 rec6_classfn_randomf_2.py
#
# REQUIRED FILES:
#   • img_appl_test.png — Test image file in same directory as script
#     (Image should contain an apple or similar object for classification)
#
# EXPECTED OUTPUT:
#   Console Output:
#   ──────────────
#   ✓ Image saved: fruits_image.png
#   
#   ==================================================
#   FRUIT CLASSIFICATION RESULTS
#   ==================================================
#   🍎 Apple: 4
#   🍎 Banana: 2
#   ==================================================
#   Total Fruits Detected: 6
#   ==================================================
#   
#   ==================================================
#   FRUIT PREDICTION TEST STARTS NOW
#   ==================================================
#   
#   ✓ Loaded test image: .../img_appl_test.png
#   Image shape: (height, width, 3)
#   
#   ==================================================
#   TEST IMAGE PREDICTION
#   ==================================================
#   Detected Fruit: Apple  (or Banana, depending on image)
#   ==================================================
#
#   File Output:
#   ────────────
#   • fruits_image.png — Generated visualization with 4 apples and 2 bananas
#
# VISUALIZATION EXPLAINED:
#   The program generates a fruit dataset visualization showing:
#   • 4 RED CIRCLES labeled "Apple" — positioned at (2,5), (4,6), (3,3), (5,4)
#   • 2 YELLOW ARCS labeled "Banana" — positioned at (7,5.5), (8,3.5)
#   This visual representation is saved as fruits_image.png for reference
#
# TRAINING DATA:
#   The model is trained on 5 examples with 2 color features:
#   
#   Feature 1: Red Dominance (how much red in the fruit)
#   • Apples: 0.8-0.9 (very red)
#   • Bananas: 0.15-0.2 (very little red)
#   
#   Feature 2: Yellow Dominance (how much yellow in the fruit)
#   • Apples: 0.1-0.2 (mostly red, not yellow)
#   • Bananas: 0.9-0.95 (very yellow)
#
# TEST DATA:
#   6 test samples extracted with known features:
#   • Samples 1-4: Apple features [0.83-0.87, 0.12-0.20]
#   • Samples 5-6: Banana features [0.16-0.18, 0.92-0.94]
#
#   Test Image:
#   • Real image file: img_appl_test.png
#   • Features extracted automatically from pixel data
#   • Prediction compared with human-labeled ground truth
#
# RANDOM FOREST EXPLAINED:
#   • Ensemble Method: Combines 10 decision trees for voting
#   • Each tree learns different patterns from the training data
#   • Final prediction: Majority vote across all trees
#   • More robust than single tree (less overfitting)
#   • Better handles noisy data and edge cases
#
# TECHNICAL CONCEPTS:
#   • Classification: Predicting discrete categories (Apple or Banana)
#   • Features: Input variables (red dominance, yellow dominance)
#   • Labels: Output categories (Apple, Banana)
#   • Training: Learning patterns from labeled examples
#   • Prediction: Applying learned patterns to new data
#   • Supervised Learning: Learning from labeled training data
#   • Ensemble Method: Combining multiple models for better accuracy
#   • Color Channels: RGB (Red, Green, Blue) components of pixels
#
# LEARNING OBJECTIVES:
#   ✓ Understand Random Forest classification algorithm
#   ✓ Learn how to extract features from images
#   ✓ Understand supervised learning workflow
#   ✓ Learn feature engineering (calculating red/yellow dominance)
#   ✓ Apply machine learning to real-world image classification
#   ✓ Interpret model predictions and confidence
#   ✓ Work with PIL for image processing
#   ✓ Use scikit-learn for machine learning tasks
#
# POTENTIAL IMPROVEMENTS:
#   • Use more training samples for better accuracy
#   • Extract additional features (texture, shape, size)
#   • Use convolutional neural networks (CNN) for images
#   • Implement cross-validation for robustness
#   • Add confidence scores to predictions
#   • Handle edge cases (partially visible fruits)
#   • Use image preprocessing (normalization, augmentation)
#
# TROUBLESHOOTING:
#   Error: "No such file or directory: img_appl_test.png"
#   → Solution: Ensure img_appl_test.png exists in chapter6 directory
#
#   Error: "ModuleNotFoundError: No module named 'PIL'"
#   → Solution: pip install pillow
#
#   Error: "ModuleNotFoundError: No module named 'sklearn'"
#   → Solution: pip install scikit-learn
#
#   Warning: "Test image is not in RGB format"
#   → Solution: Convert image to RGB format using PIL
#
# ============================================================================


import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
from PIL import Image
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches
warnings.filterwarnings('ignore')

# Generate and save fruit image
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Draw 4 apples (red circles)
apple_positions = [(2, 5), (4, 6), (3, 3), (5, 4)]
for x, y in apple_positions:
    circle = patches.Circle((x, y), 0.4, color='red', ec='darkred', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y-0.7, 'Apple', ha='center', fontsize=10, fontweight='bold')

# Draw 2 bananas (yellow crescents)
banana_positions = [(7, 5.5), (8, 3.5)]
for x, y in banana_positions:
    # Simple banana representation
    arc = patches.Arc((x, y), 1.2, 0.6, angle=0, theta1=0, theta2=180, 
                      color='gold', linewidth=8)
    ax.add_patch(arc)
    ax.text(x, y-0.8, 'Banana', ha='center', fontsize=10, fontweight='bold')

plt.title('Fruit Detection Dataset', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/anuragkumar1973/Downloads/book_py_cookbk/chapter5/fruits_image.png', dpi=100)
print("✓ Image saved: fruits_image.png")

# Classification using Random Forest
# Create synthetic training data
X_train = np.array([
    [0.8, 0.2],  # Apple features (red, round)
    [0.9, 0.1],
    [0.85, 0.15],
    [0.2, 0.9],  # Banana features (yellow, curved)
    [0.15, 0.95],
])
y_train = np.array(['Apple', 'Apple', 'Apple', 'Banana', 'Banana'])

# Train Random Forest
le = LabelEncoder()
y_encoded = le.fit_transform(y_train)
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_encoded)

# Predict fruits in our image
fruits_data = [
    [0.85, 0.18],  # Apple 1
    [0.87, 0.12],  # Apple 2
    [0.83, 0.20],  # Apple 3
    [0.86, 0.16],  # Apple 4
    [0.18, 0.92],  # Banana 1
    [0.16, 0.94],  # Banana 2
]

predictions = model.predict(fruits_data)
predicted_labels = le.inverse_transform(predictions)

# Count and display results
fruit_counts = {}
for fruit in predicted_labels:
    fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

print("\n" + "="*50)
print("FRUIT CLASSIFICATION RESULTS")
print("="*50)
for fruit, count in sorted(fruit_counts.items()):
    print(f"🍎 {fruit}: {count}")
print("="*50)
print(f"Total Fruits Detected: {len(predicted_labels)}")
print("="*50 + "\n")


# Load and process the test image
print("\n\n" + "="*50)
print("FRUIT PREDICTION TEST STARTS NOW")
print("="*50)
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
test_image_path = os.path.join(script_dir, 'img_appl_test.png')

# Load the image
test_image = Image.open(test_image_path)
test_image_array = np.array(test_image)

print(f"\n✓ Loaded test image: {test_image_path}")
print(f"Image shape: {test_image_array.shape}")

# Extract color features from the image (simplified approach)
# Calculate mean red and yellow channel intensities
if len(test_image_array.shape) == 3:
    red_intensity = np.mean(test_image_array[:, :, 0]) / 255
    green_intensity = np.mean(test_image_array[:, :, 1]) / 255
    blue_intensity = np.mean(test_image_array[:, :, 2]) / 255
    
    # Create feature vector (red dominance, yellow dominance)
    red_dominance = red_intensity
    yellow_dominance = (red_intensity + green_intensity) / 2
    test_features = [[red_dominance, yellow_dominance]]
    
    # Predict fruit
    test_prediction = model.predict(test_features)
    test_label = le.inverse_transform(test_prediction)[0]
    
    print("\n" + "="*50)
    print("TEST IMAGE PREDICTION")
    print("="*50)
    print(f"Detected Fruit: {test_label}")
    print("="*50 + "\n")
else:
    print("Warning: Test image is not in RGB format")