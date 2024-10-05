import streamlit as st

st.title("Market Research Report Generator")

st.write("Upload your company documentation to generate a tailored TAM/SAM/SOM analysis.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "pptx"])

if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    # You can add logic to process the file here.
