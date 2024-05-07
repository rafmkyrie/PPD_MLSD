# Use the official Python 3.5 image as a base
FROM python:3.5

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install torch==1.0.1 torchvision==0.2.2 nose

RUN pip install -e .