import pytesseract
from PIL import Image
from io import BytesIO

# Optional: Set the path to tesseract (if it's not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Example for Windows

def process_receipt_image(image_file):
    """
    Process the receipt image to extract text using OCR.
    """
    try:
        # Convert the image file to a format that pytesseract can process
        image = Image.open(BytesIO(image_file.read()))
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(image)

        # Return the extracted text
        return text
    except Exception as e:
        return str(e)

def extract_receipt_data(text):
    """
    Extract meaningful data from the raw OCR text.
    For this basic example, we're looking for item names and totals.
    """
    # Split the text by lines
    lines = text.split("\n")
    
    # Example: Basic logic to extract receipt information
    items = []
    total = None

    for line in lines:
        line = line.strip()
        # Simple heuristic: if line contains "total" or "TOTAL", assume it's the total amount line
        if "total" in line.lower():
            try:
                total = float(line.split()[-1])  # Assuming the last word is the total amount
            except ValueError:
                pass  # If we can't convert to float, ignore this line
        elif line:  # Ignore empty lines
            items.append(line)
    
    return {"items": items, "total": total}

def process_receipt(image_file):
    """
    Process the receipt image and extract structured data (items and total).
    """
    # Step 1: Process the image to get raw text
    raw_text = process_receipt_image(image_file)

    # Step 2: Extract structured data from raw text
    receipt_data = extract_receipt_data(raw_text)

    return receipt_data

class ReceiptProcessor:
    def __init__(self, extracted_text):
        self.extracted_text = extracted_text

    def process_receipt(self):
        # Add logic to process the extracted text and return structured data
        return {
            "items": ["item1", "item2"],
            "total": "100.00"
        }
