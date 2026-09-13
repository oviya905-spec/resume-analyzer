import streamlit as st
import re

st.set_page_config(page_title="Resume Analyzer - by Oviya", page_icon="📄", layout="wide")
st.title("📄 Resume Analyzer - AI Powered")
st.markdown("#### Built by Oviya | Helps you get past ATS & land jobs")
st.divider()

st.sidebar.header("🎯 Job Target")
job_role = st.sidebar.selectbox("Select Role", ["Software Engineer", "Data Scientist", "AI/ML Engineer", "Web Developer"])
custom_skills = st.sidebar.text_area("Enter Required Skills", "Python, SQL, Machine Learning, Communication")

resume_text = st.text_area("📋 Paste your Resume Text Here", height=300)

if st.button("🚀 Analyze My Resume", type="primary"):
    if not resume_text.strip():
        st.warning("Resume paste pannu da!")
    else:
        word_count = len(resume_text.lower().split())
        score = 70
        if word_count > 200: score += 10
        if word_count > 400: score += 10
        if "experience" in resume_text.lower(): score += 5
        score = min(score, 95)

        required = [s.strip().lower() for s in custom_skills.split(',')]
        found = [s for s in required if s in resume_text.lower()]
        missing = [s for s in required if s not in resume_text.lower()]

        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("📊 ATS Score", f"{score}/100")
        c2.metric("🔑 Keywords Found", f"{len(found)}/{len(required)}")
        c3.metric("📝 Words", word_count)

        c4, c5 = st.columns(2)
        with c4:
            st.subheader("✅ Found")
            for f in found: st.write(f"- {f}")
        with c5:
            st.subheader("❌ Missing - Add these!")
            for m in missing: st.write(f"- **{m}**")

st.caption("Made with ❤️ by Oviya")