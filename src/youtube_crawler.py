import os
import csv
import json
from googleapiclient.discovery import build

def crawl_videos(api_key, query, raw_path, csv_path, max_results=50):
    youtube = build("youtube", "v3", developerKey=api_key)
    videos = []

    request = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        maxResults=max_results,
        relevanceLanguage="id"
    )
    response = request.execute()

    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    with open(f"{raw_path}/videos_{query.replace(' ', '_')}.json", "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2, ensure_ascii=False)

    for item in response.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        published = item["snippet"]["publishedAt"]
        videos.append({"video_id": video_id, "title": title, "published": published})

    # Simpan ke CSV
    with open(csv_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["video_id", "title", "published"])
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerows(videos)

    return videos
