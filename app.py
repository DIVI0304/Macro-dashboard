import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 1. ADD CACHING: This tells Streamlit to save the data for 1 hour
# This prevents constant re-fetching.
@st.cache_data(ttl=3600) 
def get_stock_details(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    # Fetching history and info together
    hist = stock.history(period="1mo")
    info = stock.info
    return info, hist

# 3. ADD ERROR HANDLING: Use a try-except block
if selected_stock:
    try:
        # Call the cached function
        info, hist = get_stock_details(selected_stock)
        
        # Display logic...
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Price", f"₹{info.get('currentPrice', 'N/A')}")
            # ... (rest of your display code)
            
        with col2:
            fig = go.Figure(data=[go.Candlestick(x=hist.index, ...)])
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error("Could not fetch data from Yahoo Finance right now. Please try again in a few minutes.")
        st.write("Reason:", e)
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
        
        # We define the Candlestick chart fully here
        fig = go.Figure(data=[go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close']
        )])
        
        # Configure layout
        fig.update_layout(
            title="Last 1 Month Performance", 
            xaxis_rangeslider_visible=False,
            height=400
        )
        
        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
    with st.expander("View Full Financials"):
        st.json(info)
