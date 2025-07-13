import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu
import plotly.express as px

# Load the model
model = joblib.load('churn_model.joblib')

# Load the dataset
data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Clean and preprocess data for dashboard
processed_data = data.copy()
processed_data['Churn'] = processed_data['Churn'].map({'Yes': 1, 'No': 0})

# Streamlit Page Configuration
st.set_page_config(page_title="Customer Churn Prediction", page_icon="⚡", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Dashboard", "About"],
        icons=["house", "bar-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("⚡ Customer Churn Prediction Web App")
    st.write("Welcome to the Customer Churn Prediction Tool. Please provide the customer's details below to assess their likelihood of leaving the service.")

    st.header("Please Provide Customer Details Below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.radio("Select the Customer's Gender:", ['Female', 'Male'], help="Customer's gender: Female or Male.")
        Partner = st.radio("Does the Customer Have a Partner?", ['Yes', 'No'], help="Indicates whether the customer has a spouse or partner.")
        PhoneService = st.radio("Does the Customer Use Phone Service?", ['Yes', 'No'], help="Whether the customer has a phone service.")
        InternetService = st.selectbox("Select the Internet Service Type:", ['DSL', 'Fiber optic', 'No'], help="Type of internet service: DSL, Fiber optic, or None.")
        OnlineBackup = st.radio("Does the Customer Use Online Backup Services?", ['Yes', 'No', 'No internet service'], help="Whether the customer subscribes to an online backup service.")
        TechSupport = st.radio("Does the Customer Have Tech Support?", ['Yes', 'No', 'No internet service'], help="Whether the customer has technical support services.")

    with col2:
        SeniorCitizen = st.radio("Is the Customer a Senior Citizen?", [0, 1], help="Indicates whether the customer is a senior citizen (1) or not (0).")
        Dependents = st.radio("Does the Customer Have Dependents?", ['Yes', 'No'], help="Indicates whether the customer has dependents like children.")
        MultipleLines = st.radio("Does the Customer Have Multiple Phone Lines?", ['Yes', 'No', 'No phone service'], help="Whether the customer has multiple phone lines.")
        OnlineSecurity = st.radio("Does the Customer Use Online Security Services?", ['Yes', 'No', 'No internet service'], help="Whether the customer subscribes to an online security service.")
        DeviceProtection = st.radio("Does the Customer Have Device Protection?", ['Yes', 'No', 'No internet service'], help="Whether the customer has device protection services.")
        StreamingTV = st.radio("Does the Customer Stream TV?", ['Yes', 'No', 'No internet service'], help="Whether the customer streams TV services.")

    with col3:
        tenure = st.slider("Customer's Tenure (in Months)", 0, 72, 12, help="Number of months the customer has been with the company.")
        Contract = st.selectbox("Customer's Contract Type:", ['Month-to-month', 'One year', 'Two year'], help="Customer's contract type: Monthly, yearly, or two years.")
        PaperlessBilling = st.radio("Is Paperless Billing Enabled?", ['Yes', 'No'], help="Whether the customer uses paperless billing.")
        StreamingMovies = st.radio("Does the Customer Stream Movies?", ['Yes', 'No', 'No internet service'], help="Whether the customer streams movies.")
        PaymentMethod = st.selectbox("Select the Payment Method:", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], help="Customer's payment method.")
        MonthlyCharges = st.number_input("Enter Monthly Charges ($)", min_value=0.0, value=70.0, help="The customer's current monthly bill amount.")
        TotalCharges = st.number_input("Enter Total Charges to Date ($)", min_value=0.0, value=1400.0, help="The total amount charged to the customer so far.")

    if st.button("🎯 Predict Churn"):
        input_data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [SeniorCitizen],
            'Partner': [Partner],
            'Dependents': [Dependents],
            'tenure': [tenure],
            'PhoneService': [PhoneService],
            'MultipleLines': [MultipleLines],
            'InternetService': [InternetService],
            'OnlineSecurity': [OnlineSecurity],
            'OnlineBackup': [OnlineBackup],
            'DeviceProtection': [DeviceProtection],
            'TechSupport': [TechSupport],
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies],
            'Contract': [Contract],
            'PaperlessBilling': [PaperlessBilling],
            'PaymentMethod': [PaymentMethod],
            'MonthlyCharges': [MonthlyCharges],
            'TotalCharges': [TotalCharges]
        })

        # ✅ Pass raw input directly to the model
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1] * 100

        st.markdown("---")

        if prediction[0] == 1:
            st.error(f'⚠️ The customer is likely to churn. (Confidence: {probability:.2f}%)')
        else:
            st.success(f'✅ The customer is not likely to churn. (Confidence: {100 - probability:.2f}%)')

elif selected == "Dashboard":
    st.title("📊 Customer Churn Dashboard")

    st.subheader("KPI Overview")

    col1, col2, col3 = st.columns(3)
    churn_rate = processed_data['Churn'].mean() * 100
    total_customers = len(processed_data)
    avg_tenure = processed_data['tenure'].mean()

    col1.metric("Churn Rate", f"{churn_rate:.2f}%")
    col2.metric("Total Customers", f"{total_customers}")
    col3.metric("Average Tenure", f"{avg_tenure:.1f} months")

    st.markdown("---")

    st.subheader("Explore Churn by Filters")

    gender_filter = st.selectbox("Select Gender:", ['All'] + list(processed_data['gender'].unique()))
    contract_filter = st.selectbox("Select Contract Type:", ['All'] + list(processed_data['Contract'].unique()))

    filtered_data = processed_data.copy()

    if gender_filter != 'All':
        filtered_data = filtered_data[filtered_data['gender'] == gender_filter]
    if contract_filter != 'All':
        filtered_data = filtered_data[filtered_data['Contract'] == contract_filter]

    churn_counts = filtered_data['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']

    churn_count_fig = px.bar(churn_counts,
                             x='Churn', y='Count', labels={'Churn': 'Churn', 'Count': 'Count'},
                             color='Churn', color_discrete_sequence=['#EF553B', '#00CC96'],
                             title='Churn Count Distribution')
    st.plotly_chart(churn_count_fig, use_container_width=True)

    churn_by_contract = px.pie(filtered_data, names='Contract', color='Contract',
                               title='Churn by Contract Type',
                               color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(churn_by_contract, use_container_width=True)

    tenure_fig = px.histogram(filtered_data, x='tenure', color='Churn', barmode='group',
                              title='Tenure Distribution by Churn',
                              color_discrete_sequence=['#EF553B', '#00CC96'])
    st.plotly_chart(tenure_fig, use_container_width=True)

elif selected == "About":
    st.title("ℹ️ About This App")

    st.subheader("Tech Stack")
    st.write("""
    - Python
    - Streamlit
    - Scikit-learn
    - Plotly
    - Pandas
    - Streamlit Option Menu
    """)

    st.subheader("Developer")
    st.write("Vanij Prasher")
    st.write("Email: 2004vanij.prasher@gmail.com")
    st.write("[GitHub](https://github.com/Vanij-Prasher)")
    st.write("[LinkedIn](https://www.linkedin.com/in/vanij-prasher)")