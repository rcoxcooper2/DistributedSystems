```markdown
# Meteorite Data Analysis

## Description
This project provides a Python script for analyzing meteorite landing data. The script processes a JSON file containing information about meteorite landings and generates summary statistics about the meteorites, including average mass, hemisphere distribution, and class distribution.

## Files
- **ml_data_analysis.py**: The main Python script for analyzing meteorite landing data.
- **test_ml_data_analysis.py**: Test script containing unit tests for the functions in ml_data_analysis.py.
- **Meteorite_Landings.json**: Example dataset containing meteorite landing data in JSON format.

## Usage

### Running with Docker Image from Docker Hub
```bash
docker run rcoxcooper2/ml_data_analysis:hw04
```

### Building and Running from Dockerfile
```bash
docker build -t ml_data_analysis:hw04 .
docker run ml_data_analysis:hw04
```

### Running with User-provided Data
To run the script with user-provided data, mount the directory containing the data to `/data` in the container and specify the path to the data file as an argument.
```bash
docker run -v /path/to/data:/data ml_data_analysis:hw04 /data/your_data.json
```

### Running Tests with Pytest
```bash
docker run ml_data_analysis:hw04 pytest
```

## Expected Input Data
The input data should be in JSON format and contain information about meteorite landings. Each entry in the JSON file should represent a single meteorite landing event and include fields such as name, id, recclass, mass (g), reclat, reclong, and GeoLocation.

Example snippet of input data:
```json
[
  {
    "name": "Smitty",
    "id": "10001",
    "recclass": "L5",
    "mass (g)": "21",
    "reclat": "50.775",
    "reclong": "6.08333",
    "GeoLocation": "(50.775, 6.08333)"
  },
  {
    "name": "James",
    "id": "10002",
    "recclass": "H6",
    "mass (g)": "720",
    "reclat": "56.18333",
    "reclong": "10.23333",
    "GeoLocation": "(56.18333, 10.23333)"
  },
  ...
]
```

For additional meteorite landing data, you can download more datasets from [this link](https://example.com/meteorite_data).
```