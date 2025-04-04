import streamlit as st

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.sidebar.title("📊 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Overview", icon="🏠")
st.sidebar.page_link("pages/predict_elo.py", label="📈 Elo Predictions")
st.sidebar.page_link("pages/research_hub.py", label="🔬 Research Hub")

st.title("🤠 MM Sports Hub")
st.subheader("Welcome to the Sports Betting Intelligence Platform")

st.markdown("""
**MM Sports Hub** delivers real-time predictive modeling and betting analytics, powered by:
- ⚡ Elo & Logistic Regression models
- 🔮 Upcoming model-based insights
- 📈 Live odds (mock data for now)
- 🧠 Research & ROI evaluation tools

Use the sidebar to navigate through the app.
""")