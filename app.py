from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = joblib.load("model_b_binary_boosted.pkl")
scaler = joblib.load("scaler_b_binary_boosted.pkl")
# model = joblib.load(r"C:\Users\archi\OneDrive\Desktop\ML\bigdata\api\model_b_binary_boosted.pkl")
# scaler = joblib.load(r"C:\Users\archi\OneDrive\Desktop\ML\bigdata\api\scaler_b_binary_boosted.pkl")

usa_states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Dropdown mappings
occupancy_mapping = {
    "Principal Residence": 1,
    "Investment Property": 2,
    "Second Residence": 3
}

loan_purpose_mapping = {
    "Home Purchase": 1,
    "Refinancing": 2,
    "Home Improvement": 3,
    "Other": 4
}

def convert_state_abbr_to_code(state_abbr):
    try:
        return usa_states.index(state_abbr.upper())
    except ValueError:
        print("⚠️ Invalid state abbrev received — defaulting to CO")
        return 5

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        loan_amount = float(data["loan_amount"])
        loan_term_years = float(data["loan_term"])  # entered as years
        loan_term_months = loan_term_years * 12      # convert to months

        income = float(data["income"])               # monthly income
        monthly_debt = float(data["monthly_debt"])   # monthly debt
        dti = (monthly_debt / income) * 100

        # Map dropdown strings to numeric codes
        occupancy_type = occupancy_mapping.get(data["occupancy_type"], 1)
        loan_purpose = loan_purpose_mapping.get(data["loan_purpose"], 1)
        state_code = convert_state_abbr_to_code(data.get("state", "CO"))

        input_df = pd.DataFrame([{
            "loan_amount": loan_amount,
            "loan_term": loan_term_months,
            "income": income,
            "debt_to_income_ratio": dti,
            "occupancy_type": occupancy_type,
            "loan_purpose": loan_purpose,
            "state_code": state_code
        }])

        numeric_cols = ["loan_amount", "loan_term", "income", "debt_to_income_ratio"]
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

        proba = model.predict_proba(input_df)[0][1]
        prediction = 1 if proba > 0.45 else 0

        msg = (
            f"✅ Your loan for ${loan_amount:,.0f} has been Approved"
            if prediction == 1 else
            f"❌ Sorry, your loan for ${loan_amount:,.0f} has been Rejected"
        )

        return jsonify({
            "prediction": msg,
            "probability_of_approval": round(float(proba), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return "🚀 Model B API is alive and ready to approve loans!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


