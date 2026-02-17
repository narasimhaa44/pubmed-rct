import streamlit as st
from pubmed_rct import load_data, train_model, evaluate

st.title("PubMed RCT Classifier")

st.write("Upload abstract text to classify:")

text = st.text_area("Paste abstract here")

if st.button("Classify"):
    # your custom logic here
    result = "Prediction result here"
    st.write("Prediction:", result)
