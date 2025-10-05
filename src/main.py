import json
from src.youtube_crawler import crawl_videos
from src.youtube_comments import crawl_all_comments
from src.sentiment_analysis import process_comments

def main():
    # Baca API key dan settings
    with open("config/api_settings.json") as f:
        api_key = json.load(f)["YOUTUBE_API_KEY"]

    with open("config/settings.json") as f:
        settings = json.load(f)

    # Daftar keyword untuk pencarian video
    search_keywords = [
        "Prabowo PBB",
        "Prabowo pidato PBB",
        "Prabowo di sidang PBB",
        "Pidato Prabowo Subianto",
        "Prabowo Subianto UN speech",
        "Kedatangan Prabowo ke sidang PBB"
    ]

    raw_path = "data/raw_json"
    csv_videos = "data/master_csv/videos.csv"
    csv_comments = "data/master_csv/comments.csv"
    csv_comments_analyzed = "data/master_csv/comments_analyzed.csv"
    csv_word_freq = "data/master_csv/word_freq.csv"
    img_wordcloud = "data/visualizations/wordcloud.png"
    csv_sentiment_trend = "data/master_csv/sentiment_trend.csv"

    # 1️⃣ Crawl video
    videos = []
    for query in search_keywords:
        print(f"\n🔍 Crawling video untuk keyword: {query}")
        vids = crawl_videos(api_key, query, raw_path, csv_videos)
        videos.extend(vids)

    # 2️⃣ Crawl komentar
    crawl_all_comments(api_key, videos, raw_path, csv_comments)

    # 3️⃣ Analisis sentimen, wordcloud, dan tren
    process_comments(
        csv_comments,
        csv_comments_analyzed,
        csv_word_freq,
        img_wordcloud,
        csv_sentiment_trend
    )

if __name__ == "__main__":
    main()
