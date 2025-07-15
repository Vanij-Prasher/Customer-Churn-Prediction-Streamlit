# ⚡ Customer Churn Prediction 

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?logo=streamlit)](https://vanij-customer-churn-prediction-app.streamlit.app/)


A modern, interactive Streamlit web application that predicts the likelihood of customer churn based on user-inputted telecom data. Powered by a trained **Random Forest Classifier**, the app also offers a dynamic **churn analytics dashboard** to visualize customer insights.

🌐 **Live App**: [[https://vanij-customer-churn-prediction-app.streamlit.app/](https://vanij-customer-churn-prediction-app.streamlit.app/](https://customer-churn-prediction-app-klzcihfkne2jpnt3ymkcw8.streamlit.app))

---

## 📌 Features

### 🔮 Churn Prediction
- Predicts whether a telecom customer is likely to churn.
- Takes user input via interactive widgets for all relevant features.
- Displays churn probability and confidence.

### 📊 Dashboard
- Interactive charts to explore churn trends:
  - Churn distribution
  - Churn by contract type
  - Tenure distribution by churn
- Filter customers by gender and contract type.

### 🔧 Model Highlights
- Trained on the [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn).
- Uses `RandomForestClassifier` with `GridSearchCV` for hyperparameter tuning.
- Full preprocessing pipeline with `StandardScaler` and `OneHotEncoder`.
- Model serialized with `joblib` and integrated into Streamlit app.

---

## 🧠 Technologies Used

- **Frontend & Deployment**:
  - [Streamlit](https://streamlit.io/)
  - Streamlit Option Menu
  - Plotly for interactive charts

- **Machine Learning**:
  - `scikit-learn` for preprocessing, modeling, and evaluation
  - `pandas`, `numpy` for data manipulation
  - `joblib` for model serialization

---

## 🚀 Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/Vanij-Prasher/Customer-Churn-Prediction-Streamlit.git
cd Customer-Churn-Prediction-Streamlit
```

2. Install the requirements

We recommend using a virtual environment:
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run app.py
```

🧪 Sample Inputs (for quick test)
# Sample Customer Feature Values (as environment variables or inline vars)
GENDER="Male"
SENIOR_CITIZEN=0
PARTNER="Yes"
DEPENDENTS="No"
TENURE=24
PHONE_SERVICE="Yes"
INTERNET_SERVICE="Fiber optic"
CONTRACT="Month-to-month"
MONTHLY_CHARGES=89.10
TOTAL_CHARGES=2256.95

📁 Project Structure
```
├── app.py                        # Streamlit frontend
├── churn_model.py               # Model training script
├── churn_model.joblib           # Trained model
├── requirements.txt             # Python dependencies
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
└── README.md                    # Project documentation
```

📈 Model Performance
	•	Accuracy: ~79%
	•	Precision (No Churn): 83%
	•	Precision (Churn): 63%
	•	Top Important Features:
	•	TotalCharges
	•	Tenure
	•	MonthlyCharges
	•	Contract Type
	•	OnlineSecurity

⸻

🙋‍♂️ Author

Vanij Prasher
📧 Email: 2004vanij.prasher@gmail.com
🔗 GitHub
🔗 LinkedIn

⸻
