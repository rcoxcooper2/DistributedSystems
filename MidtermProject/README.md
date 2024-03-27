# ISS Tracking Flask Application

Welcome to the ISS Tracking Flask Application! This application allows you to query and retrieve interesting information from the International Space Station (ISS) positional and sighting datasets. 

## Description

The ISS Tracking Flask Application loads two datasets:
1. **Positional Data**: Contains ISS position and velocity data at given times.
2. **Sighting Data**: Provides information on when the ISS can be seen over select cities.

The Flask application provides the following routes to interact with the data:

1. **Load Data**: POST `/load_positional_data` - Endpoint to load positional data and sighting data from a file into memory.
2. **Get All Epochs**: GET `/positional_data/epochs` - Retrieve all epochs in the positional data.
3. **Get Epoch Info**: GET `/positional_data/epochs/<epoch>` - Retrieve information about a specific epoch in the positional data.
4. **Get All Countries**: GET `/sighting_data/countries` - Retrieve all countries from the sighting data.
5. **Get Country Info**: GET `/sighting_data/countries/<country>` - Retrieve information about a specific country in the sighting data.
6. **Get All Regions by Country**: GET `/sighting_data/countries/<country>/regions` - Retrieve all regions associated with a given country in the sighting data.
7. **Get Region Info**: GET `/sighting_data/countries/<country>/regions/<region>` - Retrieve information about a specific region in the sighting data.
8. **Get All Cities by Country and Region**: GET `/sighting_data/countries/<country>/regions/<region>/cities` - Retrieve all cities associated with a given country and region in the sighting data.
9. **Get City Info**: GET `/sighting_data/countries/<country>/regions/<region>/cities/<city>` - Retrieve information about a specific city in the sighting data.

## Requirements

- Python 3.9
- Flask
- xmltodict

## How to Run

Follow these steps to run the application:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies
4. Run the Flask application with `python app.py`.

Once the application is running, you can make requests to the above-mentioned routes using tools like Postman or cURL.

## Dockerfile

The Dockerfile included in this repository allows you to containerize the Flask application along with both the positional and sighting datasets. To build the Docker image, run the following command:

```bash
docker build -t iss-tracking-midterm .
```

## Makefile

The Makefile provides convenient targets to build the Docker container and start the containerized Flask application. Use the following commands:

- `make build`: Builds the Docker container.
- `make run`: Starts the containerized Flask application.
- 'python app.py': For windows to start flask application
## Additional Information

- The `app.py` file contains the main Flask application code.
- The `dockerfile` defines the Docker image for containerizing the application.
- The `makefile` provides targets to simplify Docker image building and application running.
- Ensure you adhere to the ethical and professional responsibilities in engineering situations, such as citing data sources and verifying data quality.

For further details, refer to the project documentation and the written document included in the repository.

Enjoy tracking the International Space Station with this Flask application! 🛰🌍

Data Source:
The positional data for the International Space Station (ISS) was obtained from NASA's Open Data Portal. The specific dataset used can be found at: [ISS_COORDS_2022-02-13](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq/about_data).
