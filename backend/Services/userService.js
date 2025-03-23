// services/userService.js
const User = require('../models/userModel');

const getUserInfo = (userId) => {
  return User.findOne(userId);  // Simulate finding user by ID
};

module.exports = { getUserInfo };
