# Use the official Python image from the Docker Hub
FROM python:3.11-slim


# Set the working directory
WORKDIR /app 

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8080

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
