# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train model
RUN python train.py

# Run prediction
CMD ["python", "predict.py"]
