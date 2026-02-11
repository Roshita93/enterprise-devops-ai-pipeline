from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Home endpoint called")
    return "DevOps AI Pipeline Running"

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
