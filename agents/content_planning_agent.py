from core.llm import get_response

class ContentPlanningAgent:
    """
    Role: Creates a structured blog outline.
    Goal: Ensure content follows a logical structure optimized for SEO.
    """
    def generate_outline(self, topic):
        prompt = (
            f"Create a detailed, SEO-optimized blog outline for the topic: {topic}. The outline should include: "
            "1. A compelling introduction that hooks the reader and includes the primary keyword. "
            "2. At least 5 main sections with clear headings (H2) that cover key aspects of the topic. "
            "3. Subheadings (H3) under each main section to break down the content further. "
            "4. A conclusion that summarizes the key points and includes a call-to-action. "
            "5. Suggestions for relevant keywords to include in each section for SEO optimization. "
            "Ensure the outline is well-structured, easy to follow, and aligns with SEO best practices."
        )
        return get_response(prompt)