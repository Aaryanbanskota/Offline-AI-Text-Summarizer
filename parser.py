from io import BytesIO
from pdfminer.high_level import extract_text
import os

def parse_file(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        text = extract_text(BytesIO(file.read()))
    elif filename.endswith('.txt'):
        text = file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file type. Only PDF and TXT are allowed.")
    return text
