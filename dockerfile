# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Set the default command to run the app
CMD ["python","app.py"]