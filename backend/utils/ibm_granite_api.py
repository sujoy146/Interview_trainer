import re
import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

load_dotenv()  

API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("IBM_PROJECT_ID")
URL = os.getenv("IBM_URL", "https://us-south.ml.cloud.ibm.com")
MODEL_ID = "ibm/granite-3-3-8b-instruct"

params = {
    GenTextParamsMetaNames.DECODING_METHOD: "sample",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 150,
    GenTextParamsMetaNames.TEMPERATURE: 0.7,
}

model = Model(
    model_id=MODEL_ID,
    credentials={"apikey": API_KEY, "url": URL},
    project_id=PROJECT_ID
)

def generate_questions(context):
    prompt = f"""You are an expert technical interviewer.
    Generate 3 diverse interview questions (technical + behavioral)
    for the profile: {context}
    Format:
    1. Question one
    2. Question two
    3. Question three"""
    response = model.generate_text(prompt=prompt, params=params)
    print("DEBUG: response type:", type(response))
    print("DEBUG: response:", response)

    # Defensive parsing:
    if isinstance(response, dict) and "results" in response:
        raw_output = response["results"][0].get("generated_text", "")
    elif isinstance(response, str):
        raw_output = response
    else:
        raw_output = ""
    lines = [re.sub(r'^\d+\.\s*', '', line.strip()) for line in raw_output.strip().split('\n')]
    return [line for line in lines if line]



def evaluate_answer(question, answer):
    prompt = f"""You are an AI interviewer. Evaluate this:
    Question: {question}
    Answer: {answer}
    Format:
    Score: X/10
    Feedback: [short improvement advice]"""
    response = model.generate_text(prompt=prompt, params=params)
    print("DEBUG evaluate_answer: response:", response)
    if isinstance(response, dict) and "results" in response:
        raw = response["results"][0].get("generated_text", "").strip()
    elif isinstance(response, str):
        raw = response.strip()
    else:
        raw = ""
    return raw if raw else "⚠️ No feedback generated."
