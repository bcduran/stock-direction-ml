import pandas as pd

# Step 1: Load the dataset
file_path = "C:/Users/burha/Downloads/crspraw.csv"
crsp = pd.read_csv(file_path, low_memory=False)

# Step 2: Clean column names
crsp.columns = crsp.columns.str.strip().str.lower()

# Step 3: Filter for required columns
required_cols = ['date', 'ticker', 'prc', 'ret', 'vol', 'shrout', 'shrcd', 'exchcd']
missing = [col for col in required_cols if col not in crsp.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Step 4: Convert key columns to numeric
for col in ['prc', 'ret', 'vol', 'shrout']:
    crsp[col] = pd.to_numeric(crsp[col], errors='coerce')

# Step 5: Drop rows with missing values
crsp = crsp.dropna(subset=['prc', 'ret', 'vol', 'shrout'])

# Step 6: Keep only common stocks (shrcd 10 or 11)
crsp = crsp[crsp['shrcd'].isin([11])]

# Step 7: Keep only NYSE
crsp = crsp[crsp['exchcd'].isin([1])]

# Step 8: Fix any negative prices
crsp['prc'] = crsp['prc'].abs()

# Step 9: Save the cleaned dataset
crsp.to_csv("crsp_cleaned_basic.csv", index=False)
print("✅ Cleaned CRSP dataset saved as crsp_cleaned_basic.csv")
print("Shape:", crsp.shape)
