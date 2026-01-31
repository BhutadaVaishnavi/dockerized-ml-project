import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Example passenger
# Pclass, Sex(0=female,1=male), Age, Fare
sample = np.array([[3, 1, 25, 7.25]])

prediction = model.predict(sample)

print("Survived" if prediction[0] == 1 else "Not Survived")

