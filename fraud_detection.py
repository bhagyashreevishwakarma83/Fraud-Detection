import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.set_page_config(page_title="Fraud Detection App", page_icon="🏦")
st.title("🏦 Credit Card Fraud Detection")
st.markdown("Please enter the transaction details and use the predict button!!")
st.divider()


transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("🔍 Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    risk_score = round(probability * 100, 2)

    st.divider()
    st.subheader("🤖 AI Risk Analysis")

    st.metric(label="Fraud Risk Score", value=f"{risk_score}%")
    st.progress(probability)

    if risk_score >= 80:
        risk_level = "🔴 VERY HIGH RISK"
    elif risk_score >= 60:
        risk_level = "🟠 HIGH RISK"
    elif risk_score >= 30:
        risk_level = "🟡 MEDIUM RISK"
    else:
        risk_level = "🟢 LOW RISK"

    st.subheader(f"Risk Level: {risk_level}")

    st.divider()

    if prediction == 1:
        st.error("🚨 FRAUD ALERT!! This transaction is suspicious!!")

        st.subheader("📋 Why is this suspicious??")
        reasons = []

        if newbalanceOrig == 0 and oldbalanceOrg > 0:
            reasons.append("⚠️ Sender's entire balance was drained!!")
        if transaction_type in ["TRANSFER", "CASH_OUT"]:
            reasons.append("⚠️ High risk transaction type!!")
        if amount >= oldbalanceOrg:
            reasons.append("⚠️ Amount equals or exceeds sender's balance!!")
        if newbalanceDest == 0 and transaction_type in ["TRANSFER", "CASH_OUT"]:
            reasons.append("⚠️ Receiver's balance shows zero after transaction!!")

        if reasons:
            for reason in reasons:
                st.warning(reason)
        else:
            st.warning("⚠️ Suspicious pattern detected by ML model!!")

    else:
        st.success("✅ Transaction appears SAFE!!")
        st.balloons()

        st.subheader("📋 Why is this safe??")
        safe_reasons = []

        if transaction_type in ["PAYMENT", "DEPOSIT"]:
            safe_reasons.append("✅ Low risk transaction type!!")
        if newbalanceOrig > 0:
            safe_reasons.append("✅ Sender still has remaining balance!!")
        if newbalanceDest > 0:
            safe_reasons.append("✅ Receiver's balance increased properly!!")

        if safe_reasons:
            for reason in safe_reasons:
                st.success(reason)