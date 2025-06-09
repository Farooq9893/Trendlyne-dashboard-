import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd

# Sample Data (Replace with real stock data later)
data = {
    'Sector': ['IT', 'Banking', 'FMCG', 'Pharma', 'Auto'],
    'Performance': [8.2, 5.1, 3.3, -1.2, 4.5]
}
df = pd.DataFrame(data)

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Dashboard", "Screener", "Study Material", "AI Chatbot"],
        icons=['bar-chart-line', 'search', 'book', 'robot'], menu_icon="cast", default_index=0)

# Header
st.markdown("""
    <style>
        .main {
            background-color: #F9FAFC;
        }
        .css-1d391kg {background-color: #F9FAFC;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 VCP Screener & Stock Analysis Dashboard")

# Dashboard Section
if selected == "Dashboard":
    col1, col2, col3 = st.columns(3)
    col1.metric("Top Gainer Sector", "IT", "+8.2%")
    col2.metric("Volume Surge", "TATASTEEL", "+320%")
    col3.metric("Breakout Count", "15 Stocks", "+5 Today")
    style_metric_cards()

    st.subheader("📈 Sector Rotation Heatmap")
    fig = px.bar(df, x='Sector', y='Performance', color='Performance', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig, use_container_width=True)

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
    st.text_input("Ask your question:", placeholder="e.g. What is a VCP breakout?"
