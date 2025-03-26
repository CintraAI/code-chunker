import streamlit as st
import json
import os
from Chunker import CodeChunker

# Set Streamlit page config at the very beginning
st.set_page_config(page_title="Cintra Code Chunker", layout="wide")

# Function to load JSON data
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to read code from an uploaded file
def read_code_from_file(uploaded_file):
    return uploaded_file.getvalue().decode("utf-8")

st.link_button('Contribute on GitHub', 'https://github.com/CintraAI/code-chunker', help=None, type="secondary", disabled=False, use_container_width=False)

json_file_path = os.path.join(os.path.dirname(__file__), 'mock_codefiles.json')
code_files_data = load_json_file(json_file_path)

# Extract filenames and contents
code_files = list(code_files_data.keys())

st.title('Cintra Code Chunker')

selection_col, upload_col = st.columns(2)
with selection_col:
    # File selection dropdown
    selected_file_name = st.selectbox("Select an example code file", code_files)

with upload_col:
    # File upload
    uploaded_file = st.file_uploader("Or upload your code file", type=['py', 'js', 'css', 'jsx'])

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
    elif file_extension in ['ts', 'typescript', 'tsx']:
        return 'typescript'
    elif file_extension in ['rb', 'ruby']:
        return 'ruby'
    elif file_extension == 'php':
        return 'php'
    elif file_extension == 'go':
        return 'go'
    else:
        return None

language = get_language_by_extension(file_extension)

st.write("""
### Choose Chunk Size Target""")
token_chunk_size = st.number_input('Target Chunk Size Target', min_value=5, max_value=1000, value=25, help="The token limit guides the chunk size in tokens (tiktoken, gpt-4), aiming for readability without enforcing a strict upper limit.")

with st.expander("Learn more about the chunk size target"):
    st.markdown("""
The `token_limit` parameter in the `chunk` function serves as a guideline to optimize the size of code chunks produced. It is not a hard limit but rather an ideal target, attempting to achieve a balance between chunk size and maintaining logical coherence within the code.

- **Adherence to Logical Breakpoints:** The chunking logic respects logical breakpoints in the code, ensuring that chunks are coherent and maintain readability.
- **Flexibility in Chunk Size:** Chunks might be slightly smaller or larger than the specified `token_limit` to avoid breaking the code in the middle of logical sections.
- **Handling Final Chunks:** The last chunk of code captures any remaining code, which may vary significantly in size depending on the remaining code's structure.

This approach allows for flexibility in how code is segmented into chunks, emphasizing the balance between readable, logical code segments and size constraints.
    """)

original_col, chunked_col = st.columns(2)

with original_col:
    st.subheader('Original File')
    st.code(code_content, language=language)

# Initialize the code chunker
code_chunker = CodeChunker(file_extension=file_extension)

# Chunk the code content
chunked_code_dict = code_chunker.chunk(code_content, token_chunk_size)

with chunked_col:
    st.subheader('Chunked Code')
    for chunk_key, chunk_code in chunked_code_dict.items():
        st.code(chunk_code, language=language)