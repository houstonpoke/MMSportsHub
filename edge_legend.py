import streamlit as st

def show_edge_legend():
    st.sidebar.markdown("### 🎯 Morrow’s Edge Legend")
    st.sidebar.markdown("**🔴 Low Confidence**: 0% – 2%")
    st.sidebar.markdown("**🟡 Medium Confidence**: 2% – 5%")
    st.sidebar.markdown("**🟢 High Confidence**: 5% and above")