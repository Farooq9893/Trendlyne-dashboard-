import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd
import datetime

# Simulated Sector & Industry Data (Replace with actual NSE/BSE data fetch later)
sector_data = {
    'Sector': ['IT', 'Banking', 'FMCG', 'Pharma', 'Auto', 'Real Estate', 'Energy', 'Telecom', 'Metal', 'Media'],
    '1D': [0.5, -0.3, 0.2, 0.8, -0.1, 1.0, 0.7, -0.4, 0.3, 0.0],
    '7D': [2.1, 1.4, 0.5, 3.2, -0.9, 2.5, 3.1, -1.2, 1.1, 0.8],
    '30D': [5.4, 4.8, 2.7, 6.1, 1.2, 7.0, 6.5, -2.3, 3.9, 2.4]
}
industry_data = {
    'Industry': ['Software', 'Private Banks', 'Beverages', 'Biotech', 'Automobile Parts', 'Construction', 'Oil & Gas', 'Telecom Services', 'Steel', 'Entertainment'],
    '1D': [0.6, -0.2, 0.1, 0.9, -0.2, 1.1, 0.6, -0.5, 0.4, 0.2],
    '7D': [2.2, 1.5, 0.6, 3.5, -1.0, 2.7, 3.2, -1.4, 1.2, 0.9],
    '30D': [5.8, 4.9, 2.8, 6.4, 1.1, 7.3, 6.8, -2.6, 4.0, 2.6]
}

sector_df = pd.DataFrame(sector_data)
industry_df = pd.DataFrame(industry_data)

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Dashboard", "Screener", "Study Material", "AI Chatbot"],
        icons=['bar-chart-line', 'search', 'book', 'robot'], menu_icon="cast", default_index=0)

# Header
st.title("📊 VCP Screener & Stock Analysis Dashboard")

# Dashboard Section
if selected == "Dashboard":
    col1, col2, col3 = st.columns(3)
    col1.metric("Top Gainer Sector", "IT", "+8.2%")
    col2.metric("Volume Surge", "TATASTEEL", "+320%")
    col3.metric("Breakout Count", "15 Stocks", "+5 Today")
    style_metric_cards()

    # Sector Rotation Heatmap
    st.subheader("📈 Sector Rotation Heatmap")
    time_range = st.radio("Select Timeframe:", ["1D", "7D", "30D"], horizontal=True)
    fig = px.bar(sector_df, x='Sector', y=time_range, color=time_range, color_continuous_scale='RdYlGn')
    st.plotly_chart(fig, use_container_width=True)

    # Industry Rotation Heatmap
    st.subheader("🏭 Industry Rotation Heatmap")
    fig2 = px.bar(industry_df, x='Industry', y=time_range, color=time_range, color_continuous_scale='Blues')
    st.plotly_chart(fig2, use_container_width=True)

# Screener Section
elif selected == "Screener":
    st.subheader("🔍 VCP + Volume Surge Screener")
    st.write("(Coming soon with real-time data and filters)")
    st.success("You will be able to filter by D/E ratio, volume spike, and RS rank.")

# Study Material Section
elif selected == "Study Material":
    st.subheader("📚 Downloadable PDF Resources")
    st.download_button("📥 Download Price Action Guide (PDF)", data="Price Action Content...", file_name="price_action.pdf")
    st.download_button("📥 Download VCP Strategy (PDF)", data="VCP Strategy Content...", file_name="vcp_strategy.pdf")

# Chatbot Section
elif selected == "AI Chatbot":
    st.subheader("🤖 Ask Anything about Stocks")
    st.info("ChatGPT integration coming soon...")
    st.text_input("Ask your question:", placeholder="e.g. What is a VCP breakout?")
