from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=500,
    messages=[
        {"role": "user",
         "content": "टमाटरको बिरुवामा लाग्ने लाहीलाई जैविक तरिकाले कसरी नियन्त्रण गर्ने? छोटो उत्तर दिनुहोस्।"}
    ],
)

print(response.content[0].text)