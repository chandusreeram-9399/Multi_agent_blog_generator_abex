import os
import google.generativeai as genai  # Correct import
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Configure the API key
genai.configure(api_key=api_key)

def get_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model reference
        response = model.generate_content(prompt)

        return response.text.strip() if response.text else "No response generated."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Example usage
print(get_response("Hello, how are you?"))
