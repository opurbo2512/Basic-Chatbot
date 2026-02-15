#import librarys
import streamlit as st
import time
import random
from PIL import Image

#page configuration and title
st.set_page_config(page_title="ChatBot",page_icon="🤖")
st.title("Rumi ChatBot🍫")

rumi = Image.open("img.jpg")

#About this bot
with st.expander("About this bot"):
    st.info("At first,I want to say that this is not a large language model like gpt or gemini. This is dumb like you. Here I use just some prompt and response.Ohh, I dedicate this bot to Rumi. So, it's name is 'Rumi ChatBot🍫'.")

#function for creating response
def get_response(prompt):
    #dictionary of responses
    """
    dic = {
    "hi": "Hello!☺️",
    "hello": "Hi there!☺️",
    "how are you": "I'm good, thank you! How about you?😘",
    "how's it going": "Everything's great! How about you?😌",
    "good morning": "Good morning! Have a nice day!😝",
    "good night": "Good night! Sleep well!😝",
    "thank you": "You're welcome! 😊",
    "thanks": "No problem!",
    "what is your name": "I'm Rumi, your offline chatbot.",
    "who are you": "I'm a simple offline chatbot.",
    "see you": "See you soon!",
    "bye": "Goodbye! Take care!",
    "goodbye": "Bye! Have a nice day!",
    "what time is it": "I can't tell time, but hope your day is great!",
    "how old are you": "I don't have an age, I'm just a bot!",
    "what can you do": "I can chat with you offline!",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus! 😄",
    "i'm sad": "I'm here for you. Hope you feel better soon!",
    "i'm happy": "That's great! 😄",
    "what is love": "Love is complicated, but it's beautiful!",
    "who made you": "I was made by my human creator.",
    "help": "Sure! You can say hi, ask my name, or just chat!",
    "how is the weather": "I can't check the weather, but hope it's nice outside!",
    "what's up": "Not much! How about you?",
    "greetings": "Greetings! How are you today?",
    "nice to meet you": "Nice to meet you too!",
    "welcome": "Thank you! Happy to chat with you.",
    "i love you": "Aww! That's sweet ❤️",
    "are you real": "I'm real as a bot can be! 😄",
    "what is your favorite color": "I don't have favorites, but I like all colors!",
    "do you sleep": "I never sleep, I'm always here to chat!",
    "can you help me": "Of course! What would you like to talk about?",
    "good afternoon": "Good afternoon! Hope your day is going well!",
    "good evening": "Good evening! How was your day?",
    "i'm bored": "Let's chat! Ask me anything.",
    "tell me a story": "Once upon a time, there was a little bot named Rumi...",
    "sing a song": "La la la... 🎵 I'm not very good at singing though!",
    "repeat after me": "Sure! What do you want me to repeat?",
    "joke": "Why don't programmers like nature? Too many bugs!",
    "favorite food": "I don't eat, but I love virtual cookies! 🍪",
    "yes": "Okay!",
    "no": "Alright!",
    "maybe": "Hmm, I'm not sure either.",
    "i need help": "I'm here! What do you need help with?",
    "congratulations": "Thank you! 🎉",
    "good luck": "Good luck to you too!",
    "sorry": "No worries!",
    "welcome back": "Glad to see you again!",
    "default": "Sorry, I didn't understand that.",
    "who is rumi": "Hmm… Rumi is someone special, but maybe you can figure it out 😉",
    "why your name is rumi": "Names have stories… mine is a little secret for now 😏"
    }
    
    

    #searching in dictionary
    key = prompt.strip().lower()
    response = dic.get(key,"Sorry, I cannot understand that.")
    """
    lis = ["o","hmm","😂","🤣","Ok"]
    #returning the value
    response = random.choice(lis)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

#making session_state.message
if "messages" not in st.session_state:
    st.session_state.messages = []

#showing the full messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#taking input from user
prompt = st.chat_input("What is up?")

#showing the input and response
if prompt:
    #showing the input
    with st.chat_message("user"):
        st.markdown(prompt)
    #saving data to session_state
    st.session_state.messages.append({"role":"user","content":prompt})

    #showing response
    with st.chat_message("assistant",avatar=rumi):
        #creating response using function
        response = "".join(get_response(prompt))
        st.markdown(response)

    #saving data to session_state
    st.session_state.messages.append({"role":"assistant","content":response})
    
