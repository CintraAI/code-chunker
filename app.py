import streamlit as st
import json
import os
from Chunker import CodeChunker
from utils import count_tokens

# Load JSON data for code file paths
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Setup Streamlit page
st.set_page_config(page_title="Cintra Code Chunker", layout="wide")

# Assuming app.py and mock_codefiles.json are in the same directory
json_file_path = os.path.join(os.path.dirname(__file__), 'mock_codefiles.json')
code_files_data = load_json_file(json_file_path)
code_files = code_files_data['files']

# UI Elements
st.title('Cintra Code Chunker')

# File selection
selected_file_name = st.selectbox("Select a code file", code_files)

# Assuming you have the path or the content in the JSON, adjust accordingly
# This example assumes paths are stored in the JSON
file_path = os.path.join(os.path.dirname(__file__), 'example_code_files', selected_file_name)
with open(file_path, "r") as file:
    code_content = file.read()

col1, col2 = st.columns(2)

with col1:
    st.subheader('Original File')
    st.code(code_content, language='python')  # Adjust language dynamically based on file extension if necessary

with col2:
    token_chunk_size = st.sidebar.slider('Token Chunk Size Target', min_value=5, max_value=50, value=25)
    if st.sidebar.button("Chunk Code"):
        # Initialize the code chunker, assuming it takes file extension and encoding name
        file_extension = selected_file_name.split('.')[-1]
        code_chunker = CodeChunker(file_extension=file_extension)

        # Chunk the code content
        chunked_code_dict = code_chunker.chunk(code_content, token_chunk_size)

        # Select a chunk to display
        chunk_keys = list(chunked_code_dict.keys())
        selected_chunk_key = st.selectbox("Select Chunk", options=chunk_keys)

        st.subheader('Chunked Code')
        st.code(chunked_code_dict[selected_chunk_key], language='python')  # Adjust language dynamically based on file extension if necessary