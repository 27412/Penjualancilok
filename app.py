import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

# Judul halaman
st.title("Analisis Penjualan Cilok")

# Input user: Modal & Pendapatan Harian
modal = st.number_input("Modal Harian (Rp)", value=50000)
pendapatan = st.number_input("Pendapatan Harian (Rp)", value=200000)

# Konversi ke tipe numerik biasa (untuk hindari error sympy)
modal = int(modal)
pendapatan = int(pendapatan)

# Hitung keuntungan
keuntungan = pendapatan - modal
st.success(f"🧾 Keuntungan Harian: Rp {keuntungan:,}")

# ======== Bagian SymPy (turunan parsial) =========
M, P = sp.symbols('M P')
K = P - M
dK_dM = sp.diff(K, M)
dK_dP = sp.diff(K, P)

st.subheader("📐 Fungsi Keuntungan dan Turunan Parsial")
st.latex(r"K(M, P) = P - M")
st.latex(r"\frac{\partial K}{\partial M} = " + sp.latex(dK_dM))
st.latex(r"\frac{\partial K}{\partial P} = " + sp.latex(dK_dP))

# ======== Data Mingguan =========
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
pendapatan_mingguan = [pendapatan + i*5000 for i in range(7)]
modal_mingguan = [modal] * 7
keuntungan_mingguan = [p - m for p, m in zip(pendapatan_mingguan, modal_mingguan)]

# Buat DataFrame
df = pd.DataFrame({
    'Hari': hari,
    'Modal': modal_mingguan,
    'Pendapatan': pendapatan_mingguan,
    'Keuntungan': keuntungan_mingguan
})

# ======== Diagram Batang: Keuntungan Harian ========
st.subheader("📊 Diagram Batang Keuntungan Harian")
fig1, ax1 = plt.subplots()
ax1.bar(df['Hari'], df['Keuntungan'], color='green')
ax1.set_ylabel("Rp")
ax1.set_title("Keuntungan Harian")
st.pyplot(fig1)

# ======== Diagram Garis: Pertumbuhan Mingguan ========
st.subheader("📈 Grafik Pertumbuhan Keuntungan Mingguan")
fig2, ax2 = plt.subplots()
ax2.plot(df['Hari'], df['Keuntungan'], marker='o', linestyle='-', color='blue')
ax2.set_ylabel("Rp")
ax2.set_title("Pertumbuhan Keuntungan Mingguan")
ax2.grid(True)
st.pyplot(fig2)

# ======== Tabel ========
st.subheader("📋 Tabel Data Mingguan")
st.dataframe(df)
