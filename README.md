# 🎯 JobFit AI — Job Description Skill Extractor

A simple Streamlit application that extracts technical and soft skills from job descriptions and compares them against a resume.

## Features

- Extracts skills from job descriptions
- Groups skills by category
- Calculates a resume-to-job match percentage
- Shows matched skills
- Shows missing skills
- No API key required
- Runs locally

## Tech Stack

- Python
- Streamlit
- Regular Expressions
- Basic NLP / text processing

## Run Locally

### 1. Open the project in VS Code

Open this folder:

```text
job_description_skill_extractor
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

If PowerShell blocks activation, use:

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The app will open in your browser.

## Project Structure

```text
job_description_skill_extractor/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- PDF resume upload
- DOCX resume upload
- TF-IDF / NLP-based extraction
- Semantic similarity using embeddings
- AI-generated skill recommendations
- Job recommendations based on resume skills
- ATS score calculation

## Portfolio Description

**JobFit AI — Job Description Skill Extractor**

Developed a Streamlit-based tool that extracts technical and soft skills from job descriptions and evaluates resume compatibility using automated text processing. Implemented categorized skill detection and a resume-to-job match score to identify strengths and skill gaps.

## License

For educational and portfolio use.
