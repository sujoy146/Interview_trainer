from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("IBM_PROJECT_ID")
URL = os.getenv("IBM_URL", "https://us-south.ml.cloud.ibm.com")
MODEL_ID = "ibm/granite-3-3-8b-instruct"

if not API_KEY or not PROJECT_ID:
    raise ValueError("Missing credentials. Check your .env file.")

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

prompt = "Give 3 technical interview questions for a backend developer with Python and SQL experience."
response = model.generate_text(prompt=prompt, params=params)
print(response)
