from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/signal")
def signal():
    return jsonify({
        "price": 2450.12,
        "signal": "BUY",
        "confidence": 78
    })

@app.route("/")
def home():
    return "Gold Strategy API running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
