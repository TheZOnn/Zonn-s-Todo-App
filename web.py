import streamlit as st
import modules.functions

todos = modules.functions.get_todos('todos.txt')


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    modules.functions.write_todos('todos.txt', todos)


st.title('My Todo App')
st.subheader('My todo app')
st.write('This is an app designed to increase productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modules.functions.write_todos('todos.txt', todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder='Enter a new todo...',
              on_change=add_todo, key='new_todo')
