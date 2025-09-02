# app.py
import streamlit as st
import requests
import datetime

st.set_page_config(page_title="📰 AI News Agent", layout="wide")

left, center, right = st.columns([2, 6, 2])

with center:
    st.title("🤖 AI News Agent")
    st.markdown("Get **summarized, sentiment-tagged news** by selecting a location/date or searching for the incident.")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Input section
    location = st.text_input("🌍 Enter Location (e.g., Delhi, USA)")
    category = st.selectbox("📂 Select Category", 
                            [ "Custom", "General", "World", "Nation", "Business", "Technology", 
                            "Entertainment", "Sports", "Science", "Health"])

    custom_query = ""
    if category == "Custom":
        custom_query = st.text_input("✍️ Enter custom incident/topic (e.g., 'earthquake in Turkey')")

    start_date = st.date_input("📅 Start Date", datetime.date.today())
    end_date = st.date_input("📅 End Date", datetime.date.today())

    if st.button("🔎 Get News"):
        if location or (category == "custom" and custom_query):
            with st.spinner("🔎 Fetching and summarizing news... Please wait."):
                response = requests.get(
        f"http://127.0.0.1:8000/get_news/?location={location}&start_date={start_date}&end_date={end_date}&category={category}&custom_query={custom_query}"
    ).json()


            news_items = response.get("news", [])

            bot_reply = f"### 📰 News Digest ({start_date} → {end_date}) | Category: {category}\n\n"
            for i, item in enumerate(news_items, 1):
                emoji = "😊" if "POSITIVE" in item['sentiment'] else "😞" if "NEGATIVE" in item['sentiment'] else "😐"
                bot_reply += f"**{i}. {item['title']}** ({emoji} {item['sentiment']})\n\n"
                bot_reply += f"{item['summary']}\n\n[Read more]({item['url']})\n\n"

            query_display = custom_query if category == "custom" else f"{location} news"
            st.session_state["messages"].append(("user", f"{query_display} from {start_date} to {end_date}"))
            st.session_state["messages"].append(("bot", bot_reply))

    # Display chat history with bubble style
    for role, msg in st.session_state["messages"]:
        if role == "user":
            st.markdown(f"<div style='background:#light-grey;padding:10px;border-radius:10px;margin:5px'><b>🧑 You:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background:#grey;padding:10px;border-radius:10px;margin:5px'>{msg}</div>", unsafe_allow_html=True)



