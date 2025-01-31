import pandas as pd

# Load the CSV
df = pd.read_csv("march_madness_advanced_stats.csv")

# Drop unnecessary unnamed columns
df = df.loc[:, ~df.columns.str.contains("Unnamed")]

# Save the cleaned CSV
df.to_csv("march_madness_cleaned.csv", index=False)
