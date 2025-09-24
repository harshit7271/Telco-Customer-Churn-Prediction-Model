import streamlit as st
import pandas as pd
import pickle

# Load model and encoders
with open('customer_churn_model.pkl', 'rb') as f:
    model = pickle.load(f)
    if isinstance(model, dict) and "model" in model:
        model = model["model"]

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

# CSS
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }
        .main { background-color: #ffffff; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; font-size: 2.5rem; text-align: center; }
        .stButton>button { background-color: #2ecc71; color: white; font-weight: bold; border-radius: 8px; padding: 0.5rem 1rem; }
        .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label { font-weight: bold; color: #34495e; }
        .prediction { font-size: 1.2rem; font-weight: bold; padding: 1rem; border-radius: 8px; margin-top: 1rem; }
        .success { background-color: #dff0d8; color: #3c763d; }
        .error { background-color: #f2dede; color: #a94442; }
        .feedback { font-size: 1rem; margin-top: 1rem; color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# Sidebar: Name and Rating
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.title("👤 User Info")
user_name = st.sidebar.text_input("Your Name", "")
rating = st.sidebar.slider("Rate this app", 1, 5, 4)

if user_name:
    st.sidebar.markdown(f"**Welcome, {user_name}!** 👋")
    st.sidebar.markdown(f"Thanks for rating us **{rating}/5** ⭐")

# Main title
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("<h1>📉 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("Fill in the customer details below to get a churn prediction.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1500.0)

# Prepare input data
input_dict = {
    "gender": gender,
    "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

input_df = pd.DataFrame([input_dict])

# Apply encoders to categorical columns only
for col in encoders:
    input_df[col] = encoders[col].transform(input_df[col])

# Predict
if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.markdown(f'<div class="prediction error">⚠️ This customer is likely to churn.<br>Probability: {probability:.2f}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="prediction success">✅ This customer is likely to stay.<br>Probability: {1 - probability:.2f}</div>', unsafe_allow_html=True)

    if user_name:
        st.markdown(f'<div class="feedback">Thanks for using the app, {user_name}! Your feedback helps us improve. 🙌</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)