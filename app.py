import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/match-jobs"

st.title("Resume-to-Job Matcher")
st.write("Upload your resume and get matched with relevant jobs.")

resume_text = st.text_area("Paste your Resume Text here")

if st.button("Find Matching Jobs"):
    if resume_text:
        response = requests.post(API_URL, json={"resume_text": resume_text})
        matches = response.json()["matches"]
        
        st.write("### Job Matches:")
        for job, score in matches:
            st.write(f"🔹 {job} - **Similarity Score:** {score:.2f}")
    else:
        st.warning("Please enter your resume text.")
