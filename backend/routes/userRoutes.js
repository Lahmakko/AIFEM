// routes/userRoutes.js
const express = require("express");
const router = express.Router();

// Assuming you have a controller or a service to handle user logic
// const userController = require('../controllers/userController'); // Import the controller

// Example route to get all users
router.get("/", (req, res) => {
    res.send("Getting all users");
});

// Example route to create a new user
router.post("/", (req, res) => {
    res.send("Creating a new user");
});

module.exports = router;
