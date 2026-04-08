import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
model = pickle.load(open('trained_model.sav', 'rb'))

st.title("Rock vs Mine Prediction")
st.markdown("## 🚀 Rock vs Mine Prediction App")
st.write("A Machine Learning model that classifies sonar signals.")
st.write("Paste 60 comma-separated values OR use sample data.")

st.sidebar.title("Model Info")

st.sidebar.write("**Algorithm:** Logistic Regression")
st.sidebar.write("**Accuracy:** 85.71%")

# Sample data
sample_data = "0.0286,0.0453,0.0277,0.0174,0.0384,0.0990,0.1201,0.1833,0.2105,0.3039,0.2988,0.4250,0.6343,0.8198,1.0000,0.9988,0.9508,0.9025,0.7234,0.5122,0.2074,0.3985,0.5890,0.2872,0.2043,0.5782,0.5389,0.3750,0.3411,0.5067,0.5580,0.4778,0.3299,0.2198,0.1407,0.2856,0.3807,0.4158,0.4054,0.3296,0.2707,0.2650,0.0723,0.1238,0.1192,0.1089,0.0623,0.0494,0.0264,0.0081,0.0104,0.0045,0.0014,0.0038,0.0013,0.0089,0.0057,0.0027,0.0051,0.0062"

st.code(sample_data)

if st.button("Use Sample Data"):
    st.session_state["input"] = sample_data

input_text = st.text_area("Input here", value=st.session_state.get("input", ""))

# Prediction
if st.button("Predict"):
    try:
        input_data = list(map(float, input_text.strip().split(',')))

        if len(input_data) != 60:
            st.error(f"Expected 60 values, got {len(input_data)}")
        else:
            input_array = np.array(input_data).reshape(1, -1)
            prediction = model.predict(input_array)

            label = "Rock 🪨" if prediction[0] == 'R' else "Mine 💣"
            st.success(f"Prediction: {label}")

    except:
        st.error("Invalid format. Use comma-separated numbers.")

# ---------------- CSV SECTION ----------------

st.subheader("Upload CSV for Bulk Prediction")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        if data.shape[1] != 60:
            st.error("CSV must have exactly 60 columns.")
        else:
            predictions = model.predict(data)

            # Convert labels
            data['Prediction'] = ["Rock" if p == 'R' else "Mine" for p in predictions]

            st.write(data)

            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results", csv, "predictions.csv", "text/csv")

    except Exception as e:
        st.error("Error reading file. Make sure it's a valid CSV.")

# ---------------- SAMPLE CSV DOWNLOAD ----------------

st.subheader("Download Sample CSV")

with open("sample_data.csv", "rb") as file:
    st.download_button(
        label="Download Sample CSV",
        data=file,
        file_name="sample_data.csv",
        mime="text/csv"
    )



st.info("Upload a CSV file with 60 columns OR use the sample file provided.")