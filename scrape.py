import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Base URL pattern for different years
base_url = "https://www.sports-reference.com/cbb/seasons/men/{}-advanced-school-stats.html"

# Define years to scrape (last 10 years)
years = range(2015, 2025)

# Dictionary to store data for each year
all_data = []

# Loop through each year and scrape data
for year in years:
    url = base_url.format(year)
    print(f"Scraping data for {year}...")

    try:
        # Read tables from the webpage
        tables = pd.read_html(url)
        
        # The main table is usually the first one
        df = tables[0]

        # Add a year column to track the season
        df["Year"] = year

        # Append to list
        all_data.append(df)

    except Exception as e:
        print(f"Could not retrieve data for {year}: {e}")

# Combine all years into a single DataFrame
df_all_years = pd.concat(all_data, ignore_index=True)

# Save to CSV for later analysis
df_all_years.to_csv("march_madness_advanced_stats.csv", index=False)

print("Data scraping complete! Saved as 'march_madness_advanced_stats.csv'.")
