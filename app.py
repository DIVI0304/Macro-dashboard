import streamlit as st
import pandas as pd

# ------------------------------------------------------
# 1. THE 5-STEP LINEAR DATABASE
# ------------------------------------------------------
macro_database = {
    "🔥 India Heatwave + Cooling Subsidy": {
        "step_1_event": "India heatwave hits 45°C + Govt announces 15% PLI component subsidy.",
        "step_2_economic": "Massive retail shift to cooling appliances; extreme power grid load.",
        "step_3_sector": "HVAC OEM Manufacturing & Electrical Component Bottlenecks.",
        "step_4_company": "Amber Enterprises (AMBER.NS) captures subsidy + supplies 70% of market compressors.",
        "step_5_trade": "BUY AMBER.NS: Valuation is fair, trading at a discount to historical peak-summer multiples.",
        # Base confidence scores for the sliders (out of 10)
        "default_scores": [9, 8, 9, 8, 6] 
    },
    "🤖 Global AI Data Center Boom": {
        "step_1_event": "OpenAI/Google accelerate LLM training requiring 10x compute power.",
        "step_2_economic": "Massive build-out of hyper-scale data centers globally.",
        "step_3_sector": "Server Liquid Cooling Systems and High-Voltage Power Racks.",
        "step_4_company": "Vertiv Holdings (VRT) dominates the specialized liquid cooling market.",
        "step_5_trade": "HOLD VRT: Incredible fundamentals, but retail market has already priced in 2 years of growth.",
        "default_scores": [10, 10, 9, 7, 4] 
    }
}

# ------------------------------------------------------
# 2. DASHBOARD UI SETTINGS
# ------------------------------------------------------
st.set_page_config(page_title="Macro Logic Engine", layout="wide")

st.title("🌍 Thematic Macro Inference Engine")
st.markdown("Trace the logic from a global event directly to a tradeable opportunity.")
st.divider()

# ------------------------------------------------------
# 3. SIDEBAR SELECTION
# ------------------------------------------------------
st.sidebar.header("Select Catalyst")
selected_event = st.sidebar.selectbox(
    "Choose a Global Macro Event:",
    options=list(macro_database.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Pro Tip:** Use the sliders at the bottom to stress-test this thesis.")

event_data = macro_database[selected_event]

# ------------------------------------------------------
# 4. THE 5-STEP WATERFALL VISUALIZATION
# ------------------------------------------------------
st.subheader("🧠 The Logic Map")

# Using Streamlit success/info/warning boxes to create a visual step-by-step flow
st.error(f"**1. THE EVENT:** {event_data['step_1_event']}")
st.markdown("⬇️")
st.warning(f"**2. ECONOMIC SHIFT:** {event_data['step_2_economic']}")
st.markdown("⬇️")
st.info(f"**3. SECTOR IMPACT:** {event_data['step_3_sector']}")
st.markdown("⬇️")
st.success(f"**4. WINNING COMPANY:** {event_data['step_4_company']}")
st.markdown("⬇️")
st.success(f"**5. THE TRADE:** {event_data['step_5_trade']}")

st.divider()

# ------------------------------------------------------
# 5. THE INTERACTIVE SCORING ENGINE
# ------------------------------------------------------
st.subheader("🧮 Interactive Trade Conviction Scorer")
st.markdown("Do you agree with this thesis? Rate each step from 1 (Weak) to 10 (Strong) to calculate the final trade conviction.")

# Create two visual columns: Sliders on the left, Score on the right
col1, col2 = st.columns([2, 1])

with col1:
    s1 = st.slider("1. Event Clarity (Is the catalyst undeniable?)", 1, 10, event_data["default_scores"][0])
    s2 = st.slider("2. Economic Shift (Is the demand shift massive?)", 1, 10, event_data["default_scores"][1])
    s3 = st.slider("3. Sector Alignment (Is this the exact right sub-sector?)", 1, 10, event_data["default_scores"][2])
    s4 = st.slider("4. Company Moat (Does this company dominate?)", 1, 10, event_data["default_scores"][3])
    s5 = st.slider("5. Valuation (Is the stock cheap enough to buy now?)", 1, 10, event_data["default_scores"][4])

# Calculate the percentage score (Max points = 50)
total_points = s1 + s2 + s3 + s4 + s5
conviction_percentage = (total_points / 50) * 100

with col2:
    st.markdown("### Final Conviction Score")
    
    # Display a massive metric number
    st.metric(label="Calculated Probability of Success", value=f"{conviction_percentage:.0f}%")
    
    # Dynamic alerts based on the score
    if conviction_percentage >= 80:
        st.success("🟢 **HIGH CONVICTION**\n\nThe logic is tight and the valuation is good. Strong Buy opportunity.")
    elif conviction_percentage >= 60:
        st.warning("🟡 **MEDIUM CONVICTION**\n\nThe trend is real, but the valuation might be slightly priced in. Monitor for a pullback.")
    else:
        st.error("🔴 **LOW CONVICTION**\n\nToo risky. Either the macro link is weak, or the stock is wildly overvalued. Do not trade.")
