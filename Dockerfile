# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY myapp.py .

# Optional: Add any additional dependencies if needed
# RUN pip install --no-cache-dir some_package

# Run the script when the container launches
CMD ["python", "myapp.py"]
