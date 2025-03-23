// server.js
const express = require("express");
const cors = require("cors");
const userRoutes = require("./routes/userRoutes");  // Assuming you've created userRoutes.js

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Use your defined routes here
app.use("/api/users", userRoutes); // This could be for user-related routes like /users

app.get("/", (req, res) => {
    res.send("Hello from backend!");
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
