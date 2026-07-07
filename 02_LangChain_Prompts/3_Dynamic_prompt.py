from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

#load_prompt to load the template.json generated from 2Prompt_generator.py

load_dotenv()

st.header('Research Tool')

#  Model
model = ChatGroq(
    model="llama-3.1-8b-instant"
)

# Inputs
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


#Prompt template is in 2PromptGenerator
template = load_prompt('template.json')


# calling template here by inputing values inside
# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

#summarize and print
if st.button("Summarize"):

    #now using chaining here -> get template then give it to model reducing template.invoke and  model.invoke
    chain = template | model
    result = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
    })
    # result = model.invoke(prompt)
    st.write(result.content)

    