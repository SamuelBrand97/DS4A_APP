import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('images/banner.jpg')

st.image(image)

st.title('Dummy Front End')
st.text('This is a Front End for Team 88')

st.sidebar.title('Navigation')
data1 = st.sidebar.file_uploader('Upload the database here')

if data1:
    df = pd.read_csv(data1, encoding = 'latin-1', skiprows = 1)
    st.header('Data Header')
    st.write(df.head(10))