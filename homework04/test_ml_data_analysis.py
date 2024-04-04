import pytest
from ml_data_analysis import compute_average_mass, check_hemisphere, count_classes

# Sample data for testing
sample_data = {
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
    {
      "name": "Beeler",
      "id": "10002",
      "recclass": "H6",
      "mass (g)": "720",
      "reclat": "56.18333",
      "reclong": "10.23333",
      "GeoLocation": "(56.18333, 10.23333)"
    },
    
  ]
}

# Test compute_average_mass function
def test_compute_average_mass():
    average_mass = compute_average_mass(sample_data['meteorite_landings'], 'mass (g)')
    assert average_mass == 370.5  

# Test check_hemisphere function
def test_check_hemisphere():
    assert check_hemisphere(50.775, 6.08333) == 'Northern & Eastern'
    assert check_hemisphere(-33.16667, -64.95) == 'Southern & Western'
    

# Test count_classes function
def test_count_classes():
    class_counts = count_classes(sample_data['meteorite_landings'], 'recclass')
    assert class_counts['L5'] == 1
    assert class_counts['H6'] == 1
    


if __name__ == '__main__':
    pytest.main()
