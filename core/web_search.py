import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_serpapi(query):
    params = {
        "q": query,
        "engine": "google",  # Ensure we're using the correct search engine
        "api_key": SERPAPI_API_KEY
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()  # Get the results as a dictionary

    if "organic_results" in results:
        return results["organic_results"][0]["title"]  # Extract the first result title
    else:
        return "No relevant HR topic found."
