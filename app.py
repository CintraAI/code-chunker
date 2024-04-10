import streamlit as st
from utils import load_json
from Chunker import CodeChunker

# Slider for selecting a value
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

# Slider for inputting 'token chunk size target'
token_chunk_size = st.slider(
    "Select token chunk size target", min_value=1, max_value=100, value=25
)
st.write("Token chunk size target:", token_chunk_size)

# Assuming 'mock_codefiles.json' is a file in the same directory that contains code to be chunked
# and 'app.py' is part of the mock codebase for demonstration purposes
mock_codebase = load_json("mock_codefiles.json")
app_code = mock_codebase[
    "app.py"
]  # This would be replaced with actual code fetching logic in a real scenario

# Initialize CodeChunker with Python file extension
code_chunker = CodeChunker(file_extension="py")
chunks = code_chunker.chunk(app_code, token_limit=token_chunk_size)

# Display chunked code under the label 'Chunked Code'
st.write("Chunked Code:")
for chunk_number, chunk_code in chunks.items():
    st.text(f"Chunk {chunk_number}:\n{chunk_code}")
