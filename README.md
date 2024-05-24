# Hugging Face Model Hub Report Generator

This Docker container periodically generates reports on the top 10 downloaded models from the Hugging Face model hub and saves them as JSON files.


## Project Structure

- Dockerfile: Defines the Docker image and sets up the environment for running the Python script.
  ```
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
  ```
  - Base Image: `python:3.9-slim` provides a minimal Python environment.
  - Working Directory: `/app` ensures all operations are performed in this directory within the container.
  - File Copy: Copies the current directory contents (including scripts and dependencies list) into the container.
  - Dependency Installation: Installs necessary Python packages specified in `requirements.txt`.
  - Default Command: Executes `generate_report.py` using Python 3 when the container starts.

- generate\_report.py: Python script to fetch data from the Hugging Face model hub API, compile a list of the top 10 downloaded models, and save the report as a JSON file.

- requirements.txt: Lists the Python dependencies required by the `generate_report.py` script.


## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker: [Install Docker]()


## Getting Started

Follow these steps to set up and run the report generator:


### 1. Clone the Repository

Clone this repository to your local machine:

   ```
   git clone https://github.com/Hameed-Akshal/generate-report-docker.git
   ```

### 2. Navigate to the Project Directory

Move into the directory containing the Dockerfile, Python script, and requirements file:

    cd generate-report-docker
    


### 3. Build the Docker Image

Build the Docker image using the provided Dockerfile. This image will contain all the dependencies required to run the report generation script:

    docker build -t huggingface-report-generator .
    


### 4. Run the Docker Container

Run the Docker container to generate the report:

    docker run --rm -v "$(pwd):/app" huggingface-report-generator
    

This command runs the container, mounts the current directory to the `/app` directory inside the container, executes the report generation script, and saves the report locally. The `--rm` flag ensures the container is removed after it stops running.


