import streamlit as st
import pandas as pd

# ------------------------------------------------------
# 1. THE MOCK KNOWLEDGE GRAPH (Hardcoded Data)
# ------------------------------------------------------
# This dictionary acts as your free database. 
# You can add as many new events here as you want later!

macro_database = {
    "🔥 India Heatwave + Cooling Subsidy": {
        "thesis_map": "Extreme Temps ➔ AC Demand Spike ➔ Compressor Bottleneck ➔ Subsidy Boosts OEM Margins",
        "stocks": [
            {"Ticker": "AMBER.NS", "Company": "Amber Enterprises", "Supply Chain Role": "OEM/Component Mfg", "P/E Ratio": 45.2, "Debt/Equity": 0.8, "Risk": "Medium", "Action": "Top Pick"},
            {"Ticker": "VOLTAS.NS", "Company": "Voltas Ltd", "Supply Chain Role": "Consumer AC Brand", "P/E Ratio": 60.1, "Debt/Equity": 0.1, "Risk": "Low", "Action": "Hold"},
            {"Ticker": "SUBROS.NS", "Company": "Subros Ltd", "Supply Chain Role": "Thermal Compressors", "P/E Ratio": 35.5, "Debt/Equity": 0.4, "Risk": "High", "Action": "Spec Buy"}
        ]
    },
    "⚡ US Electric Vehicle Grid Mandate": {
        "thesis_map": "EV Mandate ➔ Grid Overload ➔ Transformer Upgrades ➔ Copper & Switchgear Demand",
        "stocks": [
            {"Ticker": "ETN", "Company": "Eaton Corp", "Supply Chain Role": "Grid Switchgear", "P/E Ratio": 28.4, "Debt/Equity": 0.6, "Risk": "Low", "Action": "Top Pick"},
            {"Ticker": "FCX", "Company": "Freeport-McMoRan", "Supply Chain Role": "Raw Copper Mining", "P/E Ratio": 15.2, "Debt/Equity": 0.3, "Risk": "Medium", "Action": "Buy"},
            {"Ticker": "PWR", "Company": "Quanta Services", "Supply Chain Role": "Grid Infrastructure Install", "P/E Ratio": 32.1, "Debt/Equity": 0.9, "Risk": "Medium", "Action": "Hold"}
        ]
    },
    "🤖 Global AI Data Center Boom": {
        "thesis_map": "AI Adoption ➔ Massive Server Farms ➔ Massive Cooling & Power Needs ➔ Liquid Cooling Shortage",
        "stocks": [
            {"Ticker": "VRT", "Company": "Vertiv Holdings", "Supply Chain Role": "Server Cooling Systems", "P/E Ratio": 55.0, "Debt/Equity": 1.2, "Risk": "Medium", "Action": "Top Pick"},
            {"Ticker": "SMCI", "Company": "Super Micro", "Supply Chain Role": "Server Rack Assembly", "P/E Ratio": 40.5, "Debt/Equity": 0.2, "Risk": "High", "Action": "Buy"},
            {"Ticker": "NVDA", "Company": "Nvidia", "Supply Chain Role": "AI Processors", "P/E Ratio": 75.3, "Debt/Equity": 0.1, "Risk": "Low", "Action": "Hold (Priced In)"}
        ]
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
# Create a dropdown menu using the keys from our mock database
selected_event = st.sidebar.selectbox(
    "Choose a Global Macro Event:",
    options=list(macro_database.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **How it works:** This tool maps real-world events to specific supply chain bottlenecks to find high-probability stock picks.")

# ------------------------------------------------------
# 4. MAIN DISPLAY (Data Output)
# ------------------------------------------------------
# Fetch the specific data for the chosen event
event_data = macro_database[selected_event]

# Display the Logic/Thesis Map
st.subheader("🧠 Investment Thesis Map")
st.info(f"**{event_data['thesis_map']}**")

st.write("") # Add a little space

# Display the Recommended Stocks Table
st.subheader("📈 Identified Beneficiaries")

# Convert the list of dictionaries into a clean Pandas DataFrame for Streamlit to render
df = pd.DataFrame(event_data["stocks"])

# Display the dataframe as an interactive table
st.dataframe(
    df, 
    use_container_width=True, 
    hide_index=True # Hides the ugly number column on the left
)

# Add a fake disclaimer to make it look professional
st.caption("Disclaimer: Fundamental data is for demonstration purposes. Always conduct your own due diligence.")
