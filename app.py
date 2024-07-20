import IPython
from dotenv import load_dotenv

load_dotenv()  #take environment variable from .env


#Import Required Libraries
import streamlit as st     #streamlit is a web interface for user interaction
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

import streamlit as st

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Q&A Pro", page_icon="✨", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextInput input {
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.title("Gemini Q&A Pro ✨")
st.header("Welcome to the Gemini Application")

# Input section
input = st.text_input("Ask your question here:", key="input", help="Type your question and click the 'Ask the question' button")

# Button to submit the question
submit = st.button("Ask the question")

# Response section
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
