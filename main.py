import streamlit as st
import  pandas


col1,col2=st.columns(2)

with col1:
    st.image("images/Kaushik.png",width=300)

with col2:
    st.title("Kaushik Roy")
    content= """ 
    I am Machine Learning Engineer | Passionate about building intelligent systems
    . Skilled in NLP, computer vision, and deep learning frameworks (TensorFlow, PyTorch).
     Always learning and exploring new applications of ML. """
    st.info(content)

content2=""" Below are some basic python apps that I created while learning"""

st.write(content2)

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source CODE] ({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source CODE] ({row['url']})")