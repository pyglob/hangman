# Use Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-dev && \
    apt-get clean

# Set up working directory for the application
WORKDIR /app

# Copy all required files into the image
COPY hangman.py words.txt /app/

RUN chmod +x /app/hangman.py && ln -s /app/hangman.py /app/hangman

ENV PATH="/app:${PATH}"

# Create a virtual environment inside the project directory
RUN python3.10 -m venv /app/venv

# Install dependencies (if the repository has a requirements.txt)
RUN /app/venv/bin/pip install --upgrade pip

# Expose ports for SSH (22) and HTTP (80)
EXPOSE 22 80

# Optionally, run hangman by default
ENTRYPOINT ["hangman"]
