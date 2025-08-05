# main.py
import csv
from crewai import Crew
from agents import get_tasks
from web import scrape_profile_sequential_optimized
from dotenv import load_dotenv
load_dotenv()

def load_tweets_from_csv(csv_filename):
    tweets = []
    with open(csv_filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tweets.append(row["Tweet"])
    return "\n\n".join(tweets)

if __name__ == "__main__":
    username = "elonmusk"
    max_tweets = 5
    csv_filename = f"{username}_tweets.csv"

    scrape_profile_sequential_optimized(username, max_tweets, csv_filename)
    tweet_data = load_tweets_from_csv(csv_filename)

    tasks = get_tasks(tweet_data)
    crew = Crew(tasks=tasks)
    result = crew.kickoff()

    print("\n📝 Summary and Suggestions:\n")
    print(result)
