import os
import streamlit as st
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

st.title("Streamlit + Langchain template")
prompt = st.text_input("Please enter a prompt?")

basic_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are an advanced AI chatbot please do this prompt: {topic} '
        )



llm = OpenAI(temperature=0.9)
basic_chain = LLMChain(llm=llm, prompt=basic_template, verbose=True, output_key='output')

if prompt:
    response = basic_chain.run(topic=prompt)
    st.write(response)
