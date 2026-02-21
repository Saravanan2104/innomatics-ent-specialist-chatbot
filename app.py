import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get the key and verify it exists
api_key = os.getenv('gemini_key')

if not api_key:
    st.error("API Key not found! Please set 'gemini_key' in your .env file.")
    st.stop()

# Initialize the client with the key directly
if 'client' not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)
    
client = st.session_state.client

system_prompt = """You are an ENT specialist.  provide solutions withing 2 or 3 lines.
if user asks other than ENT related doubts respectly say visit other doctor or may i refer based on your illness"""

st.title('ENT SPECIALIST Chatbot')
st.write('This model is an ENT specialist. Ask your doubts related to Ear, Nose, and Throat.')


# initialize chat session only once
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model = 'gemini-2.5-flash',
        config = types.GenerateContentConfig(
            system_instruction = system_prompt
        )
    )

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display the past messages
for role,text in st.session_state.messages:
    if role == 'user':
        st.markdown(f"**YOU:** {text}")
    else:
        st.markdown(f"**ENT SPECIALIST:** {text}")

user_input = st.chat_input('Type you message here...')

if user_input:
    st.session_state.messages.append(('user',user_input))

    chat = st.session_state.chat_session
    bot_reply = chat.send_message(user_input).text

    st.session_state.messages.append(('assistant',bot_reply))

    st.rerun()

