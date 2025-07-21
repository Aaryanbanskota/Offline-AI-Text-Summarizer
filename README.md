# 🧠 Offline AI Text Summarizer

A fully **offline**, privacy-focused web-based application that allows users to upload or paste long blocks of text and receive high-quality summaries using local AI models.

> ✅ Built with **Python**, **JavaScript**, and **C++**  
> ✅ No internet required after setup  
> ✅ Ideal for secure environments, schools, or offline devices

---

## 📁 Project Structure

```
offline-ai-text-summarizer/
├── app.py                # Flask backend (serves model + API)
├── utils/
│   └── parser.py         # PDF/TXT file parsing logic
├── cpp/
│   └── tokenizer.cpp     # High-speed C++ chunking (via pybind11)
├── cpp_build/            # Compiled C++ shared library
├── static/
│   ├── index.html        # User interface
│   ├── tutorial.html     # (Optional) Visual help file
│   ├── styles.css        # Modern CSS styling
│   └── script.js         # Frontend JS to handle input/output
├── build_cpp.sh          # Shell script to compile C++ tokenizer
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🚀 Features

- 🔒 Fully offline (runs locally, no cloud API)
- 📄 Summarize plain text, PDFs, or pasted content
- 🧠 Fast and accurate with `distilbart-cnn-12-6` model
- 🧩 C++ chunking for speed and efficiency
- 💡 Clean and responsive UI for all screen sizes
- 👶 Beginner-friendly interface (no coding required)

---

## 🛠 Setup Instructions

> 🐍 **Python 3.8+**, 🧱 **g++**, 📦 **pip**, and 🖥️ basic terminal access required

1. **Clone or extract the project**
   ```bash
   git clone https://github.com/yourname/offline-ai-summarizer.git
   cd offline-ai-summarizer
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download summarization model (only once)**
   ```bash
   python -c "from transformers import pipeline; pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')"
   ```

4. **Build the C++ tokenizer module**
   ```bash
   chmod +x build_cpp.sh
   ./build_cpp.sh
   ```

5. **Run the Flask server**
   ```bash
   python app.py
   ```

6. **Visit the app**
   ```
   http://localhost:5000
   ```

---

## 📂 Supported Input Types

- ✅ Plain text (`.txt`)
- ✅ PDF files (`.pdf`)
- ✅ Manual paste input

---

## 🧠 Model Info

- **Model**: `sshleifer/distilbart-cnn-12-6`  
- **Framework**: HuggingFace Transformers  
- **Inference**: CPU or GPU (uses GPU if available)

---

## 🛡️ Offline & Secure

- No internet connection is required after initial model download
- Great for air-gapped systems or child-safe educational environments

---

## ❓ Troubleshooting

- 🔥 **Model takes time to load first time**: Wait ~10–20s
- 🧱 **C++ not compiling?** Install:
  ```bash
  sudo apt install g++ python3-dev
  pip install pybind11
  ```

---

## 📜 License

MIT License – free to use, modify, and distribute.

---

## 👨‍💻 Author

**Aaryan Banskota**  
*Full-stack + AI Developer*

GitHub: [@Aaryanbanskota](https://github.com/Aaryanbanskota)
