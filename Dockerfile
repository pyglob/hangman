# Use Ubuntu base image
FROM ubuntu:22.04

MAINTAINER pyglob@gmail.com

# Set environment variables to prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-dev && \
    apt-get install -y openssh-server apache2 && \
    apt-get clean

# Configure SSH server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Set up working directory for the application
WORKDIR /app


# Clone the repository from GitHub
ARG GIT_REPO_URL
RUN git clone ${GIT_REPO_URL} /app/project


# Create a virtual environment inside the project directory
RUN python3.10 -m venv /app/project/venv


# Install dependencies (if the repository has a requirements.txt)
RUN /app/project/venv/bin/pip install --upgrade pip && \
    test -f /app/project/requirements.txt && /app/project/venv/bin/pip install -r /app/project/requirements.txt || echo "No requirements.txt found"


# Expose ports for SSH (22) and HTTP (80)
EXPOSE 22 80

# Start both services
CMD service ssh start && apachectl -D FOREGROUND
