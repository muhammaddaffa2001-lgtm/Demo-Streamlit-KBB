import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# 1. Basic Text Components
st.title("Analisis Konflik Kebebasan Beragama/Kepercayaan di Indonesia")
st.write("""
## Peace without Justice is an Illusion!
Aplikasi ini dibuat untuk mendukung analisis data konflik terkait kebebasan 
beragama dan berkeyakinan di Indonesia.  
Silakan eksplorasi fitur-fitur berikut.
""")

# 2. Text Input
st.header("1. Input Identitas")
st.write("""
`st.text_input()` bisa digunakan untuk mencatat nama peneliti atau responden.
""")
user_input = st.text_input("Masukkan nama Anda", "Ketik di sini...")
st.write(f"Halo, {user_input}! Selamat datang di aplikasi analisis konflik.")

# 3. Buttons
st.header("2. Tombol Aksi")
if st.button("Lihat Pesan Perdamaian"):
    st.write("Kebebasan beragama adalah hak asasi yang fundamental.")

# 4. Checkbox
st.header("3. Checkbox")
show_content = st.checkbox("Tampilkan pesan penting")
if show_content:
    st.write("Konflik sering kali muncul karena intoleransi dan diskriminasi.")

# 5. Select Box
st.header("4. Pilihan Topik")
option = st.selectbox(
    "Pilih aspek konflik yang ingin Anda analisis:",
    ("Wilayah", "Aktor", "Jenis Konflik", "Tahun")
)
st.write(f"Anda memilih analisis berdasarkan: **{option}**")

# 6. Slider
st.header("5. Slider")
tahun = st.slider("Pilih rentang tahun penelitian:", 2000, 2025, 2015)
st.write(f"Anda sedang melihat data pada tahun: {tahun}")

# 7. File Uploader
st.header("6. Upload Dataset")
uploaded_file = st.file_uploader("Upload file CSV kasus konflik")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File berhasil diupload!")
    st.dataframe(df.head())
else:
    st.info("Silakan upload file CSV untuk memulai analisis data.")

# 8. Progress Bar
st.header("7. Progress")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)
st.write("Simulasi progress selesai!")

# 9. Sidebar
st.header("8. Sidebar")
with st.sidebar:
    st.header("Kontrol Tambahan")
    st.write("Gunakan ini untuk filter data.")
    if st.button("Tampilkan Prinsip HAM"):
        st.write("Kebebasan beragama dijamin dalam Pasal 28E UUD 1945.")

# 10. Columns
st.header("9. Layout dengan Kolom")
col1, col2 = st.columns(2)
with col1:
    st.write("Kasus di Wilayah A")
    st.button("Detail Kasus A")
with col2:
    st.write("Kasus di Wilayah B")
    st.button("Detail Kasus B")

# 11. Expander
st.header("10. Expander")
with st.expander("Klik untuk melihat kutipan hukum"):
    st.write("“Setiap orang bebas memeluk agama dan beribadat menurut agamanya.” (UUD 1945 Pasal 29)")

# 12. Markdown
st.header("11. Markdown")
st.markdown("""
### Fakta Penting:
- **Hak beragama** adalah hak yang tidak bisa dikurangi (non-derogable rights).  
- *Konflik sering kali dipicu oleh intoleransi antar kelompok.*  
- [Baca UU No. 39 Tahun 1999](https://peraturan.bpk.go.id/Home/Details/45417/uu-no-39-tahun-1999)
""")

# 13. Status Messages
st.header("12. Status Pesan")
st.success("Analisis berhasil dijalankan!")
st.info("Dataset Anda siap dieksplorasi.")
st.warning("Beberapa data mungkin tidak lengkap.")
st.error("Tidak ditemukan data pada filter yang dipilih.")

# 14. Charts
st.header("13. Visualisasi Data")
st.subheader("Line Chart - Tren Kasus Konflik")
chart_data = pd.DataFrame(
    np.random.randint(0, 20, size=(10, 3)), columns=["Intoleransi", "Regulasi Diskriminatif", "Kekerasan"]
)
st.line_chart(chart_data)

st.subheader("Bar Chart - Kasus per Wilayah")
bar_data = pd.DataFrame(
    np.random.randint(1, 50, size=(5, 2)), columns=["Jawa Barat", "Jawa Timur"]
)
st.bar_chart(bar_data)

st.subheader("Area Chart - Intensitas Kasus")
area_data = pd.DataFrame(
    np.random.randint(0, 20, size=(10, 3)), columns=["Aktor Negara", "Ormas", "Masyarakat"]
)
st.area_chart(area_data)

st.subheader("Scatter Plot - Hubungan Faktor Sosial")
x = np.random.randn(100)
y = np.random.randn(100)
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5)
ax.set_xlabel("Indeks Toleransi")
ax.set_ylabel("Jumlah Konflik")
st.pyplot(fig)

# 15. Dataframes and Descriptive Statistics
st.header("14. Dataframe & Statistik Deskriptif")
data = {
    'Tahun': np.random.randint(2000, 2025, 10),
    'Kasus': np.random.randint(1, 100, 10),
    'Kategori': np.random.choice(['Intoleransi', 'Diskriminasi', 'Kekerasan'], 10)
}
df = pd.DataFrame(data)

st.subheader("Tabel Data")
st.dataframe(df)

st.subheader("Statistik Deskriptif")
st.write(df.describe())
