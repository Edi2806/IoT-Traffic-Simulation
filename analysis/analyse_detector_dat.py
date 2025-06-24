import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Load detector data
tree = ET.parse("iot_detector_output.xml")
root = tree.getroot()

data = []

for interval in root.findall("interval"):
    time = float(interval.get("begin"))
    speed = float(interval.get("speed"))
    occupancy = float(interval.get("occupancy"))
    data.append({"time": time, "speed": speed, "occupancy": occupancy})

df = pd.DataFrame(data)

# Group by time
grouped = df.groupby("time").mean()

# Plotting
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(grouped.index, grouped["speed"], label="Speed (m/s)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Speed")
plt.title("Average Speed Over Time")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(grouped.index, grouped["occupancy"], label="Occupancy (%)", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Occupancy")
plt.title("Lane Occupancy Over Time")
plt.grid(True)

plt.tight_layout()
plt.show()
