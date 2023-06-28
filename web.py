import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo app")
st.subheader("This is my todo list")
st.write("Tick off the To-Dos")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add a new todo")

print("Hello")
