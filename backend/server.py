from flask import Flask, request, jsonify
from receiptparser.receipt_processor import process_receipt
from flask_cors import CORS
from receiptparser.ocr_parser import OCRParser

app = Flask(__name__)
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route("/api/process_receipt", methods=['POST'])
def process_receipt_route():
    """
    Handle the receipt image upload, process it using the receipt processor,
    and return structured data (items, total).
    """
    if 'receipt' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['receipt']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Process the receipt with the processor
    receipt_data = process_receipt(file)
    
    return jsonify(receipt_data)

if __name__ == '__main__':
    app.run(debug=True)
