import re
import streamlit as st

st.set_page_config(page_title="JobFit Skill Extractor", page_icon="🎯", layout="wide")

SKILLS = {
    "Programming": [
        "python", "java", "javascript", "typescript", "c", "c++", "c#", "r", "sql",
        "html", "css", "php", "scala", "kotlin", "swift"
    ],
    "Data & Analytics": [
        "pandas", "numpy", "excel", "power bi", "tableau", "matplotlib", "seaborn",
        "statistics", "data analysis", "data visualization", "power query"
    ],
    "AI & Machine Learning": [
        "machine learning", "deep learning", "artificial intelligence", "nlp",
        "natural language processing", "computer vision", "tensorflow", "pytorch",
        "scikit-learn", "keras", "xgboost", "opencv"
    ],
    "Cloud & DevOps": [
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "git",
        "github", "linux", "ci/cd", "jenkins"
    ],
    "Databases": [
        "mysql", "postgresql", "mongodb", "oracle", "sqlite", "redis", "dbms"
    ],
    "Web & Backend": [
        "react", "angular", "node.js", "nodejs", "express", "fastapi", "flask",
        "django", "rest api", "api"
    ],
    "Cybersecurity": [
        "cybersecurity", "network security", "wireshark", "burp suite", "kali linux",
        "cryptography", "penetration testing", "ethical hacking", "ssl", "tls",
        "vulnerability assessment"
    ],
    "Soft Skills": [
        "communication", "leadership", "teamwork", "problem solving", "analytical",
        "time management", "adaptability", "presentation", "collaboration",
        "critical thinking"
    ]
}

ALIASES = {
    "nodejs": "node.js",
    "scikit learn": "scikit-learn",
    "powerbi": "power bi",
    "google cloud platform": "google cloud",
    "natural language processing": "nlp",
}

def normalize(text):
    text = text.lower()
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text

def extract_skills(text):
    normalized = normalize(text)
    found = {}
    for category, skills in SKILLS.items():
        matches = []
        for skill in skills:
            pattern = r"(?<![a-z0-9+#.-])" + re.escape(skill.lower()) + r"(?![a-z0-9+#.-])"
            if re.search(pattern, normalized):
                display = ALIASES.get(skill.lower(), skill)
                if display not in matches:
                    matches.append(display)
        if matches:
            found[category] = sorted(matches)
    return found

def flatten(found):
    return {skill.lower() for skills in found.values() for skill in skills}

def make_resume_match(job_skills, resume_text):
    resume_found = extract_skills(resume_text)
    resume_skills = flatten(resume_found)
    job_flat = flatten(job_skills)
    matched = sorted(job_flat & resume_skills)
    missing = sorted(job_flat - resume_skills)
    score = round((len(matched) / len(job_flat)) * 100) if job_flat else 0
    return score, matched, missing, resume_found

st.title("🎯 JobFit AI")
st.caption("Job Description Skill Extractor & Resume Match Checker")

tab1, tab2 = st.tabs(["🔎 Extract Skills", "📄 Resume Match"])

with tab1:
    st.subheader("Paste a Job Description")
    jd = st.text_area(
        "Job description",
        height=300,
        placeholder="Paste the complete job description here..."
    )

    if st.button("Extract Skills", type="primary"):
        if not jd.strip():
            st.warning("Please paste a job description first.")
        else:
            result = extract_skills(jd)
            total = sum(len(v) for v in result.values())

            c1, c2 = st.columns(2)
            c1.metric("Skills Found", total)
            c2.metric("Categories", len(result))

            if not result:
                st.info("No predefined skills were detected. Try a longer job description.")
            else:
                for category, skills in result.items():
                    st.markdown(f"### {category}")
                    st.write(" • ".join(skills))

with tab2:
    st.subheader("Compare Your Resume With a Job Description")
    job_text = st.text_area("Job Description", height=230, key="job")
    resume_text = st.text_area("Resume Text", height=230, key="resume")

    if st.button("Calculate Match Score", type="primary"):
        if not job_text.strip() or not resume_text.strip():
            st.warning("Please provide both the job description and resume text.")
        else:
            job_found = extract_skills(job_text)
            score, matched, missing, _ = make_resume_match(job_found, resume_text)

            st.metric("Job Match Score", f"{score}%")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### ✅ Matched Skills")
                if matched:
                    for skill in matched:
                        st.success(skill)
                else:
                    st.write("No matching skills found.")

            with col2:
                st.markdown("### ❌ Missing Skills")
                if missing:
                    for skill in missing:
                        st.error(skill)
                else:
                    st.success("No missing skills from the detected skill set!")

st.divider()
st.caption("Built with Python + Streamlit • Rule-based NLP skill extraction")
