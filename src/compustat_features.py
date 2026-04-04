import pandas as pd

# --- Step 1: Load raw Compustat file ---
comp = pd.read_csv("C:/Users/burha/Downloads/compustat.csv", low_memory=False)

# --- Step 2: Convert date column ---
comp['datadate'] = pd.to_datetime(comp['datadate'], errors='coerce')
comp = comp.dropna(subset=['datadate', 'permno'])  # Keep only valid entries

# --- Step 3: Keep only relevant variables ---
keep_vars = ['permno', 'datadate', 'epspxq', 'niq', 'ceqq', 'ltq', 'atq', 'revtq', 'cshoq']
comp = comp[keep_vars]

# --- Step 4: Convert financials to numeric ---
for col in ['epspxq', 'niq', 'ceqq', 'ltq', 'atq', 'revtq', 'cshoq']:
    comp[col] = pd.to_numeric(comp[col], errors='coerce')

# --- Step 5: Drop rows with missing key data ---
comp = comp.dropna(subset=['epspxq', 'niq', 'ceqq', 'ltq', 'atq'])

# --- Step 6: Create financial ratios/features ---
comp['pe_ratio'] = comp['epspxq'].replace(0, pd.NA)
comp['de_ratio'] = comp['ltq'] / comp['ceqq']
comp['roe'] = comp['niq'] / comp['ceqq']
comp['roa'] = comp['niq'] / comp['atq']

# --- Step 7: Drop rows with missing ratios ---
comp = comp.dropna(subset=['pe_ratio', 'de_ratio', 'roe', 'roa'])

# --- Step 8: Save cleaned and featured Compustat data ---
comp.to_csv("compustat_cleaned_with_ratios.csv", index=False)
print("✅ Compustat cleaned and saved as compustat_cleaned_with_ratios.csv")
print("Final shape:", comp.shape)
