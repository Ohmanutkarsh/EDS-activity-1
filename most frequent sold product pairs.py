import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# 1. Group products by 'Date' and create a list of products for each date
# We use sort() to ensure pairs like (A, B) and (B, A) are treated as the same
grouped = df.groupby('Date')['Product'].apply(list)

pair_counts = Counter()

# 2. Iterate through each date's product list to find combinations
for products in grouped:
    # Sort products alphabetically to maintain consistency in pairing
    products.sort()
    # Generate unique pairs (combinations of 2)
    day_pairs = list(combinations(products, 2))
    # Update the global counter
    pair_counts.update(day_pairs)

# 3. Find the maximum frequency
if pair_counts:
    max_freq = max(pair_counts.values())

    # 4. Filter all pairs that match the maximum frequency
    # We sort the keys to ensure the output matches the expected alphabetical order
    most_frequent = sorted([pair for pair, count in pair_counts.items() if count == max_freq])

    # 5. Output the results in the required format: "Product A and Product B: X times"
    for pair in most_frequent:
        print(f"{pair[0]} and {pair[1]}: {max_freq} times")
		
