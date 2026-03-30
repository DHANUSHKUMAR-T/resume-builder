from flask import Flask, render_template
import os

app = Flask(__name__)

# ✅ Clean template list (NO duplicates)
TEMPLATES = [ {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"}, {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"}, {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"}, {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"}, {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"}, {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"}, {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"}, {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"}, {"id": 4, "name": "Elegant Serif", "tag": "Academic", "img": "thumbnails/template4.png"}, {"id": 2, "name": "Modern Minimal", "tag": "Creative", "img": "thumbnails/template2.png"}, {"id": 3, "name": "Bold Impact", "tag": "Designer", "img": "thumbnails/template3.png"}, {"id": 1, "name": "Executive Classic", "tag": "Professional", "img": "thumbnails/template1.png"}, ]


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


# ❌ REMOVE BACKEND PDF COMPLETELY
# (Handled in frontend using html2pdf.js)


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
