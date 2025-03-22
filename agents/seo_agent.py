from core.llm import get_response

class SeoAgent:
    def optimize_content(self, content):
        """Ensure SEO best practices (keywords, readability, structure)."""
        prompt = (
            f"You are an SEO expert. Optimize the following blog content for SEO while maintaining high readability and engagement.\n"
            f"{content}\n"
            "Ensure the following:\n"
            "1. Include the primary keyword in the title, first 100 words, and at least 3 times throughout the content.\n"
            "2. Naturally integrate secondary keywords into headings and subheadings.\n"
            "3. Add an engaging meta description (max 160 characters).\n"
            "4. Optimize internal and external linking with relevant anchor text.\n"
            "5. Ensure the blog is structured for easy readability with proper formatting.\n"
            "6. Avoid keyword stuffing and maintain a natural, engaging tone."
        )
        return get_response(prompt)