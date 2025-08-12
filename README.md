Interview Trainer Agent – AI Powered by IBM Granite
Overview
This project is an AI-driven Interview Trainer Agent built with a React frontend and a Python Flask backend, using IBM Granite Foundation Models deployed on IBM Cloud Lite. By inputting a resume, job title, or job description, users receive tailored interview questions as well as actionable, AI-powered feedback on their answers. The solution aims to make interview preparation highly personalized, efficient, and adaptive—helping candidates build both technical and soft skills for today’s dynamic job market.

Features
Custom Interview Generation: Get technical and behavioral questions tailored to your profile.

AI-Powered Answer Feedback: Receive a score and improvement suggestions for every answer.

Resume Parsing: Automatic skill extraction from provided resumes.

Real-Time Evaluation: Experience realistic mock interviews instantly.

Cloud-Ready and Secure: Powered by IBM Granite and IBM Cloud Lite, with support for environment variables.

How It Works
Frontend (React): Users enter resume or job details and interact with generated interview content via a modern web UI.

Backend (Flask): Handles requests, parses text, generates questions, and evaluates answers.

IBM Granite (Cloud): Provides advanced language model capabilities for question generation and answer assessment.

Setup Instructions
Prerequisites
Python 3.8+

Node.js (for React frontend)

IBM Cloud Lite account + IBM Granite credentials

Backend Setup
Clone the repo and cd into the backend folder.

Install dependencies:

text
pip install -r requirements.txt
Configure environment:

Create a .env file in backend/:

text
IBM_API_KEY=your_ibm_api_key
IBM_PROJECT_ID=your_project_id
IBM_URL=https://us-south.ml.cloud.ibm.com
Download spaCy model:

text
python -m spacy download en_core_web_sm
Run the Flask backend:

text
python app.py
Defaults to 0.0.0.0:8080.

Frontend Setup
Navigate to frontend directory (or root if you have a single codebase).

Install dependencies:

text
npm install
Configure environment:

Create a .env file in your frontend project:

text
REACT_APP_API_URL=http://localhost:8080
Start the React app:

text
npm start
Access in browser: http://localhost:3000

File Structure
text
.
├── backend/
│   ├── app.py                # Flask API endpoints
│   ├── requirements.txt
│   ├── resume_parser.py      # spaCy skill extraction
│   ├── utils/
│   │   └── ibm_granite_api.py # IBM Granite model logic
│   ├── .env                  # Backend environment variables
│   └── ...
├── frontend/
│   ├── App.js                # React UI main logic
│   ├── App.css
│   ├── .env                  # Frontend environment variables
│   └── ...
└── README.md
Technologies Used
Frontend: React, JavaScript

Backend: Flask, Flask-CORS, spaCy

AI: IBM watsonx.ai (Granite Foundation Models)

Deployment: IBM Cloud Lite

Example Usage
User enters resume/job info.

System displays three personalized interview questions.

User answers each; system evaluates and gives feedback.

Final feedback summary provided.

Security Notes
Keep your .env files out of version control (they’re in .gitignore).

Never expose IBM API credentials publicly.

For production deployment, use a WSGI server and secure CORS policy.

Future Improvements
Integrate voice-based mock interviews and analytics dashboard.

Support localization for multiple languages.

Augment questions with company-specific databases.

License
This project is for demonstration and educational purposes. See LICENSE for details.

Credits
IBM watsonx.ai and Granite team for cutting-edge AI models.

spaCy for robust NLP.

Open source communities for foundational libraries and tools.

Feel free to fork, contribute, and adapt for your own use!
