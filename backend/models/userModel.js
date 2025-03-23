// models/userModel.js
const connection = require('../config/mysql');  // or mongodb connection

const User = {
  findAll: callback => {
    connection.query('SELECT * FROM users', callback);
  },

  create: (userData, callback) => {
    connection.query('INSERT INTO users SET ?', userData, callback);
  },
};

module.exports = User;
