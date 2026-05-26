# ============================================================================
# PROGRAM: Optical Character Recognition (OCR) using Tesseract
# filepath: /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/rec6_cv_ocr.py
# ============================================================================
#
# PURPOSE:
#   Extract text from images using Optical Character Recognition (OCR).
#   This program reads text from image files and converts it into machine-readable
#   text format, useful for digitizing documents, receipts, forms, and more.
#
# PROBLEM STATEMENT:
#   You have image files (PNG, JPG, etc.) containing text that you need to extract
#   and convert into editable digital text. Manual transcription is time-consuming
#   and error-prone. Can you automatically read text from images?
#
# SOLUTION APPROACH:
#   Use Tesseract OCR (Optical Character Recognition) engine with Python bindings:
#   1. Install Tesseract OCR engine on your machine
#   2. Load image file using PIL (Python Imaging Library)
#   3. Preprocess image with OpenCV for better OCR accuracy
#   4. Convert RGBA to RGB/Grayscale if needed
#   5. Extract text using pytesseract
#   6. Save extracted text to a file
#   7. Display results with error handling
#
# HOW IT WORKS (SIMPLE ANALOGY):
#   Tesseract OCR is like a very smart person who can read handwriting or printed
#   text in an image and convert it to digital text. The program:
#   • Loads the image
#   • Cleans it up (preprocessing)
#   • Reads the text character by character
#   • Returns the extracted text as a string
#
# KEY FEATURES:
#   ✓ Loads image files (PNG, JPG, etc.) with error handling
#   ✓ Automatically converts RGBA to RGB format
#   ✓ Converts to grayscale for better OCR accuracy
#   ✓ Preprocesses image with OpenCV (thresholding, denoising)
#   ✓ Extracts text using Tesseract OCR engine
#   ✓ Handles missing or invalid images gracefully
#   ✓ Saves extracted text to output file (extracted_text.txt)
#   ✓ Provides detailed console output and error messages
#   ✓ Compatible with Intel and Apple Silicon Macs
#
# INSTALLATION:
#   Step 1: Install Tesseract OCR engine
#   ──────────────────────────────────────
#   On macOS using Homebrew:
#   $ brew install tesseract
#
#   On macOS Apple Silicon (M1/M2/M3):
#   $ brew install tesseract
#   (Homebrew handles Apple Silicon automatically)
#
#   On Ubuntu/Debian:
#   $ sudo apt-get install tesseract-ocr
#
#   On Windows:
#   Download from: https://github.com/UB-Mannheim/tesseract/wiki
#
#   Step 2: Install Python dependencies
#   ────────────────────────────────────
#   $ pip install pytesseract pillow opencv-python
#
#   Verify installation:
#   $ tesseract --version
#   $ python3 -c "import pytesseract, PIL, cv2; print('✓ All libraries installed')"
#
# REQUIRED FILES:
#   • IMG_4_ocr.png — Image file in the same directory as this script
#     (Can be any image format: PNG, JPG, TIFF, BMP, etc.)
#
# EXECUTION:
#   Method 1: Direct execution from chapter6 directory
#   $ python3 rec6_cv_ocr.py
#
#   Method 2: From parent directory
#   $ python3 chapter6/rec6_cv_ocr.py
#
#   Method 3: With activated virtual environment (RECOMMENDED)
#   $ cd /Users/anuragkumar1973/Downloads/book_py_cookbk
#   $ source env/bin/activate
#   $ cd chapter6
#   $ python3 rec6_cv_ocr.py
#
#   Method 4: Specify custom image file (modify code and change image_path)
#   $ python3 rec6_cv_ocr.py
#   (Edit line: image_path = 'YOUR_IMAGE.png')
#
# EXPECTED OUTPUT:
#   Console Output:
#   ──────────────
#   ✓ Image file found: IMG_4_ocr.png
#   ✓ Image loaded successfully
#     Format: PNG
#     Size: (800, 600)
#     Mode: L
#   ✓ Image preprocessed with OpenCV
#
#   🔄 Extracting text from image (this may take a moment)...
#   ✓ Text extraction successful!
#
#   ======================================================================
#   EXTRACTED TEXT FROM IMAGE
#   ======================================================================
#   The quick brown fox jumps over the lazy dog.
#   This is sample text extracted from the image.
#   ======================================================================
#
#   ✓ Results saved to: extracted_text.txt
#
#   File Output:
#   ───────────
#   • extracted_text.txt — Text file containing all extracted text
#
# IMAGE REQUIREMENTS:
#   • Supported Formats: PNG, JPG, JPEG, TIFF, BMP, GIF, WEBP
#   • Resolution: Minimum 100x100 pixels, recommended 300+ DPI
#   • Quality: Higher contrast between text and background = better results
#   • Text Color: Black or dark text on white/light background (recommended)
#   • Font: Most printed fonts supported, handwriting may have lower accuracy
#
# PREPROCESSING OPTIONS:
#   The program automatically applies:
#   1. Format Conversion: RGBA → RGB → Grayscale
#   2. Thresholding: Converts image to black and white for clarity
#   3. Denoising: Removes noise and artifacts using fastNlMeansDenoising
#   4. Result: Cleaner image = Better OCR accuracy
#
# TECHNICAL CONCEPTS:
#   • OCR (Optical Character Recognition): Reading text from images
#   • Tesseract: Open-source OCR engine by Google
#   • PIL (Python Imaging Library): Image processing library
#   • OpenCV: Computer vision library for image preprocessing
#   • Grayscale: Image with only brightness values (black/white)
#   • Thresholding: Converting image to pure black and white pixels
#   • Denoising: Removing unwanted artifacts and noise
#
# ACCURACY TIPS:
#   ✓ Use high-resolution images (300+ DPI)
#   ✓ Ensure good lighting in photos
#   ✓ Use clear, printed fonts (avoid handwriting)
#   ✓ Keep text horizontal (not rotated)
#   ✓ Maintain high contrast (dark text on light background)
#   ✓ Avoid blurry or distorted images
#   ✓ Remove watermarks or backgrounds if possible
#
# LEARNING OBJECTIVES:
#   ✓ Understand OCR (Optical Character Recognition)
#   ✓ Learn how to use Tesseract OCR engine
#   ✓ Work with image preprocessing for better accuracy
#   ✓ Handle image format conversions (RGBA, RGB, Grayscale)
#   ✓ Extract useful data from unstructured image files
#   ✓ Implement error handling for file operations
#   ✓ Use PIL and OpenCV for image processing
#   ✓ Apply computer vision techniques to solve real problems
#
# TROUBLESHOOTING:
#
#   Error: "❌ Error: Image file 'IMG_4_ocr.png' not found!"
#   Solution: Ensure IMG_4_ocr.png exists in the same directory as the script
#            Run: ls -la IMG_4_ocr.png (to verify)
#            Or change image_path variable to correct filename
#
#   Error: "❌ Error: Tesseract is not installed or not in PATH"
#   Solution: Install Tesseract: brew install tesseract
#            Verify: tesseract --version
#            On Apple Silicon: Path is /opt/homebrew/bin/tesseract
#            On Intel Mac: Path is /usr/local/bin/tesseract
#
#   Error: "ModuleNotFoundError: No module named 'pytesseract'"
#   Solution: pip install pytesseract
#
#   Error: "ModuleNotFoundError: No module named 'PIL'"
#   Solution: pip install pillow
#
#   Error: "ModuleNotFoundError: No module named 'cv2'"
#   Solution: pip install opencv-python
#
#   Warning: "⚠️  No text found in image"
#   Solution: Image may be blank, too blurry, or have no readable text
#            Try: Using a different image with clearer text
#                 Increasing image resolution
#                 Improving lighting in the image
#                 Cropping to focus on text areas only
#
#   Warning: "OpenCV preprocessing failed"
#   Solution: Program will continue with original image (less accuracy)
#            This is non-fatal and text extraction will still be attempted
#
# COMMAND REFERENCE:
#   # Check Tesseract version
#   $ tesseract --version
#
#   # Check installed languages
#   $ tesseract --list-langs
#
#   # Get help
#   $ tesseract --help-extra
#
#   # Verify Python module installation
#   $ python3 -c "import pytesseract; print(pytesseract.pytesseract.pytesseract_cmd)"
#
# ADVANCED USAGE:
#   • Extract specific language text: pytesseract.image_to_string(img, lang='fra')
#   • Get confidence scores: pytesseract.image_to_data(img)
#   • Batch process multiple images: Loop through directory and process each
#   • Extract table data: Use pytesseract with pandas for structured data
#   • Rotate images: Use OpenCV cv2.rotate() for tilted text
#
# LIMITATIONS:
#   ✗ Handwriting recognition is unreliable
#   ✗ Blurry or low-resolution images give poor results
#   ✗ Complex layouts (multi-column) may confuse the engine
#   ✗ Special characters and symbols may not be recognized
#   ✗ Performance is slow for large images (can take seconds)
#
# REAL-WORLD APPLICATIONS:
#   • Digitizing paper documents
#   • Reading text from receipts and invoices
#   • Processing forms and applications
#   • Extracting license plate text
#   • Converting scanned books to digital text
#   • Reading handwriting on checks or forms
#   • Document archival and management systems
#
# ============================================================================


import pytesseract
from PIL import Image
import cv2
import os

# ============================================================================
# FIX 1: Verify Tesseract is installed and accessible
# ============================================================================

try:
    # Check if tesseract is in PATH
    pytesseract.pytesseract.pytesseract_cmd = '/usr/local/bin/tesseract'
    # OR for Apple Silicon Macs:
    # pytesseract.pytesseract.pytesseract_cmd = '/opt/homebrew/bin/tesseract'
except Exception as e:
    print(f"Warning: Could not set tesseract path: {e}")

# ============================================================================
# FIX 2: Load and validate image
# ============================================================================

image_path = 'IMG_4_ocr.png'

# Check if file exists
if not os.path.exists(image_path):
    print(f"❌ Error: Image file '{image_path}' not found!")
    print(f"   Current directory: {os.getcwd()}")
    print(f"   Available files: {os.listdir('.')}")
    exit(1)

print(f"✓ Image file found: {image_path}")

# ============================================================================
# FIX 3: Load image with error handling
# ============================================================================

try:
    # Load with PIL and convert to RGB
    image_pil = Image.open(image_path)
    
    # Convert RGBA to RGB if needed
    if image_pil.mode == 'RGBA':
        print("Converting RGBA to RGB...")
        image_pil = image_pil.convert('RGB')
    
    # Convert to grayscale for better OCR
    image_pil = image_pil.convert('L')
    
    print(f"✓ Image loaded successfully")
    print(f"  Format: {image_pil.format}")
    print(f"  Size: {image_pil.size}")
    print(f"  Mode: {image_pil.mode}")
    
except Exception as e:
    print(f"❌ Error loading image with PIL: {e}")
    exit(1)

# ============================================================================
# FIX 4: Optional - Preprocess image with OpenCV for better OCR
# ============================================================================

try:
    # Load with OpenCV
    image_cv2 = cv2.imread(image_path)
    
    if image_cv2 is None:
        print("❌ OpenCV could not read the image")
    else:
        # Convert to grayscale
        gray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding for better OCR
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        # Apply denoising (optional)
        denoised = cv2.fastNlMeansDenoising(binary, h=10)
        
        # Convert back to PIL Image
        image_pil = Image.fromarray(denoised)
        
        print("✓ Image preprocessed with OpenCV")
        
except Exception as e:
    print(f"Warning: OpenCV preprocessing failed: {e}")
    print("  Continuing with original image...")

# ============================================================================
# FIX 5: Extract text with error handling
# ============================================================================

try:
    print("\n🔄 Extracting text from image (this may take a moment)...")
    extracted_text = pytesseract.image_to_string(image_pil)
    
    if not extracted_text.strip():
        print("⚠️  No text found in image (image may be blank or contain no readable text)")
    else:
        print("✓ Text extraction successful!")
    
except pytesseract.TesseractNotFoundError:
    print("❌ Error: Tesseract is not installed or not in PATH")
    print("   Run: brew install tesseract")
    exit(1)
    
except Exception as e:
    print(f"❌ Error extracting text: {e}")
    exit(1)

# ============================================================================
# FIX 6: Display results
# ============================================================================

print("\n" + "="*70)
print("EXTRACTED TEXT FROM IMAGE")
print("="*70)
print(extracted_text if extracted_text.strip() else "(No text detected)")
print("="*70)

# Save extracted text to file
output_file = 'extracted_text.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"\n✓ Results saved to: {output_file}")