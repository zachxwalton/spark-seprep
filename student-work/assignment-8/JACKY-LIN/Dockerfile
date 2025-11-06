# FROM alpine
# COPY prank.py .
# RUN apk add --no-cache python3 py3-pip
# RUN pip install --no-cache-dir --break-system-packages colorama
# RUN chmod +x prank.py
# CMD ["python3", "prank.py"]

# Use the official lightweight Python image (includes pip)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your script into the container
COPY prank.py .

# Install your dependency
RUN pip install --no-cache-dir colorama

# Run the script
CMD ["python3", "prank.py"]
