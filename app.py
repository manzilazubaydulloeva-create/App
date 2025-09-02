import streamlit as st
import numpy as np
import pandas as pd


with st.sidebar:
    st.header("Enter data, please!")
    user_name = st.text_input("Name please!")
    st.info(f"Your name is {user_name}")
df = pd.DataFrame(
    np.random.randint(18, 91, size=(10, 3)),
    columns=["User 1-99 ", "User 100 - 999 ", "User 1000-9999"]
)

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
st.write("*User choises:*")
st.write(df)
st.line_chart(df)
st.write("Please choose:")
eldest = st.checkbox("I'm the eldest child")
middle = st.checkbox("I'm the middle child")
youngest = st.checkbox("I'm the youngest child")
if eldest:
    st.success("Ultra chance of success")
elif middle:
    st.error("Bad chance of success")
elif youngest:
    st.warning("Average chance of success")
else:
    st.write("Please, select")
with st.expander("Developer:"):
    st.write("Developer is Amir Aliyev")
    st.image("https://images.steamusercontent.com/ugc/2046369901430585339/598952A4C009DB8F3277A60971F31667DFEFD94A/")