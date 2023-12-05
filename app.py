from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os

# Create a Flask app with static file path set to '/static'
app = Flask(__name__, static_url_path='/static')

# Route to serve the favicon.ico file
@app.route('/favicon.ico')
def favicon():
    # Send the favicon.ico file from the 'static' directory
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template for the home page
    return render_template('index.html')

# API endpoint to fetch stock data
@app.route('/api/stock_data')
def get_stock_data():
    # Get the stock symbol from the query parameters, default to 'AAPL'
    symbol = request.args.get('symbol', 'AAPL')
    # Construct the Yahoo Finance API URL for the specified stock symbol and interval
    api_url = f'https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?interval=1d'

    try:
        # Make a GET request to the Yahoo Finance API
        response = requests.get(api_url)
        # Raise an exception for HTTP errors (e.g., 404)
        response.raise_for_status()
        # Parse the JSON response from the API
        data = response.json()
        # Return the stock data as JSON
        return jsonify(data)
    except requests.exceptions.HTTPError as errh:
        # Handle HTTP errors and return an error message
        return jsonify({'error': f"HTTP Error: {errh}"})
    except requests.exceptions.ConnectionError as errc:
        # Handle connection errors and return an error message
        return jsonify({'error': f"Error Connecting: {errc}"})
    except requests.exceptions.Timeout as errt:
        # Handle timeout errors and return an error message
        return jsonify({'error': f"Timeout Error: {errt}"})
    except requests.exceptions.RequestException as err:
        # Handle other request errors and return an error message
        return jsonify({'error': f"Something went wrong: {err}"})

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
