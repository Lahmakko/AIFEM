// controllers/userController.js
const User = require('../models/userModel'); // Assume you have a model for interacting with your DB

exports.getAllUsers = (req, res) => {
    User.findAll()
        .then((users) => res.json(users))
        .catch((err) => res.status(500).json({ error: err.message }));
};

exports.createUser = (req, res) => {
    const { username, email, password } = req.body;
    User.create({ username, email, password })
        .then((newUser) => res.status(201).json(newUser))
        .catch((err) => res.status(500).json({ error: err.message }));
};
