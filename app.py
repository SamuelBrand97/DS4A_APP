import streamlit as st
import pandas as pd
from PIL import Image


#TEST
image = Image.open('banner.jpg')

st.image(image)

st.title('Dummy Front End')
st.text('This is a Front End for Team 88')

st.sidebar.title('Data Management')
data1 = st.sidebar.file_uploader('Upload the database here')

data2 = st.sidebar.file_uploader('Upload the validation data')

if data1 and data2:
    df = pd.read_csv(data1, encoding = 'latin-1', skiprows = 1)
    st.header('Data Header')
    st.write(df.head(10))
