import streamlit as st
import pickle
import re

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    vector = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("phishing.pkl", "rb"))
    return vector, model

vector, model = load_model()

st.title("🛡️ Phishing Website Detection System")
st.markdown("Enter any website URL below to check whether it is **safe** or a **phishing threat**.")
st.divider()

url = st.text_input("🔗 Enter Website URL", placeholder="e.g. https://example.com")

if st.button("Check URL", type="primary", use_container_width=True):
    if url.strip() == "":
        st.warning("Please enter a URL first.")
    else:
        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
        predict = model.predict(vector.transform([cleaned_url]))[0]

        if predict == "bad":
            st.error("⚠️ This is a Phishing Website! Do not enter any personal information.")
        elif predict == "good":
            st.success("✅ This is a Safe and Healthy Website.")
        else:
            st.warning("Something went wrong. Please try again.")
