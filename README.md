# 🚖 Sigma Cabs Dataset Viewer
<img src = "https://c.pxhere.com/photos/71/59/photo-422905.jpg!d">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fictional-capybara-v67wwj99jrvq2666-8501.app.github.dev/)

## 📌 Project Overview

Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi kenaikan harga (Surge Pricing) pada layanan taksi Sigma Cabs.
Analisis ini dilakukan menggunakan teknik Exploratory Data Analysis (EDA) dan visualisasi interaktif (via Python/Streamlit) untuk memahami pola harga, perilaku pelanggan, dan karakteristik perjalanan.

## 🎯 Objectives

Mengidentifikasi faktor utama yang memengaruhi terjadinya surge pricing.

Menganalisis hubungan antara jarak perjalanan, tipe taksi, dan lokasi tujuan terhadap surge pricing.

Memberikan insight berbasis data untuk optimalisasi strategi harga dan operasional armada.

Membuat visualisasi interaktif untuk mendukung proses pengambilan keputusan.

## 🧠 Dataset Description

Nama Dataset: sigma_cabs_clean.csv

Dataset ini berisi informasi mengenai perjalanan pelanggan, karakteristik pengguna, dan kondisi harga dinamis.

Variabel	Deskripsi
Trip_Distance	Jarak perjalanan pelanggan (dalam km)
Customer_Since_Months	Lama pelanggan menggunakan layanan (bulan)
Life_Style_Index	Indeks gaya hidup pelanggan
Customer_Rating	Rating yang diberikan pelanggan
Cancellation_Last_1Month	Jumlah pembatalan dalam 1 bulan terakhir
Type_of_Cab	Jenis taksi yang digunakan
Destination_Type	Kategori lokasi tujuan
Surge_Pricing_Type	Jenis kenaikan harga (1 = normal, 2 = sedang, 3 = tinggi)

## 🔍 Data Understanding

Dataset mencakup 30 kolom yang berisi data numerik dan kategorikal.
Beberapa langkah awal yang dilakukan:

- Mengecek missing value dan duplikasi data.
- Melihat distribusi data tiap variabel.
- Melakukan encoding pada fitur kategorikal seperti Type_of_Cab dan Destination_Type.
- Menentukan variabel target: Surge_Pricing_Type.

## 📊 Exploratory Data Analysis (EDA)

Analisis dilakukan untuk menjawab beberapa pertanyaan utama:

1️⃣ Faktor apa saja yang memengaruhi surge pricing?
Korelasi menunjukkan beberapa faktor penting:
- Trip Distance (0.28) → Semakin jauh jarak perjalanan, peluang surge pricing meningkat.
- Cancellation_Last_1Month (0.19) → Pelanggan dengan pembatalan tinggi cenderung mengalami harga lebih tinggi.
- Customer_Rating (-0.14) → Rating rendah sedikit berhubungan dengan harga lebih tinggi.
  
2️⃣ Bagaimana hubungan antara jarak perjalanan dengan surge pricing?
- Visualisasi boxplot menunjukkan tren kenaikan surge pricing seiring peningkatan jarak perjalanan.
  
3️⃣ Apakah jenis taksi tertentu lebih sering mengalami surge pricing?
- Jenis taksi Type D dan E menunjukkan rata-rata surge pricing lebih tinggi dibandingkan lainnya — kemungkinan karena segmentasi premium atau permintaan tinggi.
  
4️⃣ Apakah lokasi pelanggan (Destination Type) memengaruhi surge pricing?
- Ya — beberapa destination type (seperti D, G, H) cenderung mengalami surge lebih sering, mengindikasikan permintaan tinggi pada area tersebut.
  
5️⃣ Apakah pembatalan pesanan berpengaruh terhadap surge pricing?
- Pelanggan dengan frekuensi pembatalan tinggi dalam 1 bulan terakhir lebih mungkin terkena kenaikan harga dinamis.

## 🧩 Insights Summary

1. Jarak perjalanan dan tipe taksi merupakan faktor paling dominan terhadap kenaikan harga.
2. Lokasi tujuan dan riwayat pembatalan turut berperan dalam pembentukan harga.
3. Data menunjukkan adanya pola surge pricing konsisten di area tertentu.
4. Pelanggan baru atau jarang menggunakan layanan cenderung lebih sering mengalami harga tinggi.

## 💡 Business Recommendations

1. Optimasi Sistem Surge Pricing
Terapkan model prediktif berbasis data untuk menentukan harga lebih akurat.
2. Penyebaran Armada yang Efisien
Tambah jumlah armada di area permintaan tinggi atau waktu sibuk.
3. Transparansi Harga untuk Pelanggan
Tampilkan alasan kenaikan harga secara jelas untuk menjaga kepercayaan.
4. Program Loyalitas Pelanggan
Berikan promo/diskon untuk pelanggan loyal atau dengan pembatalan rendah.
5. Monitoring & Evaluasi Rutin
Gunakan dashboard analitik (mis. Streamlit) untuk evaluasi surge pricing berkala.

## 🧰 Tools & Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn, Streamlit)
- Jupyter Notebook
- Power BI / Streamlit Dashboard
- GitHub for Version Control
