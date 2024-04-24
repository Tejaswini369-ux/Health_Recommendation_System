const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Array to store (label, value) tuples
let checkboxData = [];

// Route handler to handle checkbox data
app.post('/checkbox-data', (req, res) => {
    // Extract checkbox data from request body
    const checkboxes = req.body;

    // Store (label, value) tuples in the array
    checkboxes.forEach(checkbox => {
        checkboxData.push({ label: checkbox.label, checked: true });
    });

    res.send('Checkbox data received and stored successfully.');
});

// Route handler to retrieve stored checkbox data
app.get('/checkbox-data', (req, res) => {
    // Send the stored checkbox data as JSON response
    res.json(checkboxData);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
