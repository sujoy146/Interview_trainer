# Interview Trainer Agent – AI Powered by IBM Granite

## Overview
An AI-driven Interview Trainer that generates personalized interview questions and provides real-time, actionable feedback on your answers. Powered by IBM Granite Foundation Models on IBM Cloud Lite, this tool helps candidates sharpen both technical and behavioral skills based on their resume or job description inputs.

---

## Features
- **Custom Interview Questions:** Tailored technical and behavioral questions generated from your resume or job title.
- **AI-Powered Feedback:** Detailed scoring and improvement suggestions on each answer.
- **Resume Parsing:** Automated skill extraction using spaCy.
- **Real-Time Mock Interviews:** Instant interaction with AI-driven interview scenarios.
- **Cloud-Ready & Secure:** Built on IBM Cloud Lite, with environment variable-based configuration for safe credential management.

---

## How It Works
- **Frontend (React):** User-friendly UI for submitting resumes/job info and answering questions.
- **Backend (Flask):** API endpoints handle text parsing, question generation, and answer evaluation.
- **IBM Granite (Cloud):** Leverages advanced AI models for natural language understanding and feedback generation.

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js (for frontend)
- IBM Cloud Lite account with Granite credentials

---

### Backend Setup
1. Clone the repo and navigate to `backend/`.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt


### Frontend Setup

1. Navigate to `frontend/`.
2. Install dependencies:

   ```bash
   npm install
   ```
3. Create a `.env` file with:

   ```
   REACT_APP_API_URL=http://localhost:8080
   ```
4. Start the React app:

   ```bash
   npm start
   ```
5. Open your browser at `http://localhost:3000`.

---

## Project Structure

```
.
├── backend/
│   ├── app.py                 # Flask API endpoints
│   ├── requirements.txt
│   ├── resume_parser.py       # spaCy-based skill extraction
│   ├── utils/
│   │   └── ibm_granite_api.py # IBM Granite API integration
│   ├── .env                   # Backend environment variables
│   └── ...
├── frontend/
│   ├── App.js                 # React main component
│   ├── App.css
│   ├── .env                   # Frontend environment variables
│   └── ...
└── README.md
```

---

## Technologies Used

* **Frontend:** React, JavaScript
* **Backend:** Flask, Flask-CORS, spaCy
* **AI:** IBM watsonx.ai Granite Foundation Models
* **Deployment:** IBM Cloud Lite

---

## Usage Flow

1. User inputs a resume or job description.
2. System extracts skills and generates tailored interview questions.
3. User answers questions through the frontend.
4. Backend evaluates answers using IBM Granite AI and returns feedback.
5. User receives a summary of performance and suggestions for improvement.

---

## Security Best Practices

* Keep `.env` files out of version control (already in `.gitignore`).
* Never expose IBM API keys publicly.
* For production, run behind a robust WSGI server and enforce strict CORS policies.

---

## Future Improvements

* Voice-based mock interview support.
* Analytics dashboard to track user progress.
* Localization for multiple languages.
* Company-specific question augmentation.

---

## License

This project is for demonstration and educational use only. See LICENSE file for details.

---

## Credits

* IBM watsonx.ai and Granite Foundation Models for AI capabilities.
* spaCy for NLP skill extraction.
* Open source community for foundational tools.

---

Fork it, improve it, and make it yours. No excuses.

```


