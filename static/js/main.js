// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
    // Define the API URL for fetching stock data, with a default symbol (AAPL)
    const apiUrl = '/api/stock_data?symbol=AAPL';

    // Fetch data from the API
    fetch(apiUrl)
        .then(response => {
            // Check if the response status is OK (status code 200-299)
            if (!response.ok) {
                // If not OK, throw an error with the HTTP status
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            // Parse the response as JSON and return the data
            return response.json();
        })
        .then(data => {
            // Process the retrieved data and update the UI using a charting library (e.g., Chart.js)
            console.log(data);
        })
        .catch(error => {
            // Handle errors that may occur during the fetch operation
            console.error('Error fetching data:', error.message);
            // Display an error message to the user in the UI
            document.getElementById('app').innerHTML = `<p>Error: ${error.message}</p>`;
        });
});
