import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load('churn_pipeline.pkl')

# ---- Page Config ----
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("📊 Customer Churn Prediction App")
st.write("""
This app predicts whether a customer is likely to leave the company (churn) based on their profile and usage details. Fill in the form below and click the **Predict Churn** button to get the prediction.

""")

st.header("Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    gender = st.selectbox("Gender", ["Female", "Male"])
    region = st.selectbox("Region", ["East", "West", "North", "South"])
    tenure_months = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=500.0, value=70.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, max_value=20000.0, value=800.0)
    contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

with col2:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    payment_method = st.selectbox("Payment Method", 
                                    ["Electronic check", "Bank transfer", "Credit card", "Mailed check"])
    num_support_calls = st.slider("Number of Support Calls", 0, 15, 1)
    late_payments_last_year = st.slider("Late Payments (last year)", 0, 12, 0)
    avg_monthly_usage_gb = st.number_input("Avg Monthly Usage (GB)", min_value=0.0, max_value=1000.0, value=150.0)

# ---- Prediction ----
if st.button("Predict Churn"):
    try:
        input_data = pd.DataFrame([{
            'age': age,
            'gender': gender,
            'region': region,
            'tenure_months': tenure_months,
            'monthly_charges': monthly_charges,
            'total_charges': total_charges,
            'contract_type': contract_type,
            'internet_service': internet_service,
            'tech_support': tech_support,
            'online_security': online_security,
            'paperless_billing': paperless_billing,
            'payment_method': payment_method,
            'num_support_calls': num_support_calls,
            'late_payments_last_year': late_payments_last_year,
            'avg_monthly_usage_gb': avg_monthly_usage_gb
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.subheader("Prediction Result")
        if prediction == 1:
            st.error(f"⚠️ This customer is likely to CHURN: **Yes**")
        else:
            st.success(f"✅ This customer is likely to STAY: **No**")

        st.write(f"**Churn Probability:** {probability:.2%}")

    except Exception as e:
        st.error(f"Something went wrong while predicting: {e}")