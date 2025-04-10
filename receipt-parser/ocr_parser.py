# receipt-parser/ocr_parser.py
import pytesseract
from PIL import Image
import sys
import json
import re

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def parse_receipt(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='fin')


    items = []
    total = None

    # Look for the total in specific lines
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        # If line contains 'YHTEENSA', it may contain the total amount
        if "YHTEENSA" in line.upper():
            total_match = re.search(r"[\d,\.]+", line)  # Match numbers (including commas and periods)
            if total_match:
                total = total_match.group(0)

        else:
            items.append(line)

    result = {
        "items": items,
        "total": total,
        "raw_text": text
    }

    print(json.dumps(result))  # Send to stdout

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ocr_parser.py path_to_image")
        sys.exit(1)

    parse_receipt(sys.argv[1])
