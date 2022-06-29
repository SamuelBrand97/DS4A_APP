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

    df['APE2_VAL'].fillna('', inplace = True)
    df['APE1_VAL'].fillna('', inplace = True)
    df['NOM2_VAL'].fillna('', inplace = True)
    df['NOM1_VAL'].fillna('', inplace = True)

    df['FULL_NAME'] = df['NOM1_VAL'] + ' ' + df['NOM2_VAL'] + ' ' + df['APE1_VAL'] + ' ' + df['APE2_VAL']

    df['FULL_NAME'] = df['FULL_NAME'].str.upper() 

    df['FULL_NAME'] = df.FULL_NAME.str.replace('¥', 'N')


    df1 = pd.read_csv(data2, encoding = 'latin-1', skiprows = 1)
    
    df1['APE2_LOTE'].fillna('', inplace = True)
    df1['APE1_LOTE'].fillna('', inplace = True)
    df1['NOM2_LOTE'].fillna('', inplace = True)
    df1['NOM1_LOTE'].fillna('', inplace = True)

    df1['FULL_NAME'] = df1['NOM1_LOTE'] + ' ' + df1['NOM2_LOTE'] + ' ' + df1['APE1_LOTE'] + ' ' + df1['APE2_LOTE']

    df1['FULL_NAME'] = df1['FULL_NAME'].str.upper() 

    df1['FULL_NAME'] = df1.FULL_NAME.str.replace('¥', 'N')


    st.header('Data Header Database')
    st.write(df.head(50))

    st.header('Data Header Validation')
    st.write(df1.head(50))
