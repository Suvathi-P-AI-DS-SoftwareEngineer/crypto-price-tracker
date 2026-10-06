from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd
from datetime import datetime


# ======================================
# SETTINGS
# ======================================

TRACKING_INTERVAL = 30   # seconds


print("======================================")
print("     CRYPTOCURRENCY PRICE TRACKER")
print("======================================")

print("\nAutomatic tracking started.")
print("Data will be collected every 30 seconds.")
print("Press CTRL + C to stop the program.")


# Start Chrome
driver = webdriver.Chrome()


try:

    while True:

        print("\n======================================")
        print("Collecting cryptocurrency data...")
        print("======================================")


        # ======================================
        # OPEN TEST WEBPAGE
        # ======================================

        file_path = os.path.abspath("test_crypto.html")

        url = "file:///" + file_path.replace("\\", "/")

        driver.get(url)

        time.sleep(2)


        # ======================================
        # FIND CRYPTO ROWS
        # ======================================

        rows = driver.find_elements(
            By.CSS_SELECTOR,
            "#crypto-table tbody tr"
        )

        print("Rows found:", len(rows))


        # ======================================
        # EXTRACT DATA
        # ======================================

        crypto_data = []

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        for row in rows:

            columns = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            if len(columns) >= 5:

                rank = columns[0].text
                coin = columns[1].text
                price = columns[2].text
                change = columns[3].text
                market_cap = columns[4].text

                crypto_data.append([
                    timestamp,
                    rank,
                    coin,
                    price,
                    change,
                    market_cap
                ])


        # ======================================
        # CREATE DATAFRAME
        # ======================================

        df = pd.DataFrame(
            crypto_data,
            columns=[
                "Timestamp",
                "Rank",
                "Coin",
                "Price",
                "24h Change",
                "Market Cap"
            ]
        )


        # ======================================
        # DISPLAY DATA
        # ======================================

        print("\nTop 10 cryptocurrencies:")

        print(
            df.to_string(index=False)
        )


        # ======================================
        # SAVE TO CSV
        # ======================================

        file_name = "crypto_prices.csv"


        if os.path.exists(file_name):

            old_data = pd.read_csv(
                file_name
            )

            final_data = pd.concat(
                [
                    old_data,
                    df
                ],
                ignore_index=True
            )

        else:

            final_data = df


        final_data.to_csv(
            file_name,
            index=False
        )


        print("\nData saved successfully!")

        print(
            "Total historical records:",
            len(final_data)
        )


        # ======================================
        # WAIT
        # ======================================

        print(
            "\nNext collection in",
            TRACKING_INTERVAL,
            "seconds..."
        )

        time.sleep(
            TRACKING_INTERVAL
        )


except KeyboardInterrupt:

    print("\n\nTracking stopped by user.")


finally:

    driver.quit()

    print("Chrome closed.")
    print("Program finished.")