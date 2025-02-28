import streamlit as st
from transformers import pipeline

# Load a text summarization model (can be used for rephrasing)
rephrase_pipeline = pipeline("summarization")

def rephrase_text(text):
    # Using summarization model creatively for rephrasing
    return rephrase_pipeline(text, max_length=len(text.split()) + 20, min_length=len(text.split()) // 2, do_sample=False)[0]['summary_text']

st.title("Text Rephraser")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    st.subheader("Original Text:")
    st.text_area("", file_contents, height=200)
    
    if st.button("Rephrase Text"):
        rephrased_text = rephrase_text(file_contents)
        st.subheader("Rephrased Text:")
        st.text_area("", rephrased_text, height=200)
        
        st.download_button(
            label="Download Rephrased Text",
            data=rephrased_text,
            file_name="rephrased_text.txt",
            mime="text/plain"
        )
