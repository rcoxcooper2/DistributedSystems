from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load JSON data from file
def load_data():
    with open('ny_env_data.json', 'r') as f:
        data = json.load(f)
    return data

# Save JSON data to file
def save_data(data):
    with open('ny_env_data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Endpoint to retrieve all data
@app.route('/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)

# Endpoint to retrieve data for a specific ID
@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    data = load_data()
    if str(id) in data:
        return jsonify(data[str(id)])
    else:
        return jsonify({'message': 'Data not found'}), 404

# Endpoint to retrieve data by regulation ID
@app.route('/data/regulation/<regulation_id>', methods=['GET'])
def get_data_by_regulation_id(regulation_id):
    data = load_data()
    result = [value for value in data.values() if value['regulation_id'] == regulation_id]
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Data not found'}), 404

# Endpoint to retrieve data by agency
@app.route('/data/agency/<agency>', methods=['GET'])
def get_data_by_agency(agency):
    data = load_data()
    result = [value for value in data.values() if value['agency'] == agency]
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Data not found'}), 404

# Endpoint to retrieve data by sector
@app.route('/data/sector/<sector>', methods=['GET'])
def get_data_by_sector(sector):
    data = load_data()
    result = [value for value in data.values() if value['sector'] == sector]
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Data not found'}), 404

# Endpoint to retrieve data by status
@app.route('/data/status/<status>', methods=['GET'])
def get_data_by_status(status):
    data = load_data()
    result = [value for value in data.values() if value['status'] == status]
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
