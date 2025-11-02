FROM python:3.12-slim

# copying script into container
COPY snail.py .

# give execute permission to my script
RUN chmod +x snail.py

# run my script with python
CMD ["python", "./snail.py"]