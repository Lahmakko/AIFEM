from flask import Flask, request, jsonify
from .ocr_parser import OCRParser  # Use relative import
from .receipt_processor import ReceiptProcessor  # Use relative import

app = Flask(__name__)

@app.route('/process-receipt', methods=['POST'])
def process_receipt():
    file = request.files['receipt_image']  # Receipt image uploaded
    # Process the receipt image using your OCR and processing logic
    ocr_parser = OCRParser(file)
    extracted_text = ocr_parser.extract_text()
    
    processor = ReceiptProcessor(extracted_text)
    receipt = processor.process_receipt()

    # Return structured data in JSON format
    return jsonify({
        'items': receipt["items"],
        'total': receipt["total"]
    })

if __name__ == '__main__':
    app.run(debug=True)
