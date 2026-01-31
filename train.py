import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("train.csv")

# Select features
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
df.dropna(inplace=True)

# Encode categorical
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

X = df.drop('Survived', axis=1)
y = df['Survived']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")
