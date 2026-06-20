import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page settings
st.set_page_config(page_title="Spam Email Classifier", page_icon="📧")

# Title
st.title("📧 Spam Email Classifier")
st.write("Enter an email message and check whether it is Spam or Not Spam.")

# User input
message = st.text_area("Enter Email Message")

# Prediction
if st.button("Predict"):
    transformed_message = vectorizer.transform([message])
    prediction = model.predict(transformed_message)

    if prediction[0] == "spam":
        st.error("❌ Spam Email")
    else:
        st.success("✅ Not Spam")