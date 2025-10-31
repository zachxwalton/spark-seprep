# Use a slim Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY joke_generator.py .

# Make sure the script is executable
RUN chmod +x joke_generator.py

# Set the default command to run the script
CMD ["python", "./joke_generator.py"]
