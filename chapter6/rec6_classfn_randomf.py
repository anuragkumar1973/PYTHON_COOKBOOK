# ============================================================================
# SETUP INSTRUCTIONS: Add Homebrew to PATH (macOS)
# ============================================================================
#
# STEP 1: Open Terminal
#   - Press Cmd + Space
#   - Type "Terminal" and press Enter
#
# STEP 2: Copy and Paste Each Command (press Enter after each)
#
#   Command 1: Add a blank line to shell profile
#   $ echo >> /Users/anuragkumar1973/.zprofile
#
#   Command 2: Add Homebrew initialization to shell profile
#   $ echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/anuragkumar1973/.zprofile
#
#   Command 3: Load the updated shell configuration
#   $ eval "$(/opt/homebrew/bin/brew shellenv zsh)"
#
# STEP 3: Verify Homebrew is in PATH
#   $ brew --version
#   (Expected output: Homebrew 4.x.x)
#
# STEP 4: Install Tesseract OCR Engine
#   $ brew install tesseract
#
# STEP 5: Verify Tesseract Installation
#   $ tesseract --version
#   (Expected output: tesseract 5.x.x)
#
# STEP 6: Install Python Dependencies
#   $ pip install pillow pytesseract opencv-python
#
# STEP 7: Verify Python Libraries
#   $ python3 -c "from PIL import Image; import pytesseract; import cv2; print('✓ All libraries installed')"
#
# STEP 8: Run This Script
#   $ python3 /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter5/rec6_classfn_randomf.py
#
# NOTE: Ensure 'fruits_image.png' exists in the same directory as this script
#
# ============================================================================

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
from PIL import Image
import pytesseract
import cv2

import matplotlib.pyplot as plt
import matplotlib.patches as patches
warnings.filterwarnings('ignore')

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

# Load and process the image
image_path = 'fruits_image.png'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply OCR to extract text
pil_image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(pil_image)

# Parse dimensions from OCR text
ocr_dimensions = []
lines = extracted_text.split('\n')
for line in lines:
    try:
        # Extract numbers that could represent dimensions
        numbers = [float(x) for x in line.replace(',', '.').split() if x.replace('.', '').isdigit()]
        if len(numbers) >= 2:
            # Normalize dimensions to 0-1 range
            normalized = [num / 100 for num in numbers[:2]]
            ocr_dimensions.append(normalized)
    except:
        continue

# Predict using extracted dimensions
if ocr_dimensions:
    ocr_predictions = model.predict(ocr_dimensions)
    ocr_labels = le.inverse_transform(ocr_predictions)
    
    ocr_counts = {}
    for fruit in ocr_labels:
        ocr_counts[fruit] = ocr_counts.get(fruit, 0) + 1
    
    print("\n" + "="*50)
    print("OCR-BASED FRUIT CLASSIFICATION RESULTS")
    print("="*50)
    for fruit, count in sorted(ocr_counts.items()):
        print(f"🍎 {fruit}: {count}")
    print("="*50)
    print(f"Total Fruits Detected from OCR: {len(ocr_labels)}")
    print("="*50 + "\n")
else:
    print("No dimensions found in image via OCR")
