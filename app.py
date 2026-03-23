from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    token = request.args.get('access_token')
    if not token:
        return jsonify({"error": "Token missing"}), 400

    # Garena New API Endpoint
    url = f"https://client.freefire.garena.com/api/v1/login?access_token={token}"
    
    try:
        response = requests.get(url, timeout=10)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": "Failed to connect to Garena", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
