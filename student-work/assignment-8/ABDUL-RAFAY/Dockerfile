FROM alpine:latest

# Install Python
RUN apk add --no-cache python3

# Copy the script into the container
COPY day.py .

# Set the command to run the script
CMD ["python3", "day.py"]
