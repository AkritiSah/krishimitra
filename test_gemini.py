from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="टमाटरको बिरुवामा लाग्ने लाहीलाई जैविक तरिकाले कसरी नियन्त्रण गर्ने? छोटो उत्तर दिनुहोस्।",
)
print(response.text)