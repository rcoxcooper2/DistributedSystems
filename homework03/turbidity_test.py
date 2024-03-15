import json
from typing import List, Dict
from datetime import datetime, timedelta
import math

def calculate_turbidity(calibration_constant: float, detector_current: float) -> float:
    """
    Calculate turbidity using the nephelometer equation.

    T = a0 * I90
    T = Turbidity in NTU Units (0 – 40)
    a0 = Calibration constant
    I90 = Ninety degree detector current
    """
    return calibration_constant * detector_current

def calculate_minimum_time(turbidity_threshold: float, current_turbidity: float, decay_factor: float) -> float:
    """
    Calculate the minimum time to fall below the safe threshold using the exponential decay function.

    Ts > T0(1-d)**b
    Ts = Turbidity threshold for safe water
    T0 = Current turbidity
    d = decay factor per hour, expressed as a decimal
    b = hours elapsed

    revised equation to get time: b= (ln(Ts/T0))/-d
 
    """
    if current_turbidity <= turbidity_threshold:
        return 0  # Turbidity is already below the threshold

    return math.log(turbidity_threshold / current_turbidity) / -decay_factor

with open('homework03/turbidity_data.json', 'r') as file:
    data = json.load(file)

turbidity_data = data.get('turbidity_data', [])

# Extract the most recent five data points
last_five = turbidity_data[-5:]

# Calculate the average turbidity from the most recent five data points
average_turbidity = sum(entry['sample_volume'] for entry in last_five) / len(last_five)

# Check if average turbidity is below the safe threshold
turbidity_threshold = 1.5 
is_below_threshold = average_turbidity < turbidity_threshold

# Print the average turbidity and whether it is below the safe threshold
print(f"Average turbidity based on most recent five measurements = {average_turbidity:.4f} NTU")
if is_below_threshold:
    print("Info: Turbidity is below threshold for safe use")
else:
    print("Info: urbidity is above threshold for safe use")

# Calculate the minimum time required to fall below the safe threshold
current_time = datetime.strptime(last_five[-1]['datetime'], "%Y-%m-%d %H:%M")
current_turbidity = last_five[-1]['sample_volume']
decay_factor = 0.02 
min_time_to_threshold = calculate_minimum_time(turbidity_threshold, current_turbidity, decay_factor)

# Print the minimum time required to fall below the safe threshold
print(f"Minimum time required to return below a safe threshold = {min_time_to_threshold:.2f} hours")


