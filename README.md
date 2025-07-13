# 🧠 Q&A ChatBot with Ollama

Hey there! 👋  
This is a simple and interactive Q&A chatbot built with [Streamlit](https://streamlit.io/) and powered by [LangChain](https://www.langchain.com/) and [Ollama](https://ollama.ai/).  
It’s designed to give short, helpful answers to your questions using a language model — kind of like a mini search buddy that replies in three sentences or less!

---

## 🚀 Features

- ✅ Ask any question, get a concise answer  
- 🔧 Adjustable settings like temperature and token limits via the sidebar  
- 💬 Clean, Streamlit-powered chat interface  
- 🤖 Runs on local models via Ollama
- 📈 LangSmith integration for tracing and debugging (optional)

---

## 🛠️ Built With

- [LangChain](https://github.com/langchain-ai/langchain) – for prompt management and chaining  
- [Streamlit](https://streamlit.io/) – for the web UI  
- [Ollama](https://ollama.ai/) – for running LLMs locally  
- [dotenv](https://pypi.org/project/python-dotenv/) – for environment variable management  

---

## 🧪 Installation & Setup

1. **Clone this repo:**

   ```bash
   git clone https://github.com/Saketh35/QnA-ChatBot-with-Ollama.git
   cd QnA-ChatBot-with-Ollama
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**

   Create a `.env` file in the root folder with your LangChain API key (optional, for tracing):

   ```
   LANGCHAIN_API_KEY=your-langsmith-key-here
   ```

   *Don't worry — if you don’t have one, the app will still work without tracing.*

4. **Make sure Ollama is installed and the model is available:**

   Install Ollama and pull the required model:

   ```bash
   ollama run gemma:2b
   ```

---

## ▶️ How to Run the App

Once everything is set up, run this in your terminal:

```bash
streamlit run app.py
```

Head over to `http://localhost:8501` in your browser, and you're all set! Ask your first question and explore how the bot responds.

---

## ⚠️ Notes & Things to Improve

- Right now, it only supports one model (`gemma:2b`). Adding more models or dynamic loading could be a fun upgrade.  
- There’s no memory or conversation history — just single-turn Q&A for now.  
- No input validation or error messages for bad API keys, missing models, etc.  
- It might be cool to add markdown rendering, or even voice input/output later!  

---

## 🙌 Final Thoughts

This was a fun weekend build and a great way to get hands-on with LangChain and Ollama.  
If you have suggestions, spot a bug, or want to contribute — feel free to [open an issue](https://github.com/Saketh35/QnA-ChatBot-with-Ollama/issues) or submit a PR!

Let’s build cool stuff together. 🚀  
**– Saketh**
