from flask import Flask, request, jsonify
from flask_cors import CORS
from receiptparser.receipt_processor import ReceiptProcessor

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

    processor = ReceiptProcessor(file)
    receipt_data = processor.process()

    return jsonify(receipt_data)

if __name__ == '__main__':
    app.run(debug=True)
