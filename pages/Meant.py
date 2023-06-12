import streamlit as st
import numpy as np
from scipy import stats

st.title('Uji Hipotesis Rata-rata')

# Input data
data = st.text_area('Masukkan data (pisahkan dengan koma)')

# Input level signifikansi
alpha = st.number_input('Masukkan level signifikansi', min_value=0.01, max_value=0.5, value=0.05, step=0.01)

# Convert input data to array
data_array = np.array([float(x.strip()) for x in data.replace('\n', '').split(',') if x.strip()])

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(data_array, popmean=0)

# Menampilkan hasil uji hipotesis
st.write('Data:', data_array)
st.write('Jumlah Data:', len(data_array))
st.write('Rata-rata:', np.mean(data_array))
st.write('T-Statistic:', t_statistic)
st.write('P-Value:', p_value)

# Uji signifikansi
if p_value < alpha:
    st.write('Hasil Uji: Terdapat bukti yang cukup untuk menolak hipotesis nol')
else:
    st.write('Hasil Uji: Tidak cukup bukti untuk menolak hipotesis nol')
