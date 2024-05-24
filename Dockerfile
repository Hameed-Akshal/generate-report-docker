# Use a temporary Python image to install dependencies
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file
COPY . ./
# Install dependencies
RUN pip3 install  -r requirements.txt

# Set the command to run the Python script
CMD ["python3","generate_report.py"]
