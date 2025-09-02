# backend.py

from fastapi import FastAPI
import requests
from transformers import pipeline

app = FastAPI()

GNEWS_API_KEY = "0ab7871c731d9e6890a2b732a91cc50a"

# Summarization and Sentiment models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
sentiment_analyzer = pipeline("sentiment-analysis")

@app.get("/get_news/")
def get_news(location: str, start_date: str, end_date: str, category: str = "general", custom_query: str = ""):
    if category == "custom" and custom_query.strip() != "":
        # Use custom incident/topic entered by user
        query = custom_query
        url = f"https://gnews.io/api/v4/search?q={query}&from={start_date}&to={end_date}&lang=en&token={GNEWS_API_KEY}&max=10"
    elif category != "general":
        url = f"https://gnews.io/api/v4/top-headlines?category={category}&q={location}&lang=en&from={start_date}&to={end_date}&token={GNEWS_API_KEY}&max=10"
    else:
        url = f"https://gnews.io/api/v4/search?q={location}&from={start_date}&to={end_date}&lang=en&token={GNEWS_API_KEY}&max=10"

    response = requests.get(url).json()
    articles = response.get("articles", [])
    summaries = []

    for article in articles[:10]:
        content = article["title"] + ". " + (article.get("description") or "")
        if len(content.strip()) < 20:
            continue
        summary = summarizer(content, max_length=100, min_length=25, do_sample=False)[0]['summary_text']
        sentiment = sentiment_analyzer(summary)[0]

        summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"],
            "source": article["source"]["name"],
            "sentiment": sentiment["label"] + f" ({sentiment['score']:.2f})"
        })

    return {"news": summaries}
