import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("💸 Aplikasi Analisis Keuntungan Penjualan Cilok")

# Definisi simbolik
M, P = sp.symbols('M P')  # M = Modal, P = Pendapatan
K = P - M                 # Fungsi Keuntungan

# Tampilkan fungsi simbolik
st.latex(r"K(M, P) = P - M")

# Turunan parsial terhadap M dan P
dK_dM = sp.diff(K, M)
dK_dP = sp.diff(K, P)

st.latex(r"\frac{\partial K}{\partial M} = " + sp.latex(dK_dM))
st.latex(r"\frac{\partial K}{\partial P} = " + sp.latex(dK_dP))

# Input nilai modal dan pendapatan
modal_input = st.number_input("Masukkan Modal (Rp)", value=50000)
pendapatan_input = st.number_input("Masukkan Pendapatan (Rp)", value=200000)

# Hitung nilai fungsi dan turunannya di titik tersebut
K_val = K.subs({M: modal_input, P: pendapatan_input})
dK_dM_val = dK_dM.subs({M: modal_input, P: pendapatan_input})
dK_dP_val = dK_dP.subs({M: modal_input, P: pendapatan_input})

st.write(f"### 💰 Keuntungan: Rp{K_val:,}")
st.write(f"Gradient di titik tersebut: (∂K/∂M = {dK_dM_val}, ∂K/∂P = {dK_dP_val})")

# --- Visualisasi Permukaan & Bidang Singgung ---
st.subheader("📈 Grafik Permukaan Keuntungan & Bidang Singgungnya")

# Rentang nilai untuk visualisasi
modal_range = np.linspace(modal_input - 30000, modal_input + 30000, 50)
pendapatan_range = np.linspace(pendapatan_input - 80000, pendapatan_input + 80000, 50)
M_vals, P_vals = np.meshgrid(modal_range, pendapatan_range)

# Fungsi Keuntungan sebagai fungsi numerik
K_func = sp.lambdify((M, P), K, 'numpy')
Z = K_func(M_vals, P_vals)

# Fungsi bidang singgung (tangent plane)
Z_tangent = float(K_val) + float(dK_dM_val)*(M_vals - modal_input) + float(dK_dP_val)*(P_vals - pendapatan_input)

# Plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(M_vals, P_vals, Z, cmap='viridis', alpha=0.7, label="Permukaan K")
ax.plot_surface(M_vals, P_vals, Z_tangent, color='red', alpha=0.5)
ax.scatter(modal_input, pendapatan_input, float(K_val), color='black', s=50, label='Titik Saat Ini')

ax.set_title("Permukaan Keuntungan dan Bidang Singgung")
ax.set_xlabel("Modal (Rp)")
ax.set_ylabel("Pendapatan (Rp)")
ax.set_zlabel("Keuntungan (Rp)")

st.pyplot(fig)
