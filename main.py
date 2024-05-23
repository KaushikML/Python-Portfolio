import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/Kaushik.png",width=400)

with col2:
    st.title("Kaushik Roy")
    content= """ 
    I am Machine Learning Engineer | Passionate about building intelligent systems
    . Skilled in NLP, computer vision, and deep learning frameworks (TensorFlow, PyTorch).
     Always learning and exploring new applications of ML. """
    st.info(content)

content2=""" Below are some basic python apps that I created while learning"""

st.write(content2)