from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import socket

app = Flask(__name__)
iris = load_iris()
model = RandomForestClassifier(random_state=42).fit(iris.data, iris.target)

@app.route("/")
def home():
    return jsonify(message="Iris ML API running", pod=socket.gethostname())

@app.route("/predict", methods=["POST"])
def predict():
    features = request.get_json()["features"]
    pred = model.predict([features])[0]
    return jsonify(prediction=iris.target_names[pred], pod=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)