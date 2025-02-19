import pandas as pd
import numpy as np

base_url = "https://kenpom.com/index.php?y="

year = range(2002, 2026)

for year in year:
    url = base_url + str(year)
    print(url)
