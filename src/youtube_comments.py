import os
import csv
import json
from googleapiclient.discovery import build

def crawl_all_comments(api_key, videos, raw_path, csv_path, max_comments_per_video=200):
    youtube = build("youtube", "v3", developerKey=api_key)
    all_comments = []
    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    for vid in videos:
        video_id = vid["video_id"]
        print(f"💬 Crawling komentar untuk video {video_id}")
        comments = []
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText"
        )
        response = request.execute()

        while response:
            for item in response["items"]:
                snippet = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "video_id": video_id,
                    "author": snippet.get("authorDisplayName", ""),
                    "text": snippet.get("textDisplay", ""),
                    "like_count": snippet.get("likeCount", 0),
                    "published_at": snippet.get("publishedAt", "")
                })
                if len(comments) >= max_comments_per_video:
                    break
            if "nextPageToken" in response and len(comments) < max_comments_per_video:
                response = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    pageToken=response["nextPageToken"],
                    maxResults=100,
                    textFormat="plainText"
                ).execute()
            else:
                break

        with open(f"{raw_path}/comments_{video_id}.json", "w", encoding="utf-8") as f:
            json.dump(comments, f, indent=2, ensure_ascii=False)

        all_comments.extend(comments)

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["video_id", "author", "text", "like_count", "published_at"])
        writer.writeheader()
        writer.writerows(all_comments)

    print(f"✅ Total komentar disimpan: {len(all_comments)}")
