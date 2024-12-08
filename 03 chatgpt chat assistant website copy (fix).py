import openai
import streamlit as st

openai.api_key = "APIkeys"

messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Streamlit app UI
st.title("Real Estate Pro Chatbot")

user_input = st.text_input("Ask a question:", "")
if user_input:
    reply = CustomChatGPT(user_input)
    st.write(f"Chatbot: {reply}")
