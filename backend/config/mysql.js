// config/mysql.js (for MySQL connection)
const mysql = require("mysql");

const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "your_password",
    database: "your_database",
});

connection.connect((err) => {
    if (err) throw err;
    console.log("Connected to MySQL!");
});

module.exports = connection;
