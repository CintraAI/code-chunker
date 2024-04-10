import streamlit as st
from Chunker import CodeChunker

# Initialize the code chunker for Python files
code_chunker = CodeChunker(file_extension="py")

# Sample code to be chunked
sample_code = """
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
"""

# User selects the token chunk size target
token_chunk_size_target = st.slider(
    "Select token chunk size target", min_value=1, max_value=100, value=20
)

# Chunk the sample code based on the selected token chunk size target
chunked_code = code_chunker.chunk(sample_code, token_chunk_size_target)

# Display the original code
st.write("Original Code:")
st.code(sample_code)

# Display the chunked code
st.write("Chunked Code:")
for chunk_number, chunk in chunked_code.items():
    st.write(f"Chunk {chunk_number}:")
    st.code(chunk)
