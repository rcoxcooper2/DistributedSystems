from flask import Flask, jsonify, request
import xmltodict


app = Flask(__name__)

# Global variables to hold loaded data
positional_data = None
sighting_data = None


# Load positional and sighting data from XML files
@app.route('/load_data', methods=['POST'])
def load_data():
    global positional_data, sighting_data
    try:
        with open('positional.xml', 'r') as f_pos:
            positional_data = xmltodict.parse(f_pos.read())  # Parse positional XML data
            
        with open('sighting.xml', 'r') as f_sight:
            sighting_data = xmltodict.parse(f_sight.read())  # Parse sighting XML data
            
        app.logger.info('Data loaded successfully')
        return jsonify({'message': 'Data loaded successfully'})
    except Exception as e:
        app.logger.error(f'Error loading data: {e}')
        return jsonify({'message': 'Error loading data'})

# Information on how to interact with the application
@app.route('/', methods=['GET'])
def instructions():
    return jsonify({
        'message': 'Welcome to the ISS tracking application!',
        'instructions': {
            'load_positional_data': 'POST /load_positional_data',
            'load_sighting_data': 'POST /load_sighting_data',
            'get_all_epochs': 'GET /positional_data/epochs',
            'get_epoch_info': 'GET /positional_data/epochs/<epoch>',
            'get_all_countries': 'GET /sighting_data/countries',
            'get_country_info': 'GET /sighting_data/countries/<country>',
            'get_all_regions_by_country': 'GET /sighting_data/countries/<country>/regions',
            'get_region_info': 'GET /sighting_data/countries/<country>/regions/<region>',
            'get_all_cities_by_country_and_region': 'GET /sighting_data/countries/<country>/regions/<region>/cities',
            'get_city_info': 'GET /sighting_data/countries/<country>/regions/<region>/cities/<city>'
        }
    })

# Get all epochs in the positional data
@app.route('/positional_data/epochs', methods=['GET'])
def get_all_epochs():
    global positional_data
    if positional_data:
        state_vectors = positional_data['ndm']['oem']['body']['segment']['data']['stateVector']
        epochs = [state_vector['EPOCH'] for state_vector in state_vectors]
        return jsonify({'epochs': epochs})
    else:
        return jsonify({'message': 'No positional data loaded'})


# Get information about a specific epoch in the positional data
@app.route('/positional_data/epochs/<epoch>', methods=['GET'])
def get_epoch_info(epoch):
    global positional_data
    if positional_data:
        state_vectors = positional_data['ndm']['oem']['body']['segment']['data']['stateVector']
        for state_vector in state_vectors:
            if state_vector['EPOCH'] == epoch:
                return jsonify({'epoch_info': state_vector})
        return jsonify({'message': 'Epoch not found'})
    else:
        return jsonify({'message': 'No positional data loaded'})

# Get all countries from the sighting data
@app.route('/sighting_data/countries', methods=['GET'])
def get_all_countries():
    global sighting_data
    if sighting_data:
        countries = set()
        for sighting in sighting_data['visible_passes']['visible_pass']:
            countries.add(sighting['country'])
        return jsonify({'countries': list(countries)})
    else:
        return jsonify({'message': 'No sighting data loaded'})

# Get information about a specific country in the sighting data
@app.route('/sighting_data/countries/<country>', methods=['GET'])
def get_country_info(country):
    global sighting_data
    if sighting_data:
        country_sightings = []
        for sighting in sighting_data['visible_passes']['visible_pass']:
            if sighting['country'] == country:
                country_sightings.append(sighting)
        if country_sightings:    
            return jsonify({f'ISS Sightings in {country}': country_sightings})
        
        else:
            return jsonify({'message': 'Country not found'})
    else:
        return jsonify({'message': 'No sighting data loaded'})

# Get all regions associated with a given country in the sighting data
@app.route('/sighting_data/countries/<country>/regions', methods=['GET'])
def get_all_regions_by_country(country):
    global sighting_data
    if sighting_data:
        country_regions = set()
        for sighting in sighting_data['visible_passes']['visible_pass']:
            if sighting['country'] == country:
                country_regions.add(sighting['region'])
        if country_regions:
            return jsonify({'regions': list(country_regions)})
        else:
            return jsonify({'message': f'No regions found for {country}'})
    else:
        return jsonify({'message': 'No sighting data loaded'})

# Get information about all sightings for a specific region in the sighting data
@app.route('/sighting_data/countries/<country>/regions/<region>', methods=['GET'])
def get_region_info(country, region):
    global sighting_data
    if sighting_data:
        region_sightings = []
        for sighting in sighting_data['visible_passes']['visible_pass']:
            if sighting['country'] == country and sighting['region'] == region:
                region_sightings.append(sighting)
        if region_sightings:
            return jsonify({f'ISS Sightings in {region}, {country}': region_sightings})
        else:
            return jsonify({'message': f'No sightings found for {region}, {country}'})
    else:
        return jsonify({'message': 'No sighting data loaded'})

# Get all cities associated with a given country and region in the sighting data
@app.route('/sighting_data/countries/<country>/regions/<region>/cities', methods=['GET'])
def get_all_cities_by_country_and_region(country, region):
    global sighting_data
    if sighting_data:
        country_and_region_cities = set()
        country_found = False

        for sighting in sighting_data['visible_passes']['visible_pass']:
            if sighting['country'] == country:
                country_found = True
                if sighting['region'] == region:
                    country_and_region_cities.add(sighting['city'])

        if country_found:
            if country_and_region_cities:
                return jsonify({f'List of cities in {region}, {country}': list(country_and_region_cities)})
            else:
                return jsonify({'message': 'No cities found for the specified country and region'})
        else:
            return jsonify({'message': 'Country not found'})
    else:
        return jsonify({'message': 'No sighting data loaded'})

#Get all information associated with a given country, region and city
@app.route('/sighting_data/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def get_city_info(country, region, city):
    global sighting_data
    if sighting_data:
        country_found = False
        region_found = False
        city_sightings = []

        for sighting in sighting_data['visible_passes']['visible_pass']:
            if sighting['country'] == country:
                country_found = True
                if sighting['region'] == region:
                    region_found = True
                    if sighting['city'] == city:
                        city_sightings.append(sighting)

        if country_found:
            if region_found:
                if city_sightings:
                    return jsonify({f'ISS Sightings in {city}': city_sightings})
                else:
                    return jsonify({'message': f'No sightings found in {city}'})
            else:
                return jsonify({'message': f'Region not found in the {country}'})
        else:
            return jsonify({'message': 'Country not found'})
    else:
        return jsonify({'message': 'No sighting data loaded'})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
