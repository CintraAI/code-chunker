import streamlit as st

# Slider to select a value
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

# Displaying the selected file's contents in a read-only text area
file_content = """import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
"""

st.text_area("Original File", file_content, height=300, disabled=True)
