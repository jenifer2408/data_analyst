import pandas as pd

# Load Superstore
df = pd.read_csv("data/superstore.csv")

# Get valid, unique Customer IDs
customer_ids = (
    df["Customer ID"]
    .dropna()
    .drop_duplicates()
)

# Take 100 actual Customer IDs
customer_ids = customer_ids.head(100)

# Save them
customer_ids.to_csv(
    "data/customer_ids.csv",
    index=False
)

print("Customer IDs extracted:", len(customer_ids))
print("\nFirst 10 IDs:")
print(customer_ids.head(10))

print("\nSaved to: data/customer_ids.csv")