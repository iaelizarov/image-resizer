# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port your FastAPI app runs on (default is 8000)
EXPOSE 8000

# Command to run your application
CMD ["python", "main.py"]
