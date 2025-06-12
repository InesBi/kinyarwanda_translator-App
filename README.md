# Umuseke Translator App

A powerful multilingual translation tool focused on Kinyarwanda, English, and French, built with **Streamlit** and integrated with top translation APIs including **OpenAI**, **Google Translate**, and **Hugging Face**. It supports both manual text input and document uploads, offering editable output, context-aware synonym suggestions, and export to PDF or Word.

 # Example Usage
   - Launch the app(https://umuseketranslator.streamlit.app/)
   - Choose your input language and target language
   - Select a translation provider
   - Choose a domain/context (e.g., Legal, Medical)
   - Enter text or upload a document
   - Review/edit the translated output
   - Click Download as PDF or DOCX

# Notes
- For best Kinyarwanda performance, use OpenAI GPT-4 or custom-trained Hugging Face models
- The synonym engine uses domain-aware heuristics and GPT assistance
- Offline translation support is planned for low-resource settings

# Tech Stack
   - Streamlit   
   - OpenAI Python SDK   
   - Google Cloud Translate API   
   - Hugging Face Transformers   
   - python-docx, PyMuPDF, reportlab for document handling

## 🚀 Features

- 🔁 **Bidirectional translation** between Kinyarwanda, English, and French
- 🧠 **Choose your model**: OpenAI (ChatGPT), Google Translate, or Hugging Face
- 📝 **Text input** or 📄 **file upload** (TXT, DOCX, or PDF)
- 🎯 **Context-based translation** (General, Legal, Medical, Education, etc.)
- 🪄 **AI-suggested synonyms** for better localization (esp. Kinyarwanda)
- 🧾 **Editable translations** before final download
- 📥 Export final output as **PDF** or **Word (DOCX)**

---

## 🧰 Installation

1. **Clone the repository**:
   ```bash
      git clone https://github.com/yourusername/kinyarwanda-translator.git
      cd kinyarwanda-translator

2. **Install  dependencies**:
   ```bash
      pip install -r requirements.txt
3. **Run the App**:
  ```bash
     streamlit run app.py

