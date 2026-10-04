from dotenv import load_dotenv
import os
load_dotenv()
print("Key loaded:", os.getenv("ANTHROPIC_API_KEY") is not None)