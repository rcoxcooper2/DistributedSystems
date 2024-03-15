# Turbidity Analysis Script

## Overview

This project contains a Python script for analyzing turbidity data from a water quality dataset. The script calculates the average turbidity from the most recent five measurements, checks if the turbidity is below a safe threshold, and estimates the minimum time required for turbidity to fall below the safe threshold.

## Folder Contents

- `turbidity_test.py`: The main Python script containing functions for turbidity analysis.
- `test_functions.py`: Unit tests for the turbidity analysis functions.
- `turbidity_data.json`: JSON file containing water quality data.

## Instructions

### Downloading the Dataset

1. Visit the original data source at [https://alt-61aa8d434113f.blackboard.com/bbcswebdav/pid-5045476-dt-content-rid-49586531_1/courses/CSC-488-01-222/Homeworks/turbidity_data.json?one_hash=BCC428C6C803513A54E4933C58EE0E44&f_hash=EEFE130F38C67164A9036D33A09EF17E].
2. Download the water quality dataset in JSON format.
3. Save the downloaded file as `turbidity_data.json` in the project directory.

### Running the Script

1. Ensure you have Python installed on your machine.
2. Install required dependencies using `pip install -r requirements.txt` (if any).
3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Run the script


### Interpretation of Results

The script outputs the average turbidity based on the most recent five measurements, a warning if turbidity is above the safe threshold, and the minimum time required for turbidity to fall below the safe threshold.

Example Output:

Average turbidity based on most recent five measurements = 1.2000 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
