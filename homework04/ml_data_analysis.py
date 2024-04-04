import json
import logging
import sys

format_str = '[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)

def compute_average_mass(a_list_of_dicts, a_key_string):
    if len(a_list_of_dicts) == 0:
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return total_mass / len(a_list_of_dicts)

def check_hemisphere(latitude, longitude):
    if latitude == 0 or longitude == 0:
        raise ValueError
    location = 'Northern' if latitude > 0 else 'Southern'
    location += ' & Eastern' if longitude > 0 else ' & Western'
    return location

def count_classes(a_list_of_dicts, a_key_string):
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return classes_observed

def main():
    logging.debug('entering main loop')

    if len(sys.argv) != 2:
        print("Usage: ml_data_analysis.py <JSON_FILE>")
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as f:
            ml_data = json.load(f)
    except FileNotFoundError:
        print("Error: File '{}' not found.".format(file_name))
        sys.exit(1)

    print("{} Summary data following meteorite analysis:".format(file_name))
    print("Average mass of {} meteor(s):".format(len(ml_data['meteorite_landings'])))
    print("{} grams".format(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)')))

    hemisphere_summary = {}
    for row in ml_data['meteorite_landings']:
        hemisphere = check_hemisphere(float(row['reclat']), float(row['reclong']))
        if hemisphere in hemisphere_summary:
            hemisphere_summary[hemisphere] += 1
        else:
            hemisphere_summary[hemisphere] = 1

    print("Hemisphere summary data:")
    for hemisphere, count in hemisphere_summary.items():
        print("There were {} meteors found in the {} quadrant".format(count, hemisphere))

    print("Class summary data:")
    class_summary = count_classes(ml_data['meteorite_landings'], 'recclass')
    for meteor_class, count in class_summary.items():
        print("The {} class was found {} times".format(meteor_class, count))

if __name__ == '__main__':
    main()
