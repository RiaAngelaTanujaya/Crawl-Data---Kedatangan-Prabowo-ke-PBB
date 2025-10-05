# Laporan Analisis YouTube Comments & Video

Proyek ini bertujuan menganalisis komentar dan statistik video YouTube secara keseluruhan, menggunakan data komentar, data video, dan tren sentimen dari waktu ke waktu. Analisis dilakukan untuk memahami pola interaksi pengguna, sentimen, dan konten yang populer.

---

## 1. Distribusi Sentimen Komentar

- Komentar mayoritas bersifat **netral**, diikuti oleh positif, dan sedikit negatif.  
- Hal ini menunjukkan sebagian besar penonton memberi komentar yang informatif atau biasa, sementara komentar viral cenderung positif atau negatif ekstrem.  

*(Ditampilkan di dashboard dengan bar chart distribusi sentimen.)*

---

## 2. Top 10 Video berdasarkan Jumlah Komentar

- Video dengan komentar terbanyak biasanya **video populer atau trending**.  
- Informasi ini membantu mengidentifikasi konten yang menarik perhatian penonton.

---

## 3. Top 10 Komentar dengan Like Terbanyak

- Komentar paling populer biasanya **menarik interaksi tinggi**, misal pertanyaan penting atau opini unik.  
- Komentar promosi atau konten tertentu seperti judol (misal `wd`, `garuda`, `hoki`) sudah **difilter** agar fokus pada komentar yang organik.

---

## 4. Distribusi Komentar per Channel

- Beberapa channel menerima **lebih banyak komentar**, menunjukkan basis penggemar aktif.  
- Analisis ini dapat membantu memahami engagement tiap channel.

---

## 5. Sebaran Like Count Komentar

- Sebagian besar komentar memiliki **like rendah (0–50)**.  
- Komentar viral sangat sedikit → distribusi miring ke kanan (right-skewed).  
- Beberapa komentar sangat populer membentuk **ekor panjang** di histogram.

---

## 6. Tren Sentimen dari Waktu ke Waktu

- Line chart menunjukkan perubahan jumlah komentar positif, netral, dan negatif setiap hari.  
- Dapat membantu melihat **momentum video viral** atau reaksi penonton terhadap kejadian tertentu.

---

## 7. Word Frequency (Global)

- Word cloud global menunjukkan kata-kata yang paling sering muncul di seluruh komentar.  
- Memberikan insight tentang topik atau istilah yang sering dibahas penonton.

---

## 8. Top Words per Sentiment

- Word cloud per sentimen (positif, netral, negatif) menampilkan kata yang sering muncul dalam masing-masing kategori.  
- Membantu memahami **karakteristik komentar positif vs negatif**.

---

## 9. Kesimpulan

- Mayoritas komentar bersifat netral dengan like rendah.  
- Komentar viral atau populer sangat sedikit tapi memiliki dampak tinggi.  
- Trend sentimen, distribusi kata, dan engagement per channel memberikan insight berguna untuk strategi konten dan memahami audiens.  
- Dashboard ini memudahkan **explorasi data interaktif**, baik untuk konten creator maupun analis.

---

## 10. Tools & Library

- **Python 3.10+**  
- **Streamlit**: untuk dashboard interaktif  
- **Pandas**: manipulasi data  
- **Matplotlib & Seaborn**: visualisasi  
- **WordCloud**: visualisasi kata
