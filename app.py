import streamlit as st
import json
import os
from Chunker import CodeChunker
from utils import count_tokens
# Function to load JSON data
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Setup Streamlit page
st.set_page_config(page_title="Cintra Code Chunker", layout="wide")

# Assuming app.py and mock_codefiles.json are in the same directory
json_file_path = os.path.join(os.path.dirname(__file__), 'mock_codefiles.json')
code_files_data = load_json_file(json_file_path)

# Extract filenames and contents
code_files = list(code_files_data.keys())

# UI Elements
st.title('Cintra Code Chunker')

# File selection
selected_file_name = st.selectbox("Select a code file", code_files)

# Assuming you have the content as a string in the JSON, extract directly
code_content = code_files_data[selected_file_name]

file_extension = selected_file_name.split('.')[-1]

# Determine the language for syntax highlighting
def get_language_by_extension(file_extension):
    if file_extension in ['py', 'python']:
        return 'python'
    elif file_extension in ['js', 'jsx', 'javascript']:
        return 'javascript'
    elif file_extension == 'css':
        return 'css'
    else:
        return None  # Default to no syntax highlighting if extension is not recognized

language = get_language_by_extension(file_extension)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Original File')
    st.code(code_content, language=language)

with col2:
    token_chunk_size = st.sidebar.slider('Token Chunk Size Target', min_value=5, max_value=50, value=25)
    if st.sidebar.button("Chunk Code"):
        # Initialize the code chunker
        code_chunker = CodeChunker(file_extension=file_extension)

        # Chunk the code content
        chunked_code_dict = code_chunker.chunk(code_content, token_chunk_size)

        # Select a chunk to display
        chunk_keys = list(chunked_code_dict.keys())
        selected_chunk_key = st.selectbox("Select Chunk", options=chunk_keys)

        st.subheader('Chunked Code')
        st.code(chunked_code_dict[selected_chunk_key], language=language)