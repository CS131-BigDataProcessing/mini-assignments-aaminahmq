# Start with a base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python", "app.py"]

