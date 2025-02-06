# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Dockerized Flask!"

# if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify
import random  # A placeholder for model inference

app = Flask(__name__)

# A sample AI model prediction function (replace this with an actual AI model)
def predict(text):
    # Fake prediction logic (use an actual model here)
    sentiments = ["positive", "negative", "neutral"]
    return random.choice(sentiments)

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    prediction = predict(text)
    return jsonify({"text": text, "sentiment": prediction})

@app.route("/")
def home():
    return "AI Model API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)