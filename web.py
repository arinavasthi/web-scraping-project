# web.py
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import csv
import time

load_dotenv()
def scrape_profile_sequential_optimized(username, max_tweets=5, csv_filename="tweets.csv"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(f"https://twitter.com/{username}", timeout=60000)
        time.sleep(5)  # Let tweets load

        tweets = page.query_selector_all("article")

        tweet_texts = []
        for tweet in tweets[:max_tweets]:
            try:
                text = tweet.inner_text()
                tweet_texts.append(text)
            except Exception:
                continue

        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Tweet"])
            for tweet in tweet_texts:
                writer.writerow([tweet])

        print(f"✅ {len(tweet_texts)} tweets saved to {csv_filename}")
        browser.close()

if __name__ == "__main__":
    username = "elonmusk"  # change this to any username
    max_tweets = 5
    csv_filename = f"{username}_tweets.csv"

    scrape_profile_sequential_optimized(username, max_tweets, csv_filename)
