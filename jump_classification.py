import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the accelerometer data (update the file path as needed)
file_path = 'C:/Users/NoMan/Downloads/low-2024-12-08_22-57-30/Accelerometer.csv'  # Replace with your actual file path
accelerometer_data = pd.read_csv(file_path)

# Extract z-axis acceleration and time
z_axis = accelerometer_data['z']
time_elapsed = accelerometer_data['seconds_elapsed']

# Detect peaks in the z-axis acceleration
peaks, _ = find_peaks(z_axis, height=0, distance=50)  # Adjust 'height' and 'distance' as needed

# Create a DataFrame for the detected peaks
peak_values = z_axis[peaks]
peak_times = time_elapsed[peaks]
peak_data = pd.DataFrame({
    'Time (s)': peak_times,
    'Peak Acceleration (m/s²)': peak_values
})

# Filter for low jumps: Peak acceleration between 15 and 35 m/s²
low_jump_filtered = peak_data[
    (peak_data['Peak Acceleration (m/s²)'] >= 15) & 
    (peak_data['Peak Acceleration (m/s²)'] < 35)
].reset_index(drop=True)

# Visualize the filtered low jumps
# Plot the z-axis acceleration over time
plt.figure(figsize=(12, 6))
plt.plot(time_elapsed, z_axis, label='Z-axis Acceleration', color='blue')
plt.scatter(low_jump_filtered['Time (s)'], low_jump_filtered['Peak Acceleration (m/s²)'], color='red', label='Low Jumps (15-35 m/s²)', zorder=5)
plt.title('Z-Axis Acceleration with Filtered Low Jumps')
plt.xlabel('Seconds Elapsed')
plt.ylabel('Z-axis Acceleration (m/s²)')
plt.axhline(y=15, color='green', linestyle='--', label='Lower Threshold (15 m/s²)')
plt.axhline(y=35, color='orange', linestyle='--', label='Upper Threshold (35 m/s²)')
plt.grid()
plt.legend()
plt.show()

# Summary of the filtered low jump dataset
print("Filtered Low Jump Dataset:")
print(low_jump_filtered)
