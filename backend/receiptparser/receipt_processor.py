import pytesseract
from PIL import Image
from io import BytesIO

# Optional: Set the path to tesseract (if it's not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Example for Windows

class ReceiptProcessor:
    def __init__(self, image_file):
        self.image_file = image_file
        self.extracted_text = ""

    def extract_text_from_image(self):
        """
        Uses OCR to extract text from the image.
        """
        try:
            image = Image.open(BytesIO(self.image_file.read()))
            self.extracted_text = pytesseract.image_to_string(image)
        except Exception as e:
            self.extracted_text = str(e)

    def extract_receipt_data(self):
        """
        Extract structured receipt data from OCR text.
        """
        lines = self.extracted_text.split("\n")
        items = []
        total = None

        for line in lines:
            line = line.strip()
            if "total" in line.lower() or "yhteensa" in line.lower():
                try:
                    amount_str = line.split()[-1].replace(",", ".")
                    total = float(amount_str)
                except ValueError:
                    continue
            elif line:
                items.append(line)

        return {"items": items, "total": total}

    def process(self):
        """
        Main method to run full pipeline.
        """
        self.extract_text_from_image()
        return self.extract_receipt_data()
