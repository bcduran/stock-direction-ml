import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the feature-enhanced dataset
df = pd.read_csv("C:/Users/burha/Downloads/crsp_with_features.csv")

df['market_cap'] = (df['prc'] * df['shrout']) / 1e3

# Step 2: Define features and target
features = ['market_cap', 'momentum_5d', 'ma_20d', 'volatility_30d']
target = 'target_class'

# Step 3: Drop missing values (safety check)
df = df.dropna(subset=features + [target])

# Step 4: Prepare X and y
X = df[features].values
y = df[target].values

# Step 5: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 7: Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate performance
print("✅ Model Performance")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
