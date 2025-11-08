import numpy as np
import pandas as pd


data = {
    'size': ['XL', 'L', 'M', np.nan, 'M', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red', 'green'],
    'gender': ['female', 'male', np.nan, 'female', 'female', 'male'],
    'price': [199.0, 89.0, np.nan, 129.0, 79.0, 89.0],
    'weight': [500, 450, 300, np.nan, 410, np.nan],
    'bought': ['yes', 'no', 'yes', 'no', 'yes', 'no']
}

# Create DataFrame
df = pd.DataFrame(data)

# Find Missing Values (NaN)
null_items = df.isna()

# Convert Missing Values to Percentage with 2 DP
null_items_pctg = np.round(null_items.sum() / len(df), 2)

print(null_items_pctg)