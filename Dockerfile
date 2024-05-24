# Use a temporary Python image to install dependencies
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file
# COPY generate_report.py /app/generate_report.py
# COPY requirements.txt /app/requirements.txt
COPY . ./
# Install dependencies
RUN pip3 install  -r requirements.txt


# Create the reports directory
RUN mkdir -p /reports

# Set the command to run the Python script
CMD ["python3","generate_report.py"]
