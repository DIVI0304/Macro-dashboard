import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 1. Define your data (You can expand these lists)
sector_data = {
    "IT": ["TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS"],
    "Banking": ["HDFCBANK.NS", "ICICIBANK.NS", "AXISBANK.NS", "SBIN.NS", "KOTAKBANK.NS"],
    "Energy": ["RELIANCE.NS", "TATAPOWER.NS", "NTPC.NS", "ONGC.NS", "ADANIGREEN.NS"]
}

st.set_page_config(page_title="India Market Dashboard", layout="wide")

st.title("📈 Indian Stock Market Interactive Dashboard")

# 2. Sidebar Flow
st.sidebar.header("Navigation")
exchange = st.sidebar.radio("Select Exchange", ["NSE", "BSE"])
selected_sector = st.sidebar.selectbox("Select Sector", list(sector_data.keys()))

# 3. Logic to show Top 10 (or available) stocks in that sector
st.subheader(f"Top Picks: {selected_sector} Sector")
tickers = sector_data[selected_sector]

# Display a table with basic info
selected_stock = st.selectbox("Select a stock to view detailed analysis:", tickers)

# 4. Detailed View
if selected_stock:
    stock = yf.Ticker(selected_stock)
    info = stock.info
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Current Price", f"₹{info.get('currentPrice', 'N/A')}")
        st.write(f"**Company:** {info.get('longName')}")
        st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}")
        st.write(f"**P/E Ratio:** {info.get('trailingPE', 'N/A')}")

    with col2:
        # Interactive Chart
        hist = stock.history(period="1mo")
        fig = go.Figure(data=[go.Candlestick(x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close'])])
        fig.update_layout(title="Last 1 Month Performance", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("View Full Financials"):
        st.json(info)
