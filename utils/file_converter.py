import markdown
from fpdf import FPDF
import docx
from io import BytesIO
import os

def convert_to_pdf(content):
    """Convert markdown content to PDF"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=content)
    return pdf.output(dest='S').encode('latin-1')

def convert_to_docx(content):
    """Convert markdown content to DOCX"""
    doc = docx.Document()
    doc.add_paragraph(content)
    doc_io = BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

def convert_to_html(content):
    """Convert markdown content to HTML"""
    return markdown.markdown(content)

def convert_to_txt(content):
    """Convert markdown content to plain text"""
    return content

def save_content(content, format_type, filename):
    """Save content in specified format"""
    if format_type == 'pdf':
        pdf_content = convert_to_pdf(content)
        with open(f"{filename}.pdf", 'wb') as f:
            f.write(pdf_content)
        return f"{filename}.pdf"
    elif format_type == 'docx':
        docx_content = convert_to_docx(content)
        with open(f"{filename}.docx", 'wb') as f:
            f.write(docx_content.getvalue())
        return f"{filename}.docx"
    elif format_type == 'html':
        html_content = convert_to_html(content)
        with open(f"{filename}.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        return f"{filename}.html"
    elif format_type == 'txt':
        with open(f"{filename}.txt", 'w', encoding='utf-8') as f:
            f.write(content)
        return f"{filename}.txt"
    elif format_type == 'md':
        with open(f"{filename}.md", 'w', encoding='utf-8') as f:
            f.write(content)
        return f"{filename}.md" 