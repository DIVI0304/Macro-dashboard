import streamlit as st
import pandas as pd

# ------------------------------------------------------
# 1. THE INSTITUTIONAL DATABASE
# ------------------------------------------------------
database = {
    "🔥 India Heatwave: The Cooling Supercycle": {
        "climate_energy": {
            "temp_anomaly": "+4.8°C vs 5-yr avg",
            "city_heat_index": {"Delhi": "48°C (Severe)", "Mumbai": "41°C + High Humidity", "Chennai": "43°C"},
            "ac_seasonality": "Peak advanced by 3 weeks; Q1 sales tracking +35% YoY",
            "electricity_load": "Record 240GW peak demand breached; Grid operating at 98% capacity"
        },
        "supply_chain": {
            "compressors": "Amber Enterprises (70% market share) running at 95% capacity.",
            "raw_materials": "Copper +12% MoM, Aluminium +8% MoM. Squeezing unhedged margins.",
            "logistics": "Port congestion at Mundra delaying refrigerant gas imports by 14 days.",
            "inventory": "Retail channel inventory down to 9 days (historically 21 days)."
        },
        "policy_financials": {
            "pli_scheme": "Govt disbursed ₹1,200 Cr to 14 component manufacturers this month.",
            "stocks": [
                {"Ticker": "AMBER.NS", "Role": "Compressor OEM", "P/E": 48.2, "Earnings In": "12 Days", "Signal": "Strong Buy"},
                {"Ticker": "VOLTAS.NS", "Role": "Retail Brand", "P/E": 65.1, "Earnings In": "18 Days", "Signal": "Hold (Margin Risk)"},
                {"Ticker": "HINDCOPPER.NS", "Role": "Raw Material", "P/E": 32.4, "Earnings In": "5 Days", "Signal": "Buy"}
            ]
        }
    }
}

# ------------------------------------------------------
# 2. APP SETUP
# ------------------------------------------------------
st.set_page_config(page_title="Macro Screener Pro", layout="wide")

st.title("🌐 Advanced Macro-Thematic Screener")
st.markdown("Deep-dive into first, second, and third-order economic impacts.")
st.divider()

# ------------------------------------------------------
# 3. EVENT SELECTION
# ------------------------------------------------------
selected_event = st.selectbox("Select Macro Catalyst:", options=list(database.keys()))
event_data = database[selected_event]

st.write("---")

# ------------------------------------------------------
# 4. THE DEEP-DIVE TABS
# ------------------------------------------------------
# This is how you organize massive amounts of data cleanly
tab1, tab2, tab3 = st.tabs([
    "🌡️ Climate & Energy Demand", 
    "⚙️ Supply Chain & Logistics", 
    "🏛️ Policy & Financials"
])

# --- TAB 1: CLIMATE & ENERGY ---
with tab1:
    st.subheader("Real-Time Climate & Grid Stress")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="National Temp Anomaly", value=event_data["climate_energy"]["temp_anomaly"], delta="Critical Stress", delta_color="inverse")
        st.info(f"**AC Seasonality Shift:** {event_data['climate_energy']['ac_seasonality']}")
        
    with col2:
        st.metric(label="National Grid Load", value=event_data["climate_energy"]["electricity_load"])
        
    st.markdown("#### City-Level Heat Index")
    # Convert dictionary to table
    heat_df = pd.DataFrame(list(event_data["climate_energy"]["city_heat_index"].items()), columns=["City", "Heat Index / Status"])
    st.dataframe(heat_df, hide_index=True, use_container_width=True)

# --- TAB 2: SUPPLY CHAIN ---
with tab2:
    st.subheader("Bottlenecks & Material Costs")
    col3, col4 = st.columns(2)
    
    with col3:
        st.warning(f"**Inventory Alert:** {event_data['supply_chain']['inventory']}")
        st.error(f"**Logistics Bottleneck:** {event_data['supply_chain']['logistics']}")
        
    with col4:
        st.info(f"**Component Manufacturing:** {event_data['supply_chain']['compressors']}")
        st.warning(f"**Raw Material Inflation:** {event_data['supply_chain']['raw_materials']}")

# --- TAB 3: POLICY & FINANCIALS ---
with tab3:
    st.subheader("Government Action & Valuations")
    st.success(f"**Policy Tailwind (PLI Scheme):** {event_data['policy_financials']['pli_scheme']}")
    
    st.markdown("#### Target Beneficiaries & Proximity")
    # Display the financial data in a clean dataframe
    stock_df = pd.DataFrame(event_data["policy_financials"]["stocks"])
    st.dataframe(stock_df, hide_index=True, use_container_width=True)
