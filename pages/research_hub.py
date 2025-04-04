import streamlit as st

st.title("🔬 Research Hub")

st.markdown("""
This section will include:
- Model Performance Comparison (Elo vs Logistic)
- Historical Edge Visualization
- Glossary of Betting Terms

---
### Glossary
- **Elo**: A rating system that updates based on wins/losses. Used for predicting matchups.
- **Implied Probability**: Converts betting odds to % chance (e.g., -150 = 60%).
- **Edge**: The value difference between your model's win % and the sportsbook's implied %.
""")