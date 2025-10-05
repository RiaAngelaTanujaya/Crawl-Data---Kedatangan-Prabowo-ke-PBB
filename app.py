import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Dashboard Analisis YouTube Comments & Video")

# =========================
# Load CSV
# =========================
data_folder = os.path.join("data", "master_csv")
comments = pd.read_csv(os.path.join(data_folder, "comments.csv"))
comments_analyzed = pd.read_csv(os.path.join(data_folder, "comments_analyzed.csv"))
videos = pd.read_csv(os.path.join(data_folder, "videos.csv"))
sentiment_trend = pd.read_csv(os.path.join(data_folder, "sentiment_trend.csv"))
word_freq = pd.read_csv(os.path.join(data_folder, "word_freq.csv"))

# =========================
# Merge menjadi master_df
# =========================
master_df = comments_analyzed.merge(
    videos[['video_id','title','channelTitle']], 
    on='video_id', how='left'
)

# =========================
# Hapus duplikat komentar (berdasarkan author + text)
# =========================
master_df = master_df.drop_duplicates(subset=['author','text'])

# =========================
# 1. Distribusi Sentimen
# =========================
st.subheader("Distribusi Sentimen Komentar")
sentiment_counts = master_df['sentiment'].value_counts()
st.bar_chart(sentiment_counts)

# =========================
# 2. Top 10 Video by Comment Count
# =========================
st.subheader("Top 10 Video dengan Komentar Terbanyak")
top_videos_comments = master_df.groupby('title')['text'].count().sort_values(ascending=False).head(10)
st.bar_chart(top_videos_comments)

# =========================
# 3. Top 10 Komentar by Likes (Unique) - Filtered
# =========================
st.subheader("Top 10 Komentar dengan Like Terbanyak (Unique, Filtered)")

# Daftar kata/keyword yang ingin diexclude (case insensitive)
exclude_keywords = ['wd','garuda','hoki', 'modal', 'betah', '20k', 'energi','wueedeh' ]

# Buat mask: komentar yang **tidak mengandung** keyword
mask = ~master_df['text'].str.lower().str.contains('|'.join(exclude_keywords))

# Terapkan filter
filtered_top_comments = master_df[mask][['author','text','like_count','title']]

# Ambil top 10 berdasarkan like_count
top_comments = filtered_top_comments.sort_values('like_count', ascending=False).head(10)
st.dataframe(top_comments)
# =========================
# 4. Distribusi Komentar per Channel
# =========================
st.subheader("Distribusi Komentar per Channel")
channel_counts = master_df.groupby('channelTitle')['text'].count().sort_values(ascending=False).head(10)
st.bar_chart(channel_counts)

# =========================
# 5. Sebaran Like Count
# =========================
st.subheader("Sebaran Like Count Komentar")
fig, ax = plt.subplots(figsize=(10,5))
sns.histplot(master_df['like_count'], bins=30, kde=True, ax=ax)
ax.set_xlabel("Like Count")
ax.set_ylabel("Jumlah Komentar")
st.pyplot(fig)

# =========================
# 6. Trend Sentimen dari Waktu ke Waktu
# =========================
st.subheader("Trend Sentimen dari Waktu ke Waktu")
sentiment_trend['date'] = pd.to_datetime(sentiment_trend['date'])
trend_data = sentiment_trend.set_index('date')[['negative','neutral','positive']]
st.line_chart(trend_data)

# =========================
# 7. Word Frequency
# =========================
st.subheader("Word Frequency")
word_freq_dict = dict(zip(word_freq['word'], word_freq['frequency']))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq_dict)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# =========================
# 8. Top Words by Sentiment
# =========================
st.subheader("Top Words per Sentiment")

sentiments = ['positive','neutral','negative']

for s in sentiments:
    st.write(f"**Word Cloud - {s.capitalize()} Comments**")
    comments_text = master_df[master_df['sentiment'] == s]['clean_text'].dropna().str.cat(sep=' ')
    if comments_text:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(comments_text)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.write(f"Tidak ada komentar {s} untuk word cloud.")