import streamlit as st
import yfinance as yf
import feedparser
import urllib.parse

st.title("🚀 Live Automated Macro Dashboard")

# ------------------------------------------------------
# STEP 1: FETCH LIVE MARKET DATA (FREE)
# ------------------------------------------------------
st.subheader("📊 Live Sector Top Performers (Real-Time)")

# Our target pool of Indian cooling stocks
cooling_tickers = ["AMBER.NS", "VOLTAS.NS", "BLUESTARCO.NS", "SUBROS.NS", "HINDCOPPER.NS"]

live_data = []

with st.spinner("Fetching live stock prices from Yahoo Finance..."):
    for ticker in cooling_tickers:
        # yfinance fetches real-time data for free
        stock = yf.Ticker(ticker)
        history = stock.history(period="2d") # Get today and yesterday
        
        if len(history) >= 2:
            close_today = history['Close'].iloc[-1]
            close_yesterday = history['Close'].iloc[-2]
            # Calculate daily percentage change
            pct_change = ((close_today - close_yesterday) / close_yesterday) * 100
            
            live_data.append({
                "Ticker": ticker,
                "Live Price (₹)": round(close_today, 2),
                "Daily Change (%)": round(pct_change, 2)
            })

# Sort the stocks automatically so the top performer is always at the top!
df = pd.DataFrame(live_data)
df = df.sort_values(by="Daily Change (%)", ascending=False)

st.dataframe(df, use_container_width=True, hide_index=True)

# ------------------------------------------------------
# STEP 2: FETCH LIVE MACRO NEWS (FREE)
# ------------------------------------------------------
st.subheader("📰 Live Macro Event Evidence")

# We build a custom Google News search URL for free RSS tracking
search_query = "India heatwave power demand"
encoded_query = urllib.parse.quote(search_query)
rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"

with st.spinner("Scanning live global news feeds..."):
    feed = feedparser.parse(rss_url)
    
    # Take the top 3 most recent news articles
    for entry in feed.entries[:3]:
        st.markdown(f"**[{entry.title}]({entry.link})**")
        st.caption(f"Published: {entry.published}")
        st.write("---")
