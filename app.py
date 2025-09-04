import streamlit as st
import pandas as pd
import time
import json
import os
from datetime import datetime

st.write("In the top-left corner, click and enter your data!")
if "progress_done" not in st.session_state:
    st.session_state.progress_done = False
    st.session_state.progress = 0

if not st.session_state.progress_done:
    progress = st.progress(0)
    for i in range(st.session_state.progress, 101):
        progress.progress(i)
        time.sleep(0.02)
    st.session_state.progress_done = True


st.header("Welcome to Amir site!")
st.toast("Developer: Amir")


with st.sidebar:
    st.header("Enter data, please!")
    user_name = st.text_input("Your name please!", key="name")
    user_surname = st.text_input("Your surname, please!", key="surname")
    age_input = st.number_input("Your age please!", key="age_input")
    gmail = st.text_input("Your gmail, please!", key="gmail")
    password = st.text_input("Your password, please!", key="password", type="password")

    st.info(f"Your name is {user_name}")
    st.info(f"Your surname is {user_surname}")
    st.info(f"Your age is {age_input}")
    st.info(f"Your gmail is {gmail}")

    if st.button("Do you want to see your password?", key="show_password"):
        st.success(f"Your password is {password}")

    st.image("https://media.tenor.com/alYCmq5y7OgAAAAM/light.gif")
    st.write("Web developer: Amir Aliyev!")


st.write("Bitcoin:")
bitcoin_data = {
    "2020": [7200, 8900, 9000, 11000, 13200, 19000],
    "2021": [35000, 50000, 60000, 34000, 43000, 64800],
    "2022": [47000, 40000, 30000, 20000, 25000, 16000],
    "2023": [20000, 25000, 28000, 30000, 35000, 38000],
    "2024": [45000, 55000, 60000, 65000, 75000, 100000],
    "2025": [85000, 90000, 95000, 100000, 110000, 115000]
}
df_bitcoin = pd.DataFrame(bitcoin_data)
st.write(df_bitcoin)
st.line_chart(df_bitcoin)


st.write("Binance Coin:")
bnb_data = {
    "2020": [13.70, 17.36, 18.50, 19.20, 20.10, 21.00, 22.30, 23.50, 24.80, 26.00, 27.50, 29.00],
    "2021": [37.66, 42.00, 47.50, 53.00, 58.50, 64.00, 70.00, 76.00, 82.00, 88.00, 94.00, 100.00],
    "2022": [110.00, 115.00, 120.00, 125.00, 130.00, 135.00, 140.00, 145.00, 150.00, 155.00, 160.00, 165.00],
    "2023": [170.00, 175.00, 180.00, 185.00, 190.00, 195.00, 200.00, 205.00, 210.00, 215.00, 220.00, 225.00],
    "2024": [230.00, 235.00, 240.00, 245.00, 250.00, 255.00, 260.00, 265.00, 270.00, 275.00, 280.00, 285.00],
    "2025": [290.00, 295.00, 300.00, 305.00, 310.00, 315.00, 320.00, 325.00, 330.00, 335.00, 340.00, 345.00]
}
df_bnb = pd.DataFrame(bnb_data)
st.write(df_bnb)
st.line_chart(df_bnb)


car_option = st.selectbox(
    "What is your favorite car?", 
    ("Bmw", "Mercedes", "Audi", "Tesla", "Nissan", "Hyundai"),
    key="favorite_car"
)
st.info(f"Your favorite car is {car_option}")


languages = st.multiselect(
    "Select your favorite programming language:",
    ["Python", "C", "Javascript", "Java", "C--", "C#", "C++"],
    key="prog_lang"
)
st.info(f"Your favorite programming languages: {', '.join(languages)}")


user_age = st.slider("How old are you?", 0, 99, 25, key="slider_age")
st.write(f"You are {user_age} y.o")

st.write("Please choose:")
eldest = st.checkbox("I'm the eldest child", key="eldest")
middle = st.checkbox("I'm the middle child", key="middle")
youngest = st.checkbox("I'm the youngest child", key="youngest")

if eldest:
    st.success("Ultra chance of success, you got really lucky!")
elif middle:
    st.error("Bad chance of success, you didn't get any luck at all!")
elif youngest:
    st.warning("Average chance of success, well you got pretty lucky")
else:
    st.write("Please, select")


with st.expander("Developer:"):
    st.write("Developer is Amir Aliyev")
    st.image("https://images.steamusercontent.com/ugc/2046369901430585339/598952A4C009DB8F3277A60971F31667DFEFD94A/")

with st.expander("Developer Data:"):
    st.write("Amir Aliyev, live in Azerbaijan - Baku, 11 y.o")
    st.info("Born in 2014, to become a billionaire!")
    st.image("https://img-webcalypt.ru/img/thumb/lg/28692/20258/IWr2mmdZNIZBbR7qE34gYdXwsq72FafrH8Q7a0889AJK5ZUm9mFXXQixEhwDpZpb0RsOWXjUPdwQouUsc4RXzrYh30PsoddAHcL5o54RLlcvAI9Tx6uiQhaqaJgxbFdA.jpeg.jpg")

FILE_PATH = "messages.json"

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        all_messages = json.load(f)
else:
    all_messages = []

with st.form("chat_form", clear_on_submit=True):
    st.write("You must enter your details to login")
    username = st.text_input("Your user_name:")
    message = st.text_area("Message:")
    gmail = st.text_input("Your gmail:")
    password = st.text_input("Your password:")
    submitted = st.form_submit_button("Send your message")

    if submitted and username and message and password and gmail:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        all_messages.append({
            "user": username,
            "message": message,
            "password": password,
            "time": timestamp,
            "gmail": gmail
        })
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(all_messages, f, ensure_ascii=False, indent=2)
        st.success("Message success")

owner_password = st.text_input("Admin psw - Amir psw (for secret data)", type="password")

st.subheader("User Messages:")

for entry in all_messages:
    if "gmail" not in entry:
        entry["gmail"] = gmail
    if owner_password == "15072014amir":
        st.markdown(f"*{entry['user']}* {entry['time']} | Message: {entry['message']} | Gmail: {entry['gmail']} | Password: {entry['password']}")
    else:
        st.markdown(f"*{entry['user']}* {entry['time']} | Message: {entry['message']}")

with st.expander("Developer Data:"):
    st.write("Amir Aliyev, live in Azerbaijan - Baku, 11 y.o")
    st.info("Born in 2014, to become a billionaire!")
    st.image("https://img-webcalypt.ru/img/thumb/lg/28692/20258/IWr2mmdZNIZBbR7qE34gYdXwsq72FafrH8Q7a0889AJK5ZUm9mFXXQixEhwDpZpb0RsOWXjUPdwQouUsc4RXzrYh30PsoddAHcL5o54RLlcvAI9Tx6uiQhaqaJgxbFdA.jpeg.jpg")
