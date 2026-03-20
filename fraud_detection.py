import streamlit as st
import pandas as pd
import joblib
import time
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), "fraud_detection_pipeline.pkl"))

st.set_page_config(page_title="Fraud Detection App", page_icon="🏦")

st.markdown("""
<style>

/* ===== GLOBAL DARK ===== */
.stApp {
    background: radial-gradient(circle at 20% 20%, #0a0f1c, #05070d 80%);
    color: #eaeaf0;
}

/* GRID BACKGROUND */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,255,0.05) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 0;
}

/* GLASS PANEL */
section.main > div {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 20px;
}

/* INPUT BORDER */
div[data-baseweb="input"],
div[data-baseweb="select"] {
    position: relative;
    border-radius: 12px;
}

div[data-baseweb="input"]::before,
div[data-baseweb="select"]::before {
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: 14px;
    background: linear-gradient(90deg, #00f5ff, #9d4edd, #ff4ecd, #00f5ff);
    background-size: 300%;
    animation: moveBorder 4s linear infinite;
    z-index: -1;
}

@keyframes moveBorder {
    0% { background-position: 0%; }
    100% { background-position: 300%; }
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #05070d !important;
    border-radius: 10px;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(135deg, #00f5ff, #9d4edd);
    border-radius: 14px;
    font-weight: 600;
    border: none;
    color: white;
    box-shadow: 0 0 20px rgba(0,245,255,0.5);
    width: 100%;
    padding: 14px;
    font-size: 15px;
}

div.stButton > button:hover {
    box-shadow: 0 0 30px rgba(0,245,255,0.7);
    transform: scale(1.01);
}

/* OVERLAY */
.overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.92);
    backdrop-filter: blur(8px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    flex-direction: column;
}

/* CARD */
.card {
    width: 340px;
    height: 210px;
    border-radius: 20px;
    background: linear-gradient(135deg, #141e30, #243b55);
    box-shadow: 0 0 60px rgba(0,255,255,0.4);
    position: relative;
    overflow: hidden;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.card.flip {
    animation: flipCard 1s forwards;
}

@keyframes flipCard {
    0% { transform: rotateY(0); }
    100% { transform: rotateY(180deg); }
}

.scan {
    position: absolute;
    width: 100%;
    height: 6px;
    background: linear-gradient(90deg, transparent, #00f5ff, transparent);
    box-shadow: 0 0 20px #00f5ff;
    animation: scanMove 1.5s infinite;
    top: 0;
}

@keyframes scanMove {
    0% { top: 0%; }
    100% { top: 100%; }
}

.card-text {
    position: absolute;
    bottom: 20px;
    left: 20px;
    letter-spacing: 3px;
    color: white;
    font-family: monospace;
    font-size: 15px;
}

.card-label {
    position: absolute;
    top: 20px;
    left: 20px;
    color: #00f5ff;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.card-chip {
    position: absolute;
    top: 50px;
    left: 20px;
    width: 40px;
    height: 30px;
    background: linear-gradient(135deg, #fde68a, #f59e0b);
    border-radius: 5px;
}

.loader {
    position: absolute;
    bottom: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(90deg, #00f5ff, #9d4edd, #ff4ecd);
    animation: load 1.5s linear forwards;
}

@keyframes load {
    from { width: 0%; }
    to { width: 100%; }
}

.scan-dots {
    display: flex;
    gap: 8px;
    margin-top: 1.5rem;
    justify-content: center;
}

.scandot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    animation: dotblink 1.2s infinite;
}

.scandot:nth-child(1) { background: #00f5ff; animation-delay: 0s; }
.scandot:nth-child(2) { background: #9d4edd; animation-delay: 0.2s; }
.scandot:nth-child(3) { background: #ff4ecd; animation-delay: 0.4s; }

@keyframes dotblink {
    0%,100% { opacity: 0.2; transform: scale(0.7); }
    50% { opacity: 1; transform: scale(1.3); }
}

.scan-title {
    color: #00f5ff;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 1.5rem;
    animation: fadepulse 1s infinite;
}

@keyframes fadepulse {
    0%,100% { opacity: 0.4; }
    50% { opacity: 1; }
}

/* ===== SECTION LABEL COLORS!! ===== */
.stSelectbox label {
    border-left: 3px solid #00f5ff !important;
    padding-left: 8px !important;
    color: #00f5ff !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

.stNumberInput:nth-of-type(1) label {
    border-left: 3px solid #ff4ecd !important;
    padding-left: 8px !important;
    color: #ff4ecd !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

.stNumberInput:nth-of-type(2) label,
.stNumberInput:nth-of-type(3) label {
    border-left: 3px solid #9d4edd !important;
    padding-left: 8px !important;
    color: #9d4edd !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

.stNumberInput:nth-of-type(4) label,
.stNumberInput:nth-of-type(5) label {
    border-left: 3px solid #a5f3fc !important;
    padding-left: 8px !important;
    color: #a5f3fc !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

/* ===== RESULT COLORS!! ===== */
div[data-testid="stSuccess"] {
    border-left: 3px solid #00f5ff !important;
    background: rgba(0,245,255,0.05) !important;
    border-radius: 8px !important;
}

div[data-testid="stError"] {
    border-left: 3px solid #ff4ecd !important;
    background: rgba(255,78,205,0.05) !important;
    border-radius: 8px !important;
}

div[data-testid="stWarning"] {
    border-left: 3px solid #9d4edd !important;
    background: rgba(157,78,221,0.05) !important;
    border-radius: 8px !important;
}

div[data-testid="stMetric"] {
    border: 1px solid rgba(0,245,255,0.15) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    background: rgba(0,245,255,0.03) !important;
}

div[data-testid="stMetricValue"] {
    color: #00f5ff !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("🏦 Credit Card Fraud Detection")
st.markdown("Please enter the transaction details and use the predict button!!")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

st.divider()

if st.button("🔍 Predict"):

    overlay = st.empty()

    overlay.markdown("""
    <div class="overlay">
        <div class="card">
            <div class="scan"></div>
            <div class="card-chip"></div>
            <div class="card-label">Scanning Front...</div>
            <div class="card-text">•••• •••• •••• 1234</div>
            <div class="loader"></div>
        </div>
        <div class="scan-title">Verifying transaction</div>
        <div class="scan-dots">
            <span class="scandot"></span>
            <span class="scandot"></span>
            <span class="scandot"></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.5)

    overlay.markdown("""
    <div class="overlay">
        <div class="card flip">
            <div class="scan"></div>
            <div class="card-label">Scanning CVV...</div>
            <div class="card-text">CVV •••</div>
            <div class="loader"></div>
        </div>
        <div class="scan-title">Analyzing patterns</div>
        <div class="scan-dots">
            <span class="scandot"></span>
            <span class="scandot"></span>
            <span class="scandot"></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)
    overlay.empty()

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
