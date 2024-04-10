import streamlit as st
from utils import load_json, count_tokens
import json

# Set up the Streamlit page configuration
st.set_page_config(page_title="Cintra Code Chunker", layout="wide")

def main():
    # Streamlit widgets for file selection
    st.title("Cintra Code Chunker")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Displaying the original file content
        file_content = uploaded_file.getvalue().decode("utf-8")
        st.text_area("File content", value=file_content, height=250, max_chars=50000)

        # Input for token chunk size target
        token_chunk_size = st.slider(
            "Select token chunk size target", min_value=10, max_value=500, value=100
        )

        # Button to trigger chunking process
        if st.button("Chunk Code"):
            # Assuming the existence of a function to chunk code based on token size
            # This is a placeholder for the actual chunking logic which would likely involve
            # the 'count_tokens' function from utils.py and some logic to split the code into chunks
            # For demonstration, we'll just show a message
            st.success(
                f"Code has been chunked with a target of {token_chunk_size} tokens per chunk."
            )
            # Displaying the chunked code - this would be replaced with actual chunked code display logic
            st.text_area(
                "Chunked Code",
                value="Chunked code would appear here...",
                height=250,
                max_chars=50000,
            )


if __name__ == "__main__":
    main()