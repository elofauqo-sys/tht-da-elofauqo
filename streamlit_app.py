import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("🚖 Sigma Cabs Dataset Viewer")

# Deskripsi singkat
st.markdown("""
Dataset **Sigma Cabs** berisi informasi terkait perjalanan pelanggan taksi daring, 
mulai dari jarak perjalanan, tipe taksi, lama menjadi pelanggan, hingga pola gaya hidup.  
Data ini digunakan untuk menganalisis faktor-faktor yang memengaruhi **terjadinya surge pricing (kenaikan harga taksi)**.
""")

# Baca dataset
df = pd.read_csv("data/sigma_cabs_clean.csv")

# Tampilkan dataframe
st.subheader("📊 Preview Dataset Sigma Cabs (5 Baris Pertama)")
st.dataframe(df.head(), use_container_width=True)

# Info singkat dataset
st.markdown(f"""
**Jumlah Baris:** {df.shape[0]}  
**Jumlah Kolom:** {df.shape[1]}
""")


#  Statistik Deskriptif
st.subheader("📈 Statistik Deskriptif")
st.write(df.describe())

# Distribusi Data Numerik
st.subheader("📊 Distribusi Fitur Numerik")
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

selected_num = st.selectbox("Pilih kolom numerik:", num_cols)
fig, ax = plt.subplots()
sns.histplot(df[selected_num], kde=True, ax=ax)
ax.set_title(f"Distribusi dari {selected_num}")
st.pyplot(fig)

#  Distribusi Data Kategorikal
st.subheader("🧩 Distribusi Fitur Kategorikal")
cat_cols = df.select_dtypes(include=['object']).columns.tolist()

if len(cat_cols) > 0:
    selected_cat = st.selectbox("Pilih kolom kategorikal:", cat_cols)
    fig, ax = plt.subplots()
    sns.countplot(x=df[selected_cat], palette="Set2", ax=ax)
    ax.set_title(f"Distribusi dari {selected_cat}")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("Tidak ada kolom kategorikal di dataset.")


# Korelasi antar Fitur Numerik
st.subheader("🔗 Korelasi Antar Fitur Numerik")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="Blues", ax=ax)
st.pyplot(fig)

# ===============================
# 📊 EDA: Faktor yang Mempengaruhi Surge Pricing
# ===============================

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("🚕 Analisis Faktor yang Mempengaruhi Surge Pricing")

# Pastikan dataset sudah dibaca sebelumnya sebagai df
if 'df' in locals() or 'df' in globals():
    st.subheader("📈 Distribusi Tipe Surge Pricing")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(data=df, x='Surge_Pricing_Type', palette='viridis', ax=ax)
    plt.title("Distribusi Kenaikan Harga (Surge Pricing)")
    st.pyplot(fig)

    # 1️⃣ Jarak perjalanan vs surge pricing
    st.subheader("📏 Hubungan Trip Distance dengan Surge Pricing")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.boxplot(data=df, x='Surge_Pricing_Type', y='Trip_Distance', palette='Blues', ax=ax)
    plt.title("Trip Distance berdasarkan Surge Pricing")
    st.pyplot(fig)

    # 2️⃣ Jenis taksi vs surge pricing
    st.subheader("🚖 Jenis Taksi dan Surge Pricing")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(data=df, x='Type_of_Cab', y='Surge_Pricing_Type', estimator='mean', palette='Oranges', ax=ax)
    plt.title("Rata-rata Surge Pricing berdasarkan Jenis Taksi")
    st.pyplot(fig)

    # 3️⃣ Lokasi tujuan vs surge pricing
    st.subheader("📍 Lokasi Tujuan dan Surge Pricing")
    if 'Destination_Type' in df.columns:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.barplot(data=df, x='Destination_Type', y='Surge_Pricing_Type', estimator='mean', palette='coolwarm', ax=ax)
        plt.title("Rata-rata Surge Pricing berdasarkan Lokasi Tujuan")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'Destination_Type' tidak ditemukan di dataset.")

    # 4️⃣ Pembatalan dan surge pricing
    st.subheader("❌ Pembatalan Pesanan dan Surge Pricing")
    if 'Cancellation_Last_1Month' in df.columns:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.scatterplot(data=df, x='Cancellation_Last_1Month', y='Surge_Pricing_Type', color='red', ax=ax)
        plt.title("Hubungan Pembatalan dengan Surge Pricing")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'Cancellation_Last_1Month' tidak ditemukan di dataset.")
else:
    st.warning("⚠️ Dataset belum dimuat. Pastikan file 'sigma_cabs_clean.csv' sudah diunggah dan dibaca terlebih dahulu.")

    # ===============================
# 🚕 Analisis Hubungan Trip Distance dengan Surge Pricing
# ===============================

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

st.header("📏 Hubungan antara Jarak Perjalanan (Trip Distance) dan Tipe Surge Pricing")

# Pastikan dataset sudah dimuat
if 'df' in locals() or 'df' in globals():
    # --- Statistik ringkas
    st.subheader("📊 Statistik Ringkas")
    st.write(df[['Trip_Distance', 'Surge_Pricing_Type']].describe())

    # --- Distribusi jarak per surge pricing
    st.subheader("🎯 Distribusi Trip Distance per Tipe Surge Pricing")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(data=df, x='Surge_Pricing_Type', y='Trip_Distance', palette='viridis', ax=ax)
    plt.title("Distribusi Jarak Perjalanan Berdasarkan Tipe Surge Pricing")
    plt.xlabel("Tipe Surge Pricing")
    plt.ylabel("Jarak Perjalanan (km)")
    st.pyplot(fig)

    # --- Scatter plot untuk melihat pola
    st.subheader("💡 Pola Jarak vs Tipe Surge Pricing")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.stripplot(data=df, x='Surge_Pricing_Type', y='Trip_Distance', jitter=True, alpha=0.6, palette='cool', ax=ax)
    plt.title("Sebaran Data Trip Distance pada Tiap Tipe Surge Pricing")
    plt.xlabel("Tipe Surge Pricing")
    plt.ylabel("Jarak Perjalanan (km)")
    st.pyplot(fig)

    # --- Insight
    st.markdown("""
    ### ✨ Insight:
    - Terlihat bahwa **semakin panjang jarak perjalanan**, kecenderungan untuk mengalami **surge pricing** cenderung meningkat.
    - Tipe surge pricing yang lebih tinggi biasanya memiliki **median trip distance yang lebih besar**.
    - Artinya, jarak perjalanan menjadi salah satu faktor penting dalam memengaruhi kenaikan harga.
    """)
else:
    st.warning("⚠️ Dataset belum dimuat. Pastikan file `sigma_cabs_clean.csv` sudah diunggah dan dibaca terlebih dahulu.")

