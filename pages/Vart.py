import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

st.title('Uji Hipotesis Varians')

# Input data
data = st.text_area('Masukkan data (pisahkan dengan koma)')

# Input level signifikansi
alpha = st.number_input('Masukkan level signifikansi', min_value=0.01, max_value=0.5, value=0.05, step=0.01)

# Convert input data to array
data_array = np.array([float(x.strip()) for x in data.split(',') if x.strip()])

# Perform chi-square test
chi2_statistic, p_value = stats.chisquare(data_array)

# Menampilkan hasil uji hipotesis
st.write('Data:', data_array)
st.write('Jumlah Data:', len(data_array))
st.write('Rata-rata:', np.mean(data_array))
st.write('Chi-Square Statistic:', chi2_statistic)
st.write('P-Value:', p_value)

# Uji signifikansi
if p_value < alpha:
    st.write('Hasil Uji: Terdapat bukti yang cukup untuk menolak hipotesis nol')
else:
    st.write('Hasil Uji: Tidak cukup bukti untuk menolak hipotesis nol')
