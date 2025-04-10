Receipt OCR Processing App
This project allows users to upload receipt images, process them using Optical Character Recognition (OCR) with Tesseract, and extract structured data (items and total amounts) from the receipt. The system uses a Flask backend for processing and a React frontend for interacting with the user.

Features
OCR-based Receipt Processing: Uses Tesseract OCR to extract text from receipt images.

Backend (Flask): Handles receipt processing and communication with the frontend.

Frontend (React): Simple user interface to upload receipts and view extracted data.

Dependency Handling: Includes installation checks for Tesseract and other dependencies.

Dependencies
This project depends on several external libraries and software. Here’s a list of key dependencies:

Tesseract OCR: Optical Character Recognition library used to extract text from images.

Flask: Python web framework for the backend.

React: Frontend framework for building the user interface.

Axios: For making HTTP requests between the frontend and backend.

Tesseract Installation
For the OCR functionality to work, you need to install Tesseract OCR on your machine. Tesseract is required by the pytesseract library, which is used to interface with the OCR engine.

If Tesseract is not installed on your machine, the application will automatically attempt to install it.

Installation Guide
Step 1: Clone the Repository

git clone https://github.com/yourusername/receipt-ocr-processing.git
cd receipt-ocr-processing
Step 2: Install Backend Dependencies
Make sure Python is installed on your machine (preferably Python 3.7+). Then, install the required Python dependencies by running:


pip install -r backend/requirements.txt
Flask for backend server

pytesseract for OCR processing

Step 3: Install Frontend Dependencies
If you haven't already, make sure you have Node.js and npm installed. Then, navigate to the frontend directory and install dependencies:


cd frontend
npm install
Step 4: Run the Application
To run both the frontend and backend, you can use the provided start.bat file. This will:

Start the Flask server.

Start the React development server.

Simply double-click the start.bat file (located in the root of the repository) to begin.

Alternatively, if you prefer to start the servers manually, use the following commands:

For Flask Backend:
bash
Copy
Edit
cd backend
python server.py
This will start the Flask development server at http://127.0.0.1:5000.

For React Frontend:

cd frontend
npm start
This will start the React development server at http://localhost:3000.

Step 5: Access the App
Once both servers are running, you can access the frontend in your browser at http://localhost:3000, where you can upload receipts and view processed data.

Step 6: Test the OCR Functionality
Upload a receipt image through the React frontend.

The Flask backend will process the image using Tesseract OCR.

The extracted data will be returned to the frontend and displayed.

If Tesseract is not installed, the program will automatically attempt to install it. However, for Windows users, you will need to manually install it by downloading it from here if the automatic installation fails.

Troubleshooting
Tesseract Not Found: If the application cannot find Tesseract, you may see a message instructing you to install it. Follow the installation link provided or use the install_tesseract() function to attempt an automatic installation.

OCR Extraction Issues: If the OCR extraction is inaccurate or incomplete, ensure that your receipt image is clear and legible. Tesseract performs better with high-quality images.

CORS Issues (Frontend-Backend Communication): If you face any issues with the frontend making requests to the backend, make sure CORS is enabled in your Flask app (flask_cors package).

Contributing
Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

start.bat file content:

@echo off
echo Starting Flask server...
start python backend/server.py
timeout /t 5

echo Starting React app...
start npm start --prefix frontend
This batch file should be placed in the root directory of your project, and it will start both the Flask server and React app simultaneously.
