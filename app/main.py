import streamlit as st
from utils import load_data, summarize_data, plot_boxplot, plot_bar_avg_ghi

# Set page config
st.set_page_config(
    page_title="Solar Dashboard",
    layout="wide",
    page_icon="☀️"
)

# Header
st.title("☀️ Solar Potential Comparison Dashboard")
st.markdown("""
Explore and compare solar energy potential across **Benin**, **Togo**, and **Sierra Leone** using interactive visualizations and statistics.
""")
st.markdown("---")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("""
This dashboard compares **Global Horizontal Irradiance (GHI)**, **Direct Normal Irradiance (DNI)**, and **Diffuse Horizontal Irradiance (DHI)** using cleaned datasets.

Built with ❤️ using **Streamlit**.
""")

# Load data
df = load_data()

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 Summary", "📊 Boxplots", "📉 GHI Ranking"])

# --- Tab 1: Summary ---
with tab1:
    st.subheader("📋 Summary Statistics")
    summary = summarize_data(df)
    st.dataframe(summary.style.format(precision=2), use_container_width=True)
    st.markdown("This table shows the **mean**, **median**, and **standard deviation** of each metric per country.")

# --- Tab 2: Boxplots ---
with tab2:
    st.subheader("📊 Metric Distribution by Country")
    metric = st.selectbox("Choose a metric to visualize", ['GHI', 'DNI', 'DHI'])
    st.markdown("Boxplot showing the distribution of selected solar metric across countries.")
    fig_box = plot_boxplot(df, metric)
    st.pyplot(fig_box)

# --- Tab 3: GHI Ranking ---
with tab3:
    st.subheader("📉 Average GHI Ranking")
    st.markdown("Bar chart ranking countries by their **average GHI**.")
    fig_bar = plot_bar_avg_ghi(df)
    st.pyplot(fig_bar)

# Footer
st.markdown("---")
st.caption("Created by your name • Solar Challenge Week 1")
