# # Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install -y tesseract-ocr

EXPOSE 8000


CMD ["python", "main.py"]