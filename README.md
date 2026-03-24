# 💳 Credit Card Fraud Detection System

## 📌 Project Overview

<img width="1909" height="907" alt="Screenshot 2026-03-24 134944" src="https://github.com/user-attachments/assets/fd80cf26-4c98-4c5c-a106-be354291bb4f" />
<img width="1906" height="912" alt="Screenshot 2026-03-24 135008" src="https://github.com/user-attachments/assets/94aacc4c-5ef1-4796-a047-1d3eed404127" />
<img width="1908" height="899" alt="Screenshot 2026-03-24 142432" src="https://github.com/user-attachments/assets/a263270c-e5be-4012-b034-88c25d6095bc" />
<img width="1908" height="897" alt="Screenshot 2026-03-24 142731" src="https://github.com/user-attachments/assets/7b9e31c5-9c45-492b-91b7-5468048913ac" />

This is my final year major project where I built a **Credit Card Fraud Detection system using Machine Learning**.

Banks process millions of transactions daily, making manual fraud detection impossible. This project solves that problem by building an intelligent system that can automatically detect suspicious transactions in real time.

The model is trained on **63 lakh+ transactions** and achieves:
* **94.58% accuracy**
* **95% fraud detection (recall)**

A live web application built with Streamlit allows users to test transactions instantly.


## 🌐 Live Application

👉 https://bhagyashree-credit-card-fraud.streamlit.app


## 🎯 What This Project Does

* Takes transaction details as input
* Runs them through a trained ML model
* Predicts whether the transaction is:
  * Fraudulent ❌
  * Safe ✅
* Displays:
  * Risk score (0–100%)
  * Risk level (Low → Very High)
  * Explanation of prediction


## 📊 Dataset Information

| Detail             | Value                     |
| ------------------ | ------------------------- |
| Total Transactions | 63,62,620                 |
| Fraud Cases        | 8,213 (0.129%)            |
| Features           | 11 columns                |
| Challenge          | Highly imbalanced dataset |


## 🔍 Key Insights

* Fraud occurs only in **TRANSFER** and **CASH_OUT**
* PAYMENT and DEPOSIT had **zero fraud cases**
* Fraudsters often:
  * Drain entire account balance
  * Leave sender balance = 0
  * Use suspicious transaction patterns


## 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core programming     |
| Pandas       | Data handling        |
| NumPy        | Numerical operations |
| Scikit-learn | ML model             |
| Joblib       | Model saving         |
| Streamlit    | Web application      |


## 🤖 Model Performance

| Metric       | Result |
| ------------ | ------ |
| Accuracy     | 94.58% |
| Fraud Recall | 95%    |
| Precision    | 2%     |

📌 **Important:**
High recall is prioritized because missing fraud is more dangerous than false alerts.


## ⚙️ How It Works

1. User enters transaction details
2. Data is processed through ML pipeline
3. Model predicts fraud probability
4. App displays:
   * Risk score
   * Risk level
   * Explanation


## 🚀 How to Run Locally

```bash
git clone https://github.com/bhagyashreevishwakarma83/Fraud-Detection.git
cd Fraud-Detection
pip install -r requirements.txt
streamlit run fraud_detection.py
```


## 📁 Project Structure

```
fraud_detection.py            # Streamlit app
analysis_model.ipynb         # Model training
fraud_detection_pipeline.pkl # Trained model
requirements.txt             # Dependencies
README.md                    # Documentation
```


## 🎨 Application Features

* Dark futuristic UI
* Animated credit card scanning effect
* Real-time fraud prediction
* Risk score with progress bar
* Explanation for each prediction
* Interactive success animations


## 🔮 Future Improvements

* Apply SMOTE for better class balance
* Try Random Forest / XGBoost
* Add real-time fraud monitoring
* Build REST API for integration
* Deploy on cloud infrastructure


## 👩‍💻 Author

**Bhagyashree Vishwakarma**
BCA Final Year Student

🔗 GitHub: https://github.com/bhagyashreevishwakarma83


## 📄 License

This project is open-source under the MIT License.



⭐ If you found this project helpful, consider giving it a star!
