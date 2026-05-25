import streamlit as st
import pandas as pd

# -----------------------------
# MOCK KNOWLEDGE GRAPH (CORE ENGINE)
# -----------------------------
KNOWLEDGE_GRAPH = {
    "India Heatwave + Government Subsidies": {
        "cause": "Extreme temperature rise + policy support for cooling infrastructure",
        "impact": "Increased demand for cooling, electricity, HVAC systems",
        "supply_chain": [
            "Power demand ↑ → Utilities load increases",
            "Copper & electrical wiring demand ↑",
            "AC manufacturing & compressor demand ↑"
        ],
        "stocks": [
            {
                "ticker": "VOLTAS.NS",
                "name": "Voltas",
                "role": "AC Manufacturer",
                "pe_ratio": 58.2,
                "de_ratio": 0.12,
                "score": 8.7
            },
            {
                "ticker": "BLUESTARCO.NS",
                "name": "Blue Star",
                "role": "Cooling Systems & HVAC",
                "pe_ratio": 52.4,
                "de_ratio": 0.18,
                "score": 8.5
            },
            {
                "ticker": "AMBER.NS",
                "name": "Amber Enterprises",
                "role": "AC Components Manufacturer",
                "pe_ratio": 66.1,
                "de_ratio": 0.35,
                "score": 8.9
            }
        ]
    },

    "US Electric Vehicle Mandates": {
        "cause": "Government EV adoption mandates + tax incentives",
        "impact": "Shift from ICE vehicles to EV ecosystem",
        "supply_chain": [
            "Lithium battery demand ↑",
            "Semiconductors for EVs ↑",
            "Charging infrastructure expansion ↑"
        ],
        "stocks": [
            {
                "ticker": "TSLA",
                "name": "Tesla",
                "role": "EV Manufacturer",
                "pe_ratio": 70.5,
                "de_ratio": 0.08,
                "score": 9.2
            },
            {
                "ticker": "NVDA",
                "name": "NVIDIA",
                "role": "EV Chips & AI Systems",
                "pe_ratio": 45.3,
                "de_ratio": 0.21,
                "score": 9.5
            },
            {
                "ticker": "ALB",
                "name": "Albemarle",
                "role": "Lithium Supplier",
                "pe_ratio": 28.4,
                "de_ratio": 0.40,
                "score": 8.6
            }
        ]
    },

    "Global Semiconductor Shortage": {
        "cause": "Supply chain disruption + rising AI demand",
        "impact": "Chip supply constraints across industries",
        "supply_chain": [
            "Chip manufacturers capacity constrained",
            "Electronics production delays",
            "Pricing power shifts to semiconductor firms"
        ],
        "stocks": [
            {
                "ticker": "TSM",
                "name": "TSMC",
                "role": "Chip Manufacturing",
                "pe_ratio": 32.1,
                "de_ratio": 0.22,
                "score": 9.6
            },
            {
                "ticker": "AMD",
                "name": "AMD",
                "role": "Semiconductor Designer",
                "pe_ratio": 38.7,
                "de_ratio": 0.30,
                "score": 9.1
            },
            {
                "ticker": "INTC",
                "name": "Intel",
                "role": "Chip Manufacturing & R&D",
                "pe_ratio": 25.6,
                "de_ratio": 0.42,
                "score": 7.8
            }
        ]
    }
}

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Macro Event Stock Dashboard", layout="wide")

st.title("📊 Macro Event → Stock Intelligence Dashboard")

st.write(
    "This tool maps real-world macro events into supply chain impacts and potential stock beneficiaries."
)

# Sidebar selection
event = st.sidebar.selectbox(
    "Select Macro Event",
    list(KNOWLEDGE_GRAPH.keys())
)

data = KNOWLEDGE_GRAPH[event]

# -----------------------------
# MAIN THESIS VIEW
# -----------------------------
st.subheader("🧠 Investment Thesis Map")

st.markdown(f"""
### Cause
{data['cause']}

⬇️

### Supply Chain Impact
{data['impact']}

⬇️

### Transmission Chain
""")

for step in data["supply_chain"]:
    st.markdown(f"- {step}")

# -----------------------------
# STOCK TABLE
# -----------------------------
st.subheader("📈 Recommended Stocks (Mock Intelligence Engine)")

df = pd.DataFrame(data["stocks"])

df = df.rename(columns={
    "ticker": "Ticker",
    "name": "Company",
    "role": "Supply Chain Role",
    "pe_ratio": "P/E Ratio",
    "de_ratio": "Debt/Equity",
    "score": "Recommendation Score (0-10)"
})

st.dataframe(df, use_container_width=True)

# -----------------------------
# INSIGHT FOOTER
# -----------------------------
st.markdown("---")
st.caption(
    "⚠️ This is a mock system for learning. Not financial advice. No real-time data is used."
)
