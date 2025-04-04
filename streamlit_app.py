import streamlit as st

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.title("🤠 MM Sports Hub")

st.markdown("### Welcome to the Sports Betting Intelligence Platform")

st.markdown("""
MM Sports Hub delivers real-time predictive modeling and betting analytics, powered by:
- ⚡ Elo & Logistic Regression models
- 🔮 Model-based matchup insights
- 📈 (Coming soon) Live odds vs model edges
- 🧠 Research & ROI evaluation tools

---

### 🧭 Navigation:

- 📈 [Elo Predictions](pages/predict_elo.py)
- 🔬 [Research Hub](pages/research_hub.py)

You can also explore the `pages/` folder for direct access.
""")
