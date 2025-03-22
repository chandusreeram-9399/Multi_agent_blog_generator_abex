from core.llm import get_response

class ReviewAgent:
    """
    Role: Proofreads and enhances content quality.
    Goal: Ensure grammar correctness, clarity, and engagement.
    """
    def proofread(self, content):
        prompt = (
            f"Proofread and enhance the readability of this blog:\n{content}. "
            "Ensure the content: "
            "1. Is free of grammatical, spelling, and punctuation errors. "
            "2. Has a clear and logical flow of ideas. "
            "3. Uses concise and engaging language. "
            "4. Maintains a professional tone throughout. "
            "5. Is formatted correctly with proper headings, paragraphs, and bullet points where necessary."
        )
        return get_response(prompt)