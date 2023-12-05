document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = '/api/stock_data?symbol=AAPL';  // You can change the symbol as needed

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process data and update the UI using a charting library (e.g., Chart.js)
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error.message);
            // Display an error message to the user in the UI
            document.getElementById('app').innerHTML = `<p>Error: ${error.message}</p>`;
        });
});
