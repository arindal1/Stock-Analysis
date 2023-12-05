from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stock_data')
def get_stock_data():
    symbol = request.args.get('symbol', 'AAPL')  # Default to AAPL if symbol not provided
    api_url = f'https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?interval=1d'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.HTTPError as errh:
        return jsonify({'error': f"HTTP Error: {errh}"})
    except requests.exceptions.ConnectionError as errc:
        return jsonify({'error': f"Error Connecting: {errc}"})
    except requests.exceptions.Timeout as errt:
        return jsonify({'error': f"Timeout Error: {errt}"})
    except requests.exceptions.RequestException as err:
        return jsonify({'error': f"Something went wrong: {err}"})

if __name__ == '__main__':
    app.run(debug=True)
