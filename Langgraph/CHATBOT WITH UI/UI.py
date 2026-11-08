import streamlit as st
from Backend import chatbot
from langchain_core.messages import HumanMessage
# Initialize history once
config={'configurable':{'thread_id':"1"}}
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Render previous messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# Handle new input
user_input = st.chat_input('Type here :')
if user_input:
    # Store & show user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    response=chatbot.invoke({'messages':HumanMessage(content=user_input)},config=config)
    ai_message=response['messages'][-1].content
    # Store & show assistant reply (echo, for now)
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
