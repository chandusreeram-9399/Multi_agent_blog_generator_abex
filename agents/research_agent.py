from core.web_search import search_serpapi
from core.llm import get_response

class ResearchAgent:
    def fetch_trending_topic(self, query):
        """Fetch trending HR topics using a combination of web search and LLM analysis."""
        
        # Step 1: Fetch web search results (real-time data)
        raw_search_results = search_serpapi(query)

        # Step 2: Ask LLM (Gemini) to refine the data
        prompt = (
            f"Analyze the following search results about '{query}':\n{raw_search_results}\n\n"
            "Extract the **top 5 most relevant and trending HR topics** with:\n"
            "- A brief explanation of each\n"
            "- Why it's important in 2025\n"
            "- Supporting data or real-world examples\n"
            "Ensure the output is **concise, well-structured, and insightful**."
        )
        refined_trends = get_response(prompt)

        return refined_trends
