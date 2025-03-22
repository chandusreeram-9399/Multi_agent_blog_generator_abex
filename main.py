import os
import streamlit as st
from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_agent import SeoAgent
from agents.review_agent import ReviewAgent
from utils.file_converter import save_content  # Utility for saving content

# Set page config
st.set_page_config(page_title="AI Chat SEO Blog Generator", page_icon="🤖", layout="wide")

# Custom UI Styles
st.markdown("""
    <style>
    .chat-bot { color: #1E90FF; font-weight: bold; font-size: 18px; }
    .chat-user { color: #4CAF50; font-weight: bold; font-size: 18px; }
    .chat-box { background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-top: 10px; }
    .highlight { font-weight: bold; color: #FF5733; }
    </style>
""", unsafe_allow_html=True)

# Sidebar - New Chat Button
if st.sidebar.button("📝 New Chat"):
    st.session_state.clear()
    st.rerun()

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "step" not in st.session_state:
    st.session_state["step"] = 0

if "name" not in st.session_state:
    st.session_state["name"] = ""

if "query" not in st.session_state:
    st.session_state["query"] = ""

if "final_content" not in st.session_state:
    st.session_state["final_content"] = ""

if "blog_generated" not in st.session_state:
    st.session_state["blog_generated"] = False

# Display Chat Title
st.markdown("<h1 class='chat-bot'>🤖 AI Chat SEO Blog Generator</h1>", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Step 1: Greeting
if st.session_state["step"] == 0:
    st.chat_message("assistant").markdown("🤖 AI: Hello! Type 'hi' to start. 😊")
    user_input = st.chat_input("👤 You:")
    if user_input and user_input.lower() == "hi":
        st.session_state.messages += [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "🤖 AI: What's your name? �"}
        ]
        st.session_state["step"] = 1
        st.rerun()

# Step 2: Get User Name
elif st.session_state["step"] == 1:
    user_input = st.chat_input("👤 You:")
    if user_input:
        st.session_state["name"] = user_input.strip()
        st.session_state.messages += [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": f"🤖 AI: Nice to meet you, {st.session_state['name']}! What HR topic are you interested in? 🔍"}
        ]
        st.session_state["step"] = 2
        st.rerun()

# Step 3: Get Blog Topic
elif st.session_state["step"] == 2:
    user_input = st.chat_input("👤 You:")
    if user_input:
        st.session_state["query"] = user_input.strip()
        st.session_state.messages += [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": f"🤖 AI: Searching for trending insights on {st.session_state['query']}... ⏳"}
        ]
        st.session_state["step"] = 3
        st.rerun()

# Step 4: Generate Blog Content
elif st.session_state["step"] == 3:
    query = st.session_state["query"]

    research_agent = ResearchAgent()
    topic = research_agent.fetch_trending_topic(query)
    st.session_state.messages.append({"role": "assistant", "content": f"✅ Topic Found!"})

    content_planner = ContentPlanningAgent()
    outline = content_planner.generate_outline(topic)
    st.session_state.messages.append({"role": "assistant", "content": "📌 Outline Created!"})

    content_generator = ContentGenerationAgent()
    content = content_generator.generate_content(outline)
    st.session_state.messages.append({"role": "assistant", "content": "✅ Blog Content Generated!"})

    seo_agent = SeoAgent()
    seo_content = seo_agent.optimize_content(content)
    st.session_state.messages.append({"role": "assistant", "content": "✅ SEO Optimization Complete!"})

    review_agent = ReviewAgent()
    final_content = review_agent.proofread(seo_content)
    st.session_state["final_content"] = final_content
    st.session_state.messages.append({"role": "assistant", "content": "✅ Final Content Ready!"})
    st.session_state["blog_generated"] = True
    st.session_state["step"] = 4
    st.rerun()

# Step 5: Show Blog and Downloads
elif st.session_state["step"] == 4:
    st.chat_message("assistant").markdown("📄 **Your SEO-Optimized Blog:**")
    st.markdown(st.session_state["final_content"], unsafe_allow_html=False)

    # 📥 **Download Section**
    st.markdown("### 📥 Download Options")
    
    file_base = f"blog_{st.session_state['name'].replace(' ', '_')}_{st.session_state['query'].replace(' ', '_')}"

    formats = {
        "PDF": "pdf",
        "DOCX": "docx",
        "HTML": "html",
        "TXT": "txt",
        "MD": "md"
    }

    col1, col2, col3, col4, col5 = st.columns(5)

    for idx, (label, ext) in enumerate(formats.items()):
        with [col1, col2, col3, col4, col5][idx]:
            if st.button(f"📂 {label}"):
                file_path = save_content(st.session_state["final_content"], ext, file_base)
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"Download {label}",
                        data=f,
                        file_name=f"{file_base}.{ext}",
                        mime={
                            "pdf": "application/pdf",
                            "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            "html": "text/html",
                            "txt": "text/plain",
                            "md": "text/markdown"
                        }[ext]
                    )