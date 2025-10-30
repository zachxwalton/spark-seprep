FROM python:3.11-slim

# Keep Python output unbuffered and avoid .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the assignment directory into the image
COPY Anthony-Sevilla-Meza/ /app/

# Upgrade pip and install requirements if a requirements.txt file exists in the directory.
# The install command is made tolerant to a missing requirements.txt by using shell || true.
RUN python -m pip install --upgrade pip \
    && pip install -r /app/requirements.txt || true

# Default command: run the main script
CMD ["python", "main.py"]
