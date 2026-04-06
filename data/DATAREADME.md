# Data Folder

This folder is reserved for local data files used during preprocessing and modelling.

## Data Sources
The project uses:

- **CRSP-derived daily stock data** (accessed via WRDS)
- Optional **Compustat-linked financial variables** for extended feature engineering

## Notes
- Raw data files are **not included** in this repository due to licensing and access restrictions.
- Users should place their own local input files in this folder if they want to reproduce the preprocessing pipeline.
- File paths in scripts may need to be adjusted to match the local project structure.

## Expected Local Inputs
Examples of files used during development:

- `crspraw.csv`
- `crsp_cleaned_basic.csv`
- `crsp_with_technical_features.csv`
- `compustat.csv`

## Recommendation
For reproducibility, it is recommended to organize local files as follows:

```text
data/
├── crspraw.csv
├── crsp_cleaned_basic.csv
├── crsp_with_technical_features.csv
└── compustat.csv
