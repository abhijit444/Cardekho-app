# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
