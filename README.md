# ₿ Cryptocurrency Price Tracker

A Python-based cryptocurrency price tracking system that uses Selenium to collect cryptocurrency market data, Pandas to process and store the data, and Streamlit to display an interactive dashboard.

---

## 📌 Project Overview

The Cryptocurrency Price Tracker collects cryptocurrency information from a web page using Selenium.

The system extracts the Top 10 cryptocurrencies and records:

- Rank
- Cryptocurrency name
- Price
- 24-hour price change
- Market capitalization
- Timestamp

The collected data is stored in a CSV file to maintain historical records.

The project also provides filtering, price graphs, automatic tracking, and an interactive Streamlit dashboard.

---

## 🎯 Objectives

The main objectives of this project are:

1. Automate cryptocurrency data collection.
2. Extract the Top 10 cryptocurrencies.
3. Store cryptocurrency data in CSV format.
4. Maintain historical price records.
5. Filter cryptocurrencies based on price and 24-hour change.
6. Visualize cryptocurrency price history.
7. Provide an interactive dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Selenium | Browser automation and web data extraction |
| Google Chrome | Browser controlled by Selenium |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |
| CSV | Historical data storage |

---

## 📁 Project Structure

```text
crypto-price-tracker/
│
├── crypto_tracker.py
├── crypto_graph.py
├── crypto_dashboard.py
├── app.py
├── test_crypto.html
├── crypto_prices.csv
├── requirements.txt
└── README.md
