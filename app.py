import streamlit as st
import os

# List example code files from a directory
code_files_directory = "example_code_files"
code_files = os.listdir(code_files_directory)

# Dropdown menu for the user to select a code file
selected_file = st.selectbox("Select a code file", code_files)

# Display the selected file content
file_path = os.path.join(code_files_directory, selected_file)
with open(file_path, "r") as file:
    code_content = file.read()
    st.code(code_content, language="python")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
