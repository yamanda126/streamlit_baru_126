import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Distribusi Poisson dan Uji Hipotesis dengan Streamlit')

# Input nilai lambda
lambd = st.number_input('Masukkan nilai lambda', value=5, step=1)

# Input jumlah kejadian pengamatan
observed_value = st.number_input('Masukkan jumlah kejadian pengamatan', value=5, step=1)

# Menghasilkan sampel dari distribusi Poisson
np.random.seed(0)
sample = np.random.poisson(lam=lambd, size=1000)

# Menampilkan histogram dari sampel
fig, ax = plt.subplots()
ax.hist(sample, bins=30, density=True, alpha=0.5)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title('Histogram Distribusi Poisson')
st.pyplot(fig)

# Menghitung p-value
p_value = 1 - stats.poisson.cdf(observed_value, mu=lambd)

# Menampilkan hasil uji hipotesis
st.write('Hasil Uji Hipotesis:')
st.write(f'Nilai pengamatan: {observed_value}')
st.write(f'Nilai p-value: {p_value:.4f}')

# Menentukan apakah H0 ditolak atau diterima
alpha = 0.05
if p_value < alpha:
    st.write('Hipotesis nol (H0) ditolak')
else:
    st.write('Hipotesis nol (H0) diterima')
