from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A ChatBot with Ollama"

## Prompt Template
prompt = ChatPromptTemplate(
    [
        ("system", "You are an helpful assistant, answer all the questions concise and accurate with in three sentences."),
        ("user", "Question: {question}")
    ]
)

## Output Parser
output_parser = StrOutputParser()

## Generate Response
def generate_response(question, model, temperature, max_tokens):
    llm = OllamaLLM(model=model, temperature=temperature, max_tokens=max_tokens)
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    print(answer)
    return answer

st.title("Q&A ChatBot with Ollama")
model = st.sidebar.selectbox("Select a model", ["gemma:2b"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.6)
max_tokens = st.sidebar.slider("Max_Tokens", min_value=50, max_value=250, value=150)

st.write("Go ahead and ask what's in your mind.")
user_input = st.text_input("You: ")

submit = st.button("Submit")
if user_input and submit:
    response = generate_response(user_input, model, temperature, max_tokens)
    st.write(response)
elif user_input:
    st.write("Submit your query!")
else:
    st.write("Please Provide a query!")