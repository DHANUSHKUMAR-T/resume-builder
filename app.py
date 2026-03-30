from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
import os
import pdfkit

app = Flask(__name__)

# 🔧 IMPORTANT: Set wkhtmltopdf path (CHANGE if needed)
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

# Template metadata
TEMPLATES = [
    {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"},
    {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"},
    {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"},
    {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"},
    {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"},
    {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"},
    {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"},
    {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"},
    {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"},
    {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"},
    {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"},
    {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"},
    
]


# Home page
@app.route('/')
def index():
    return render_template('index.html', templates=TEMPLATES)


# Editor page
@app.route('/editor/<int:template_id>')
def editor(template_id):
    template_path = f"resume_templates/template{template_id}.html"

    if not os.path.exists(template_path):
        return "Template not found", 404

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    return render_template('editor.html', content=content)


# Download PDF using pdfkit
@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        html_content = data.get('html', '')

        # Full HTML wrapper (IMPORTANT)
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Generate PDF
        pdf = pdfkit.from_string(full_html, False, configuration=config)

        return send_file(
            BytesIO(pdf),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='my_resume.pdf'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run app
if __name__ == '__main__':
    app.run(debug=True)