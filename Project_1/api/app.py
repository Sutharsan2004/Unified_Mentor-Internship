from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # allows Streamlit to access this API

model = joblib.load("model.pkl")
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = [
            data["Affordability Index Scaled"],
            data["Expenditure Ratio"],
            data["Smoker Rate"],
            data["Admission Rate"],
            data["Tobacco Price Index"],
            data["Household Expenditure on Tobacco"]
        ]
        proba = model.predict_proba([features])[0][1]  # class 1 prob
        label = int(proba > 0.5)
        return jsonify({
            'mortality_risk': label,
            'probability': round(float(proba), 4)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
