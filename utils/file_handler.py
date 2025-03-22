def save_to_markdown(content, topic):
    filename = f"{topic.replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"✅ Blog saved as {filename}")