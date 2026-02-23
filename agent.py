import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyC8-ebHoP7bJ0Xjzkou33JEte05ojtx0do"))
model = genai.GenerativeModel("gemini-pro")

def generate_report(location, store_data):
    prompt = f"""
    Generate a competitor analysis report for clothing stores in {location}.
    Data: {store_data}

    Include:
    - Top competitors
    - Estimated footfall
    - Strategic recommendations
    - Best timing for promotions
    """

    response = model.generate_content(prompt)
    return response.text