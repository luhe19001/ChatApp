import requests
import pandas as pd

url = "https://www.federalreserve.gov/releases/lbr/current/default.htm"

response = requests.get(url)

dfs = pd.read_html(response.content)

# Select the table that contains the bank asset data
bank_assets_df = dfs[3]

# Clean up the data
bank_assets_df.columns = bank_assets_df.iloc[0]
bank_assets_df = bank_assets_df.iloc[1:]
bank_assets_df = bank_assets_df[["Reporting Bank", "Total assets"]]

# Save the data to a CSV file
bank_assets_df.to_csv("bank_assets.csv", index=False)

print("Bank asset data downloaded and saved to bank_assets.csv")
