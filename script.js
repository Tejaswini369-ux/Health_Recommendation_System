document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('symptomForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Get all checked checkboxes
        const checkboxes = form.querySelectorAll('input[type="checkbox"]:checked');
        const checkboxData = Array.from(checkboxes).map(checkbox => ({
            label: checkbox.value,
            checked: true
        }));

        // Send checkbox data to backend
        fetch('/checkbox-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(checkboxData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            console.log(data); // Log response from backend
            // Perform any additional actions after successful submission
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors
        });
    });
});
