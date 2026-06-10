import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="Priyanshi_ChatBot" 
    page_icon= "🤖"
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("models/gemini-2.5-flash")

st.title("priyanshi's AI Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt=st.chat_input("type your message...")

if prompt:
    st.session_state.messages.append(
        {

        "role":"user" ,
        "content":prompt
        }
    )
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking....."):
            response=model.generate_content(prompt)
            ai_response=response.text

            st.write(ai_response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )



