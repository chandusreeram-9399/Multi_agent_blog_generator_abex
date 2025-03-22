# 🚀 AI-Powered SEO Blog Generator

A **multi-agent AI system** that generates a **high-quality, SEO-optimized** blog post (~2000 words) on a **trending HR-related topic**. Built using Python and Streamlit, this system automates research, content planning, writing, SEO optimization, and final review.

---

## 📌 Features

✅ **AI-Driven Multi-Agent System** (Research, Planning, Writing, SEO, Review)  
✅ **Fetches Trending HR Topics** from Google SERP  
✅ **SEO-Optimized & High-Quality Content** using Gemini Flash 2.0  
✅ **Multiple File Formats** (Markdown, HTML, PDF, DOCX, TXT)  
✅ **User-Friendly Web Interface** via Streamlit  

---


---

## 🧠 Agent Workflow

1️⃣ **Research Agent** 🔎 → Finds a trending HR topic  
2️⃣ **Content Planning Agent** 📋 → Creates a structured outline  
3️⃣ **Content Generation Agent** ✍️ → Writes the blog content  
4️⃣ **SEO Optimization Agent** 📈 → Enhances content for search engines  
5️⃣ **Review Agent** ✅ → Proofreads and finalizes the blog  

---
## System Workflow
![Alt Text](https://github.com/chandusreeram-9399/Multi_agent_blog_generator_abex/blob/main/Screenshot%202025-03-22%20235411.png)
---
## 🛠️ Tools & Frameworks Used

| Tool          | Purpose |
|--------------|---------|
| **Streamlit** | Web interface |
| **Google SERP API** | Fetch trending topics |
| **Gemini Flash 2.0 LLM** | AI content generation |
| **FPDF** | Generate PDF files |
| **python-docx** | Generate DOCX files |
| **Markdown** | Convert content to Markdown & HTML |
| **HTML2Text** | Convert HTML to plain text |

---

# HR Blog Generator

An AI-powered application that generates SEO-optimized HR blog content based on user queries and trending topics.

## Installation and Execution Steps

### 1. Clone the Repository
```
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment
```
python -m venv env
```

### 3. Activate Virtual Environment
```
# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate
```

### 4. Install Requirements
```
pip install -r requirements.txt
```

### 5. Set API Keys
Create a `.env` file in the project root directory and add the following:
```
GEMINI_API_KEY="your_gemini_api_key"
SERPAPI_API_KEY="you_serp-api_key"

```

### 6. Run the Application
```
streamlit run main.py
```

### 7. Follow the URL
Once the application starts, follow the displayed URL:
```
Local URL: http://localhost:8501
Network URL: http://192.168.xxx.xxx:8501
```

## Usage Instructions
1. Enter a **query** related to an HR topic
2. The system will fetch trending topics and generate an **SEO-optimized** blog
3. You can **download** the blog post in the available formats:
   - 📄 PDF
   - 📝 DOCX
   - 🌐 HTML
   - 📋 TXT
   - 📑 Markdown
4. To start a **new chat**, click the **New Chat** button and begin again

## Features
- AI-powered content generation
- Trend analysis for HR topics
- SEO optimization
- Multiple export formats
- User-friendly interface

## Requirements
- Python 3.6+
- Streamlit
- Google Gemini API access
- SerpAPI access
