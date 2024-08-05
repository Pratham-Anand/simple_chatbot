from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama

import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers

from dotenv import load_dotenv


load_dotenv()


import os
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title('Langchain demo with Google Gemini pro')
input_text=st.text_input("Search the topic u want")

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=GOOGLE_API_KEY)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
