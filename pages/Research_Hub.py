import streamlit as st

st.title("🔬 Research Hub - Model & Stat Breakdown")

st.markdown("Welcome to the **Research Hub**, your guide to how every stat and edge is calculated in MM Sports Hub.")

st.header("💡 Morrow’s Edge")
st.markdown("""
**Morrow’s Edge = Model Win % - Implied Market %**

This is your main metric for identifying value.  
If your model says a team has a 60% chance to win and the market implies 52%, the Morrow’s Edge is **+8%** — strong signal to bet.

**Color Code:**
- 🟢 High (5%+)
- 🟡 Medium (2–5%)
- 🔴 Low (<2%)
""")

st.header("📊 Key Metrics Explained")

with st.expander("📈 Elo Ratings"):
    st.markdown("""
Elo is a system that adjusts team strength based on wins/losses and opponent strength.  
It’s dynamic, meaning teams gain or lose points after every game.

- Higher = better team
- Every 400 points = 10x more likely to win
    """)

with st.expander("🧮 Implied Probability"):
    st.markdown("""
Convert betting odds into a % chance of winning.

- Odds of -150 = 60%
- Odds of +200 = 33.3%

Used to compare against model win % to create Morrow’s Edge.
    """)

with st.expander("📉 Kelly Criterion"):
    st.markdown("""
Used to size bets based on your edge.

**Formula:**  
`Edge / Odds` = % of bankroll to wager

Bigger edge = bigger bet. Prevents overbetting and bankroll blowups.
    """)

with st.expander("🔁 Bayesian Updating"):
    st.markdown("""
Continuously updates team strength over time.

Start with a prior belief (e.g. power rating) and adjust it with actual game results.

Used to keep your model current and less overreactive to one game.
    """)

with st.expander("📉 CLV (Closing Line Value)"):
    st.markdown("""
Measures whether your bet beat the market.

If you bet at -110 and the line closes -130, you got good value.  
If it closes +100, market disagreed with you.

Sharp bettors consistently beat the close.
    """)

with st.expander("📊 Expected Value (EV)"):
    st.markdown("""
The mathematical profit of a bet.

**Formula:**  
`EV = (Win % × Profit) - (Loss % × Bet)`

If EV > 0, you have a profitable long-term edge.
    """)

st.markdown("---")
st.markdown("More coming soon: Poisson modeling, regression logic, and player-level stats.")