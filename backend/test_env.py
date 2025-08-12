from dotenv import load_dotenv
import os

load_dotenv()

print("IBM_API_KEY:", os.getenv("IBM_API_KEY"))
print("IBM_PROJECT_ID:", os.getenv("IBM_PROJECT_ID"))
print("IBM_URL:", os.getenv("IBM_URL"))
