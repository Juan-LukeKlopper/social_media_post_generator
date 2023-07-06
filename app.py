import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

apikey = os.environ.get('OPENAI_API_KEY')

st.title("Social Media Post Generator")
prompt = st.text_input("Please enter a topic or item to generate social media around")

tweet_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are a social Media manager and content creator please generate a short tweet in the tone of Elon Musk around this prompt, please do not mention his name and tweet out of first person perspective: {topic} '
        )

tweet2_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are a social Media manager and content creator please generate a short tweet in the tone of Farza from Buildspace around this prompt, please do not mention his name and tweet out of first person perspective: {topic} '
        )

tweet3_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are a social Media manager and content creator please generate a short tweet in the tone of Rich Harris around the following prompt, please do not mention his name and tweet out of first person perspective: {topic} '
        )


discord_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are a social Media manager and content creator please generate a long discord message in the tone of Elon Musk around this prompt, please do not mention his name and tweet out of first person perspective: {topic} '
        )


discord2_template = PromptTemplate(
        input_variables= ['topic'],
        template='You are a social Media manager and content creator please generate a long discord in the tone of Lex Fridman around this prompt, please do not mention his name and tweet out of first person perspective: {topic} '
        )

llm = OpenAI(temperature=0.9)
tweet_chain = LLMChain(llm=llm, prompt=tweet_template, verbose=True, output_key='tweet1')
tweet2_chain = LLMChain(llm=llm, prompt=tweet2_template, verbose=True, output_key='tweet2')
tweet3_chain = LLMChain(llm=llm, prompt=tweet3_template, verbose=True, output_key='tweet3')
discord_chain = LLMChain(llm=llm, prompt=discord_template, verbose=True, output_key='discord1')
discord2_chain = LLMChain(llm=llm, prompt=discord2_template, verbose=True, output_key='discord2')

@st.cache(hash_funcs={LLMChain: lambda _: None})  # Cache the prompt generation results
def generate_prompt_output(prompt):
    if prompt:
        tweet1 = tweet_chain.run(topic=prompt)
        tweet2 = tweet2_chain.run(topic=prompt)
        tweet3 = tweet3_chain.run(topic=prompt)
        discord1 = discord_chain.run(topic=prompt)
        discord2 = discord2_chain.run(topic=prompt)
        return tweet1, tweet2, tweet3, discord1, discord2
    else:
        return None


output = generate_prompt_output(prompt)

if prompt:
    tweet1, tweet2, tweet3, discord1, discord2 = generate_prompt_output(prompt)
    option = st.radio('Please select one or multiple options from below',
                  key="twitter_choice",
                  options=[tweet1, tweet2, tweet3],
                  )
    st.write(f'discord message option 1: {discord1}')
    st.write(f'discord message option 2: {discord2}')
    if option:
        st.write('You selected:', option)


