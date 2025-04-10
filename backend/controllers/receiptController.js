const { spawn } = require("child_process");
const path = require("path");

exports.parseReceipt = (req, res) => {
    const imagePath = req.body.imagePath;

    const pythonProcess = spawn("python", [
        path.join(__dirname, "../../receipt-parser/ocr_parser.py"),
        imagePath,
    ]);

    let result = "";

    pythonProcess.stdout.on("data", (data) => {
        result += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on("close", (code) => {
        if (code === 0) {
            try {
                const parsed = JSON.parse(result);
                res.json(parsed);
            } catch (err) {
                res.status(500).json({ error: "Failed to parse OCR result." });
            }
        } else {
            res.status(500).json({ error: "Python script failed." });
        }
    });
};
