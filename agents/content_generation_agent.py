from core.llm import get_response

class ContentGenerationAgent:
    """
    Role: Writes the blog based on research and outline.
    Goal: Generate well-structured, informative, and engaging content.
    """
    def generate_content(self, outline):
        prompt = (
            f"Write a well-researched, engaging, and informative  atleast 2000-word blog post using the following outline: {outline}. "
            "Ensure the content: "
            "1. Follows the structure provided in the outline. "
            "2. Includes relevant data, statistics, and examples to support key points. "
            "3. Uses a professional yet conversational tone to engage the reader. "
            "4. Integrates the suggested keywords naturally for SEO optimization. "
            "5. Includes proper headings (H2, H3) and formatting for readability. "
            "6. Ends with a strong conclusion that summarizes the main points and encourages reader interaction (e.g., comments, shares)."
        )
        return get_response(prompt)