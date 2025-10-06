# Laporan Analisis YouTube Comments & Video

Kedatangan Menteri Pertahanan Indonesia, Prabowo Subianto, ke Sidang Umum Perserikatan Bangsa-Bangsa (PBB) menjadi sorotan media dan publik. Isu ini memunculkan berbagai opini di media sosial, khususnya di platform YouTube, di mana penonton memberikan komentar yang beragam: mendukung, netral, atau bahkan kritis.
- - -
Analisis komentar YouTube terkait topik ini memberikan insight mengenai persepsi publik, tren opini, dan tingkat interaksi penonton terhadap isu politik berskala internasional. Informasi ini dapat digunakan untuk:
- Memahami reaksi masyarakat secara keseluruhan terhadap kedatangan Prabowo.
- Mengidentifikasi konten atau komentar yang viral dan memengaruhi opini publik.
- Memberikan wawasan bagi analis politik dan media terkait sentimen dan engagement masyarakat.
- - - 
Analisis yang Dilakukan
1. Distribusi Sentimen Komentar
- Setiap komentar dikategorikan menjadi positif, netral, atau negatif menggunakan analisis sentimen berbasis teks.
- Tujuannya untuk memahami persepsi publik secara keseluruhan terhadap isu kedatangan Prabowo ke PBB.

2. Top Video berdasarkan Jumlah Komentar
- Mengidentifikasi video yang paling banyak dikomentari, sehingga menunjukkan video paling menarik perhatian publik.

3. Top Komentar berdasarkan Like
- Menampilkan komentar yang paling disukai penonton, filter komentar promosi atau spam (misal: wd, garuda, hoki).
- Memberikan insight tentang opini atau pernyataan yang dianggap penting atau populer.

4. Distribusi Komentar per Channel
- Menunjukkan channel mana yang paling banyak menarik komentar terkait isu ini.
- Berguna untuk melihat platform atau influencer yang mempengaruhi opini publik.

5. Sebaran Like Count Komentar  
Histogram like menunjukkan bahwa mayoritas komentar memiliki like rendah, sedangkan komentar populer sedikit membentuk ekor panjang. Ini mengindikasikan bahwa opini yang viral bersifat terbatas, tetapi berdampak signifikan.

6. Trend Sentimen dari Waktu ke Waktu  
Melacak perubahan jumlah komentar positif, netral, dan negatif setiap hari selama periode tertentu. Bisa digunakan untuk melihat reaksi publik terhadap liputan berita atau pernyataan resmi.

7. Word Frequency (Global) dan Top Words per Sentiment  
Word cloud global menampilkan kata yang paling sering muncul. Word cloud per sentimen (positif, netral, negatif) membantu mengidentifikasi topik yang dominan di tiap kategori opini.

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

