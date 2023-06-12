import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats

st.title('Uji Hipotesis ANOVA')

# Input data
data = st.text_area('Masukkan data (pisahkan dengan koma dan spasi)')

# Convert input data to DataFrame
data_list = [x.split(',') for x in data.split('\n')]
data_list = [x for x in data_list if all(val != '' for val in x)]

# Check if data is valid
if len(data_list) >= 2:
    num_columns = len(data_list[0])
    if num_columns == 2:
        data_df = pd.DataFrame(data_list, columns=['Group', 'Value'])
        data_df['Value'] = data_df['Value'].astype(float)

        # Perform ANOVA
        groups = data_df['Group'].unique()
        group_data = [data_df[data_df['Group'] == group]['Value'].values for group in groups]
        f_statistic, p_value = stats.f_oneway(*group_data)

        # Menampilkan hasil uji hipotesis
        st.write('Data:')
        st.write(data_df)
        if len(groups) > 2:
            st.write('Number of Groups:', len(groups))
        else:
            st.write('Group:', groups[0], 'vs', groups[1])
        st.write('F-Statistic:', f_statistic)
        st.write('P-Value:', p_value)

        # Uji signifikansi
        alpha = 0.05
        if p_value < alpha:
            st.write('Hasil Uji: Terdapat bukti yang cukup untuk menolak hipotesis nol')
        else:
            st.write('Hasil Uji: Tidak cukup bukti untuk menolak hipotesis nol')
    else:
        st.write('Input data harus terdiri dari dua kolom: Group dan Value.')
else:
    st.write('Input data harus memiliki setidaknya dua baris untuk melakukan uji ANOVA.')
