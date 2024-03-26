import os
import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_load_positional_data(client):
    # Test case for successful loading of positional data
    response = client.post('/load_positional_data')
    data = json.loads(response.data)
    assert response.status_code == 200
    #assert data['message'] == 'Positional data loaded successfully'

    # Test case for error handling with invalid XML file
    # Assuming there's a test_invalid_positional.xml file for this test
    with open('test_invalid_positional.xml', 'w') as f:
        f.write('Invalid XML content')
    response = client.post('/load_positional_data')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Error loading positional data'

    # Clean up test_invalid_positional.xml
    os.remove('test_invalid_positional.xml')

def test_load_sighting_data(client):
    # Test case for successful loading of sighting data
    response = client.post('/load_sighting_data')
    data = json.loads(response.data)
    assert response.status_code == 200
    #assert data['message'] == 'Sighting data loaded successfully'

    # Test case for error handling with invalid XML file
    # Assuming there's a test_invalid_sighting.xml file for this test
    with open('test_invalid_sighting.xml', 'w') as f:
        f.write('Invalid XML content')
    response = client.post('/load_sighting_data')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Error loading sighting data'

    # Clean up test_invalid_sighting.xml
    os.remove('test_invalid_sighting.xml')

def test_instructions(client):
    # Test case for accessing instructions
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'message' in data
    assert 'instructions' in data

def test_get_all_epochs(client):
    # Test case for getting all epochs
    response = client.get('/positional_data/epochs')
    data = json.loads(response.data)
    assert response.status_code == 200
    #assert 'epochs' in data

def test_get_epoch_info(client):
    # Test case for getting info about a specific epoch
    # Assuming there's at least one epoch available for testing
    response = client.get('/positional_data/epochs/2024-03-18T12:00:00')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'epoch_info' in data or 'message' in data

def test_get_all_countries(client):
    # Test case for getting all countries
    response = client.get('/sighting_data/countries')
    data = json.loads(response.data)
    assert response.status_code == 200
    #assert 'countries' in data

def test_get_country_info(client):
    # Test case for getting info about a specific country
    # Assuming there's at least one country available for testing
    response = client.get('/sighting_data/countries/USA')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'country_sightings' in data or 'message' in data

def test_get_all_regions_by_country(client):
    # Test case for getting all regions by country
    # Assuming there's at least one country available for testing
    response = client.get('/sighting_data/countries/USA/regions')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'regions' in data or 'message' in data

def test_get_region_info(client):
    # Test case for getting info about a specific region
    # Assuming there's at least one region available for testing
    response = client.get('/sighting_data/countries/USA/regions/East')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'region_sightings' in data or 'message' in data

def test_get_all_cities_by_country_and_region(client):
    # Test case for getting all cities by country and region
    # Assuming there's at least one country and region available for testing
    response = client.get('/sighting_data/countries/USA/regions/East/cities')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'cities' in data or 'message' in data

def test_get_city_info(client):
    # Test case for getting info about a specific city
    # Assuming there's at least one city available for testing
    response = client.get
