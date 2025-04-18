# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from your local project folder into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (required by Cloud Run)
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
