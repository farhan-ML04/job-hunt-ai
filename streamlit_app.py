import streamlit as st
from orchestrator import run_pipeline

st.title("AI Job Application Assistant")

jd = st.text_area("Paste Job Description")
resume = st.text_area("Paste Your Resume")

if st.button("Generate"):
    with st.spinner("Generating AI output..."):   # ✅ added spinner
        result = run_pipeline(jd, resume)

    if result:
        st.subheader("🔍 Job Analysis")
        st.write(result["jd_analysis"])   # ✅ changed from st.text

        st.subheader("📄 Improved Resume")
        st.write(result["resume"])        # ✅ changed from st.text

        st.subheader("✉️ Cover Letter")
        st.write(result["cover_letter"])  # ✅ changed from st.text
