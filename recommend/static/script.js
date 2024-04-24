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

        details  = JSON.stringify(checkboxData)
        const mainForm = document.getElementById('main-form')
        var json_body = document.createElement('input');
        json_body.setAttribute('name', 'json_details');
        json_body.setAttribute('type', 'json');
        json_body.setAttribute('value', details)
        json_body.hidden = true;
        mainForm.appendChild(json_body);
        document.getElementById('submit-Form').click();

        // // Send checkbox data to backend
        // fetch('', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(checkboxData)
        // })
        // .then(response => {
        //     if (!response.ok) {
        //         throw new Error('Network response was not ok');
        //     }
        //     return response.text();
        // })
        // .then(data => {
        //     console.log(data); // Log response from backend
        //     // Perform any additional actions after successful submission
        // })
        // .catch(error => {
        //     console.error('Error:', error);
        //     // Handle errors
        // });
    });
});
