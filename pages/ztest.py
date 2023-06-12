import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Distribusi Normal dan Uji Hipotesis dengan Streamlit')

# Input nilai mean dan standard deviation
mean = st.number_input('Masukkan nilai mean', value=0.0, step=0.1)
std = st.number_input('Masukkan nilai standard deviation', value=1.0, step=0.1)

# Input nilai pengamatan dan tingkat signifikansi (alpha)
observed_value = st.number_input('Masukkan nilai pengamatan', value=0.0, step=0.1)
alpha = st.number_input('Masukkan tingkat signifikansi (alpha)', value=0.05, step=0.01)

# Menghasilkan sampel dari distribusi normal
np.random.seed(0)
sample = np.random.normal(loc=mean, scale=std, size=1000)

# Menampilkan histogram dari sampel
fig, ax = plt.subplots()
ax.hist(sample, bins=30, density=True, alpha=0.5)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title('Histogram Distribusi Normal')
st.pyplot(fig)

# Menghitung z-score dan p-value
z_score = (observed_value - mean) / std
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

# Menampilkan hasil uji hipotesis
st.write('Hasil Uji Hipotesis:')
st.write(f'Nilai z-score: {z_score:.2f}')
st.write(f'Nilai p-value: {p_value:.4f}')

# Menentukan apakah H0 ditolak atau diterima
if p_value < alpha:
    st.write('Hipotesis nol (H0) ditolak')
else:
    st.write('Hipotesis nol (H0) diterima')
