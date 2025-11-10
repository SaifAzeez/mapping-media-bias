from dotenv import load_dotenv
import os
import pandas as pd
import requests

# Load the .env file
load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

# key words 
query = "Israel Palestine"
sources = "bbc-news,cnn,al-jazeera-english,fox-news,the-guardian-uk"
url = f"https://newsapi.org/v2/everything?q={query}&sources={sources}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()
articles = data.get("articles", [])

df = pd.DataFrame([{
    "source": a["source"]["name"],
    "title": a["title"],
    "description": a["description"],
    "content": a["content"],
    "url": a["url"],
    "publishedAt": a["publishedAt"]
} for a in articles])

df.to_csv("data/sample_articles.csv", index=False)
print("Saved sample_articles.csv with", len(df), "articles")
