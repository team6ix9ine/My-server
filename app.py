from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is Online!"

@app.route("/info", methods=["GET"])
def bind_info():
    access_token = request.args.get("access_token")
    if not access_token:
        return jsonify({"error": "No token provided"}), 400
    url = f"https://bind-info-nu.vercel.app/bind_info?access_token={access_token}"
    try:
        resp = requests.get(url)
        return resp.json()
    except:
        return jsonify({"error": "Failed to connect to Garena"}), 500

if __name__ == "__main__":
    app.run()
