# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts and data into the container
COPY ml_data_analysis.py .
COPY test_ml_data_analysis.py .
COPY Meteorite_Landings.json .

# Install pytest for running tests
RUN pip install pytest

# Run pytest to ensure the tests pass
RUN pytest

# Expose any necessary ports
EXPOSE 8000

# Set the command to run the script when the container starts
CMD ["python", "ml_data_analysis.py", "Meteorite_Landings.json"]
