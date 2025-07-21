from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline
from utils.parser import parse_file
import os
import torch
import sys

# Load C++ tokenizer
sys.path.append("cpp_build")
import tokenizer

app = Flask(__name__, static_folder='static')

# Load summarization model (offline)
device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/tutorial')
def tutorial():
    return send_from_directory(app.static_folder, 'tutorial.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        text = request.form.get("text", "")
        if not text and "file" in request.files:
            file = request.files["file"]
            text = parse_file(file)

        if not text.strip():
            return jsonify({"error": "No valid input provided."}), 400

        # Clean & chunk using C++ tokenizer
        text = text.strip().replace('\n', ' ')
        chunks = tokenizer.fast_tokenize(text, 1024)

        summaries = []
        for chunk in chunks:
            out = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
            summaries.append(out[0]["summary_text"])

        final_summary = " ".join(summaries)
        return jsonify({"summary": final_summary})

    except Exception as e:
        return jsonify({"error": f"Summarization failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
