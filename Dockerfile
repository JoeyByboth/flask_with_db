# Use the official Python image from the Docker Hub
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install necessary dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy the requirements file into the container
COPY requirements.txt requirements.txt
COPY database.conf /app
COPY templates/ /app/templates

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Copy the current directory contents into the container at /code
COPY src/ /app

# Run the Flask app
# Add a delay to ensure the database is ready
CMD ["sh", "-c", "sleep 10 && flask run --host=0.0.0.0"]