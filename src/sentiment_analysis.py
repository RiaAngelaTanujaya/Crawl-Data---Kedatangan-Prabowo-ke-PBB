import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from datetime import date
from src.text_cleaner import clean_text
import nltk

# pastikan stopwords sudah tersedia
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('indonesian')) | set(stopwords.words('english'))

def analyze_sentiment(text):
    """Analisis sentimen sederhana berdasarkan polaritas TextBlob."""
    if not isinstance(text, str):
        return "neutral"
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "positive"
    elif analysis.sentiment.polarity < -0.1:
        return "negative"
    return "neutral"

def process_comments(input_csv, output_csv, word_freq_csv, wordcloud_img, trend_csv):
    # Baca data komentar
    df = pd.read_csv(input_csv)

    # Pastikan kolom teks ada
    if "text" not in df.columns:
        raise ValueError(f"Kolom 'text' tidak ditemukan. Kolom tersedia: {list(df.columns)}")

    # Bersihkan teks komentar
    df["clean_text"] = df["text"].astype(str).apply(clean_text)

    # Hapus baris kosong setelah dibersihkan
    df = df[df["clean_text"].str.strip() != ""]

    # Analisis sentimen
    df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

    # Simpan hasil analisis
    df.to_csv(output_csv, index=False)

    # === Word frequency ===
    all_words = " ".join(df["clean_text"]).lower().split()
    filtered_words = [w for w in all_words if w not in stop_words and len(w) > 2]
    word_freq = Counter(filtered_words).most_common(100)

    # Simpan hasil frekuensi kata
    pd.DataFrame(word_freq, columns=["word", "frequency"]).to_csv(word_freq_csv, index=False)

    # === WordCloud ===
    wc = WordCloud(
        width=800, height=400,
        background_color="white",
        colormap="tab10"
    ).generate_from_frequencies(dict(word_freq))

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(wordcloud_img)
    plt.close()

    # === Tren sentimen ===
    if "publishedAt" in df.columns:
        df["date"] = pd.to_datetime(df["publishedAt"], errors="coerce").dt.date
    elif "published_at" in df.columns:
        df["date"] = pd.to_datetime(df["published_at"], errors="coerce").dt.date
    else:
        df["date"] = date.today()  # fallback kalau kolom tanggal gak ada

    trend = df.groupby(["date", "sentiment"]).size().unstack(fill_value=0)
    trend.to_csv(trend_csv)

    print("✅ Sentimen, wordcloud, dan tren selesai dibuat.")
