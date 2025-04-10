const express = require("express");
const router = express.Router();
const { parseReceipt } = require("../controllers/receiptController");

router.post("/parse-receipt", parseReceipt);

module.exports = router;
