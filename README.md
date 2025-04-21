
# 🏦 Loan Prediction App – Loan Sphere

Loan Sphere is an intelligent loan analysis and approval prediction platform designed to help users make informed financial decisions. This project offers real-time loan approval checks, historical mortgage analysis, and future rate forecasting.

---

## 🚀 Features

- ✅ **Loan Approval Prediction**  
  Predicts if a user's loan is likely to be approved based on their financial input and historical data.

- 📈 **Mortgage Trend Modeling**  
  Shows mortgage rate trends using historical HMDA data.

- 🔮 **Future Rate Prediction**  
  Forecasts mortgage interest rates using time series models.

- 🌐 **Modern UI + Backend API**  
  Frontend built with a responsive, user-friendly interface and connected to a Flask-based backend API.

- 📦 **Dockerized & Deployed on Google Cloud Run**  
  CI/CD integrated with Google Artifact Registry and Cloud Run for scalable deployment.

---

## 🧠 ML Model – Loan Approval

- **Model Type**: Gradient-Boosted Decision Trees (XGBoost)
- **Trained on**:  
  - 7 years (2018–2023) of **Dynamic National Loan-Level Dataset** from the [FFIEC Home Mortgage Disclosure Act](https://ffiec.cfpb.gov/data-publication/loan-level-datasets)
  - 17+ million cleaned loan entries
- **Features**:  
  Loan amount, term, income, debt-to-income ratio, occupancy type, loan purpose, and state code
- **Preprocessing**:  
  Outlier filtering, normalization, label encoding, and class imbalance handling
- **Deployment**:  
  Served via REST API with threshold-tuned binary classification

---

## 🛠️ Tech Stack

- **Frontend**: React.js + Vercel Hosting  
- **Backend**: Flask API  
- **ML/AI**: Scikit-learn, XGBoost, Pandas  
- **Deployment**: Docker, Google Cloud Run, Artifact Registry  
- **Data Source**: FFIEC HMDA Public Loan Data (2018–2023)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Arsh624/loan-prediction-app.git
cd loan-prediction-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

---

## 🐳 Docker Build (Optional)

```bash
# Build Docker image
docker build -t loan-predictor-app .

# Run locally
docker run -p 8080:8080 loan-predictor-app
```

---

## 🌍 API Endpoint

```
POST /predict
Content-Type: application/json

{
  "loan_amount": 150000,
  "loan_term": 360,
  "income": 100,
  "monthly_debt": 5,
  "occupancy_type": 1,
  "loan_purpose": 1,
  "state": "CA"
}
```

---

## 📚 Credits

Created by graduate students at the **University of Colorado Boulder** as part of the Loan Sphere initiative:
- **Archit Shukla** – Loan Approval Model, API, Deployment
- **Team** – Frontend, Historical + Time Series Modeling, UX Design

---

## 📄 License

MIT License – Free to use and modify.
