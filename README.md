# 🚀 Rock vs Mine Prediction App

A Machine Learning web application that classifies sonar signals as either **Rock 🪨** or **Mine 💣**.

---

## 🔗 Live Demo
👉 https://rock-vs-mine-prediction-aegnud4tnsrhbcedp3rred.streamlit.app/

---

## 📌 Project Overview

This project uses a trained Machine Learning model to predict whether an object detected by sonar is a **rock** or a **mine**.

The model is trained on the **Sonar Dataset**, where each data point consists of **60 numerical features** representing signal energy at different frequencies.

---

## 🧠 Features

- 🔹 Predict using manual input (comma-separated values)
- 🔹 Upload CSV file for batch predictions
- 🔹 Download sample CSV for testing
- 🔹 Clean and interactive UI using Streamlit
- 🔹 Real-time predictions

---

## ⚙️ Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit

---

## 📂 Project Structure
rock-vs-mine-prediction/
│
├── app.py # Streamlit app
├── trained_model.sav # Saved ML model
├── sample_data.csv # Sample input data
├── requirements.txt # Dependencies


---

## 📊 Model Details

- Algorithm: Logistic Regression
- Accuracy: 76.19%
- Problem Type: Binary Classification

---

```bash
git clone https://github.com/pranjalpandey007/rock-vs-mine-prediction.git
cd rock-vs-mine-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

📚 Key Learnings
Importance of clean and structured data
End-to-end ML workflow (training → deployment)
Handling real-world user inputs
Deploying ML apps using Streamlit Cloud

---
👤 Author

PandeyPranjal
🔗 https://github.com/pandeypranjal


---
⭐ If you like this project

Give it a star ⭐ and feel free to connect!
