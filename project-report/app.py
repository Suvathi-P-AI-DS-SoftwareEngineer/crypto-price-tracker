import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="Crypto Price Tracker",
    page_icon="₿",
    layout="wide"
)

# ======================================
# TITLE
# ======================================

st.title("₿ Cryptocurrency Price Tracker")

st.markdown(
    "### 📊 Live Cryptocurrency Market Monitoring Dashboard"
)

st.caption(
    "Track cryptocurrency prices, 24-hour changes, "
    "market capitalization and historical records."
)

st.divider()

# ======================================
# LOAD DATA
# ======================================

try:

    df = pd.read_csv("crypto_prices.csv")

    if df.empty:
        st.warning("No cryptocurrency data found.")
        st.stop()

except FileNotFoundError:

    st.error("crypto_prices.csv was not found.")
    st.stop()

# ======================================
# CLEAN DATA
# ======================================

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"]
)

df["Price_Value"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["Change_Value"] = (
    df["24h Change"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .str.replace("+", "", regex=False)
    .astype(float)
)

# ======================================
# LATEST RECORDS
# ======================================

latest = (
    df.sort_values("Timestamp")
      .groupby("Coin")
      .tail(1)
)

# ======================================
# SUMMARY
# ======================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🪙 Cryptocurrencies",
        len(latest)
    )

with col2:
    st.metric(
        "📊 Historical Records",
        len(df)
    )

with col3:
    st.metric(
        "🥇 Top Rank",
        latest["Rank"].min()
    )

with col4:
    st.metric(
        "🔄 Tracking Status",
        "Active Data"
    )

st.divider()

# ======================================
# MARKET TABLE
# ======================================

st.subheader("🏆 Top Cryptocurrency Market")

display_data = latest[
    [
        "Rank",
        "Coin",
        "Price",
        "24h Change",
        "Market Cap"
    ]
].sort_values("Rank")

st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================
# PRICE HISTORY
# ======================================

st.subheader("📈 Cryptocurrency Price History")

coins = sorted(
    df["Coin"].dropna().unique()
)

selected_coin = st.selectbox(
    "Select a cryptocurrency",
    coins
)
# ======================================
# SELECTED COIN INFORMATION
# ======================================

selected_data = latest[
    latest["Coin"] == selected_coin
]

if not selected_data.empty:

    selected_row = selected_data.iloc[0]

    price_col, change_col, market_col = st.columns(3)

    with price_col:
        st.metric(
            "💰 Current Price",
            selected_row["Price"]
        )

    with change_col:
        st.metric(
            "📈 24h Change",
            selected_row["24h Change"]
        )

    with market_col:
        st.metric(
            "💎 Market Cap",
            selected_row["Market Cap"]
        )

coin_data = df[
    df["Coin"] == selected_coin
].sort_values("Timestamp")

# ======================================
# IMPROVED PRICE GRAPH
# ======================================

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    coin_data["Timestamp"],
    coin_data["Price_Value"],
    marker="o",
    linewidth=2
)

ax.set_title(
    f"{selected_coin} Price History",
    fontsize=16
)

ax.set_xlabel(
    "Time",
    fontsize=11
)

ax.set_ylabel(
    "Price (USD)",
    fontsize=11
)

ax.grid(
    True,
    alpha=0.3
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

st.pyplot(fig)

st.divider()

# ======================================
# FILTER
# ======================================

st.subheader("🔎 Cryptocurrency Filter")

minimum_change = st.slider(
    "Show cryptocurrencies with 24h change greater than:",
    -10.0,
    10.0,
    1.0,
    0.5
)

filtered = latest[
    latest["Change_Value"] > minimum_change
]

st.dataframe(
    filtered[
        [
            "Rank",
            "Coin",
            "Price",
            "24h Change",
            "Market Cap"
        ]
    ].sort_values("Rank"),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================
# FOOTER
# ======================================

st.caption(
    "Cryptocurrency Price Tracker • "
    "Selenium • Pandas • Streamlit • Matplotlib"
)