import pandas as pd
import streamlit as st


import get_data as data

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🌏", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by Bota*")
# st.write("---")

st.button("Launch baloons", on_click=st.balloons)

st.button("Let it snow",on_click=st.snow)

students=st.radio("Class",["High School","Middle School","Elementary"])
number_of_students=st.slider("Number of students",1,35 )
st.write("There are", number_of_students, "students")