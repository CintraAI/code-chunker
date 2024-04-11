import streamlit as st
import json
import os
from Chunker import CodeChunker

# Function to load JSON data
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to read code from an uploaded file
def read_code_from_file(uploaded_file):
    return uploaded_file.getvalue().decode("utf-8")

# Setup Streamlit page
st.set_page_config(page_title="Cintra Code Chunker", layout="wide")

# Assuming app.py and mock_codefiles.json are in the same directory
json_file_path = os.path.join(os.path.dirname(__file__), 'mock_codefiles.json')
code_files_data = load_json_file(json_file_path)

# Extract filenames and contents
code_files = list(code_files_data.keys())

# UI Elements
st.title('Cintra Code Chunker')

# Create two columns for file selection and file upload
col1, col2 = st.columns(2)

with col1:
    # File selection dropdown
    selected_file_name = st.selectbox("Select an example code file", code_files)

with col2:
    # File upload
    uploaded_file = st.file_uploader("Or upload your code file", type=['py', 'js', 'css'])

# Determine the content and file extension based on selection or upload
if uploaded_file is not None:
    code_content = read_code_from_file(uploaded_file)
    file_extension = uploaded_file.name.split('.')[-1]
else:
    code_content = code_files_data.get(selected_file_name, "")
    file_extension = selected_file_name.split('.')[-1] if selected_file_name else None

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

# User input for Token Chunk Size
token_chunk_size = st.number_input('Chunk Size Target Measured in Tokens (Using Tiktoken)', min_value=5, max_value=1000, value=25)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Original File')
    st.code(code_content, language=language)

# Initialize the code chunker
code_chunker = CodeChunker(file_extension=file_extension)

# Chunk the code content
chunked_code_dict = code_chunker.chunk(code_content, token_chunk_size)

# Automatically display chunks without needing to select
with col2:
    st.subheader('Chunked Code')
    for chunk_key, chunk_code in chunked_code_dict.items():
        st.code(chunk_code, language=language)