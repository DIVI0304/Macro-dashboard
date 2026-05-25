import streamlit as st
import pandas as pd

# ------------------------------------------------------
# 1. EXPANDED MOCK DATABASE (With News & Growth Plans)
# ------------------------------------------------------
macro_database = {
    "🔥 India Heatwave + Cooling Subsidy": {
        "thesis_map": "Extreme Temps ➔ AC Demand Spike ➔ Compressor Bottleneck ➔ Subsidy Boosts OEM Margins",
        # High-level table data
        "stocks": [
            {"Ticker": "AMBER.NS", "Company": "Amber Enterprises", "Supply Chain Role": "OEM/Component Mfg", "Action": "Top Pick"},
            {"Ticker": "VOLTAS.NS", "Company": "Voltas Ltd", "Supply Chain Role": "Consumer AC Brand", "Action": "Hold"},
            {"Ticker": "SUBROS.NS", "Company": "Subros Ltd", "Supply Chain Role": "Thermal Compressors", "Action": "Spec Buy"}
        ],
        # Deep-dive details for each company
        "deep_dives": {
            "AMBER.NS": {
                "news": [
                    "📰 [Economic Times] India's PLI scheme for AC components triggers manufacturing boost.",
                    "🔗 [Reuters] Component makers report record forward-orders ahead of peak summer."
                ],
                "financials": {
                    "Return on Equity (ROE)": "18.4%",
                    "Debt-to-Equity Ratio": "0.45 (Low Risk)",
                    "Net Profit Margin Growth": "+22% Year-over-Year",
                    "Cash Flow Status": "Free Cash Flow Positive"
                },
                "future_plans": "Building two new component mega-factories in South India to fulfill localized compressor demand and reduce reliance on Chinese imports by 2027."
            },
            "VOLTAS.NS": {
                "news": [
                    "📰 [Bloomberg] Voltas retains 20% market share in room AC segment amid rising competition.",
                    "🔗 [CNBC TV18] Consumer retail sales jump 35% in early Q1 heatwave."
                ],
                "financials": {
                    "Return on Equity (ROE)": "14.2%",
                    "Debt-to-Equity Ratio": "0.08 (Virtually Debt-Free)",
                    "Net Profit Margin Growth": "+11% Year-over-Year",
                    "Cash Flow Status": "Strong Cash Reserves"
                },
                "future_plans": "Expanding retail footprint into Tier-2 and Tier-3 Indian cities. Launching a new line of budget-friendly, ultra-energy-efficient smart ACs."
            },
            "SUBROS.NS": {
                "news": [
                    "📰 [MoneyControl] Subros expanding capacity for commercial cooling lines.",
                    "🔗 [Mint] Raw material costs squeeze short-term margins despite high demand."
                ],
                "financials": {
                    "Return on Equity (ROE)": "9.8%",
                    "Debt-to-Equity Ratio": "0.65 (Manageable)",
                    "Net Profit Margin Growth": "+5% Year-over-Year",
                    "Cash Flow Status": "Tight cash flow due to inventory build-up"
                },
                "future_plans": "Pivoting from purely automotive cooling to domestic AC compressor contracts to diversify revenue streams."
            }
        }
    }
}

# ------------------------------------------------------
# 2. DASHBOARD UI SETTINGS
# ------------------------------------------------------
st.set_page_config(page_title="Macro-to-Micro Screener", layout="wide")

st.title("🌍 Macro Catalyst & Supply Chain Screener")
st.markdown("Identify second and third-order market beneficiaries from global macroeconomic events.")
st.divider()

# ------------------------------------------------------
# 3. SIDEBAR (User Input)
# ------------------------------------------------------
st.sidebar.header("Select Catalyst")
selected_event = st.sidebar.selectbox(
    "Choose a Global Macro Event:",
    options=list(macro_database.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **How to scale:** Ask your AI assistant to draft new data blocks matching this format to easily grow your dashboard.")

# Fetch data for the chosen event
event_data = macro_database[selected_event]

# ------------------------------------------------------
# 4. MAIN DISPLAY: SUMMARY
# ------------------------------------------------------
st.subheader("🧠 Investment Thesis Map")
st.info(f"**{event_data['thesis_map']}**")

st.write("") 
st.subheader("📈 Identified Beneficiaries")

# Display the high-level stock table
df = pd.DataFrame(event_data["stocks"])
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

# ------------------------------------------------------
# 5. MAIN DISPLAY: DEEP DIVES (The New Feature)
# ------------------------------------------------------
st.subheader("🔍 Company Deep Dives & References")
st.markdown("Select an identified company below to view its research, financial health metrics, and future roadmap.")

# Dropdown to select which stock to research
available_tickers = [stock["Ticker"] for stock in event_data["stocks"]]
selected_ticker = st.selectbox("Choose a company to inspect:", options=available_tickers)

# Pull the specific deep dive details for that ticker
ticker_details = event_data["deep_dives"].get(selected_ticker)

if ticker_details:
    # Create 3 neat interactive tabs
    tab1, tab2, tab3 = st.tabs(["📰 News & References", "📊 Financial Health Factors", "🚀 Future Plans & Roadmap"])
    
    with tab1:
        st.markdown("### Latest Relevant Context")
        for article in ticker_details["news"]:
            st.write(article)
            
    with tab2:
        st.markdown("### Core Financial Indicators")
        # Display the financial data as a neat, clean key-value table
        fin_df = pd.DataFrame(ticker_details["financials"].items(), columns=["Metric", "Value"])
        st.table(fin_df)
        
    with tab3:
        st.markdown("### Strategic Future Plans")
        st.warning(ticker_details["future_plans"])

st.caption("\n\nDisclaimer: Data provided for prototype demonstration purposes only.")
