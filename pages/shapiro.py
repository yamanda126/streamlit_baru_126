import streamlit as st
import pandas as pd 
from scipy.stats import shapiro 


df = pd.read_csv("https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv")
result = shapiro(df['grades'])

st.write('pvalue from shapiro test', result.pvalue)
st.bar_chart(df['grades'])


if result.pvalue<0.05:
    st.write('data tidak berdistribusi normal')
else:
    st.write('data berdistribusi normal')