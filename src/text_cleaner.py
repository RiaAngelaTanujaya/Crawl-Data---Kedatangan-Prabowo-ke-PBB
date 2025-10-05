import re

# Daftar kata umum (stopwords) yang diabaikan dalam analisis
STOPWORDS = set([
    "yang", "dan", "di", "ke", "dari", "untuk", "ini", "itu", "dengan", "pada",
    "karena", "sebagai", "adalah", "ya", "nya", "lah", "deh", "dong", "sih",
    "gak", "ga", "tidak", "bukan", "aja", "kok", "pun", "jadi", "kalo", "kalau",
    "kan", "dah", "udah", "emang", "atau", "sama", "nih", "tuh", "punya",
    "udah", "lagi", "baik", "jadi", "aja", "gua", "gue", "aku", "saya", "yg", "bisa", "seperti"
])

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Bersihkan simbol, URL, tanda baca
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Pisahkan kata & buang stopwords
    words = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
    return " ".join(words)
