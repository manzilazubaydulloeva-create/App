import streamlit as st
import pandas as pd

st.write("Welcome to Amirchik site!")

with st.sidebar:
    st.header("Enter data, please!")
    user_name = st.text_input("Name please!")
    age = st.number_input("Your age please!")
    st.info(f"Your name is {user_name}")
    st.info(f"Your age is {age}")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6eVsSVpYYpDYb6fkTkx85NJPvDNpKBKi17g&s")
    st.write("Web developer: Amir Aliyev!")
st.write("*Bitcoin:*")
data = {"2020": [7200, 8900, 9000, 11000, 13200, 19000],
      "2021": [35000, 50000, 60000, 34000, 43000, 64800],
      "2022": [47000, 40000, 30000, 20000, 25000, 16000],
      "2023": [20000, 25000, 28000, 30000, 35000, 38000],
      "2024": [45000, 55000, 60000, 65000, 75000, 100000],
      "2025": [85000, 90000, 95000, 100000, 110000, 115000]
      
}
df = pd.DataFrame(data)
st.write(df)
st.line_chart(df)

option = st.selectbox("What is your favorite car?", ("Bmw", "Mercedes", "Audi", "Tesla", "Nissan", "Hyundai"))
st.info(f"Your favorite car is {option}")
multi = st.multiselect("Select your favorite programming language:",["Python", "C", "Javascript", "Java",
                                                                     "C--", "C#", "C++"])

st.info(f"Your favorite programming languages: {', '.join(multi)}")

age = st.slider("How old are you?", 0, 99, 25)
if age:
    st.write(f"*You are {age} y.o*")
else:
    st.error("*I'm ... y.o*")
st.write(df)
st.line_chart(df)
st.write("Please choose:")
eldest = st.checkbox("I'm the eldest child")
middle = st.checkbox("I'm the middle child")
youngest = st.checkbox("I'm the youngest child")
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
    st.info("Born in 2014, to become a billionire!")
    st.image("https://img-webcalypt.ru/img/thumb/lg/28692/20258/IWr2mmdZNIZBbR7qE34gYdXwsq72FafrH8Q7a0889AJK5ZUm9mFXXQixEhwDpZpb0RsOWXjUPdwQouUsc4RXzrYh30PsoddAHcL5o54RLlcvAI9Tx6uiQhaqaJgxbFdA.jpeg.jpg")