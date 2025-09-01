#flask backend

from flask import Flask, render_template, request
import nltk
import re

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
keywords_file = os.path.join(BASE_DIR, "keywords.txt")


keywords = []
if os.path.exists("keywords.txt"):
    with open("keywords.txt", "r") as f:
        keywords = [line.strip() for line in f.readlines()]
else:
    print("⚠️ keywords.txt not found! Using default keywords...")
    keywords = ["Python", "Java", "SQL", "Machine Learning", "Communication"]

nltk.download("punkt")

app = Flask(__name__)

#load keywords
with open("keywords.txt" , "r") as f:
  keywords = [line.strip() for line in f.readlines()]

def highlight_keywords(text):
  """Highlight keywords in resume text"""
  highlighted = text
  for kw in keywords:
    regex = re.compile(rf"\b({kw})\b", re.IGNORECASE)
    highlighted = regex.sub(r'<span class="highlight">\1</span>', highlighted)
  return highlighted

@app.route("/", methods=["GET","POST"])
def index():
  if request.method == "POST":
    resume_text = request.form["resume"]
    highlighted_text = highlight_keywords(resume_text)
    return render_template("result.html", text=highlighted_text)
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)