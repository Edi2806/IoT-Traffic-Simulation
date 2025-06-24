import json
import time
import xml.etree.ElementTree as ET
import paho.mqtt.client as mqtt

# MQTT Broker Settings
broker = "localhost"
port = 1883
topic_prefix = "traffic/sensors/"

# Load the detector XML output
tree = ET.parse("iot_detector_output.xml")
root = tree.getroot()

# Create MQTT client
client = mqtt.Client()
client.connect(broker, port, 60)

# Loop through all intervals
for interval in root.findall("interval"):
    loop_id = interval.get("id")
    speed_raw = interval.get("speed")
    occupancy_raw = interval.get("occupancy")

    # Skip invalid values
    if speed_raw is None or float(speed_raw) < 0:
        continue

    # Parse valid values
    speed = float(speed_raw)
    occupancy = float(occupancy_raw)
    end_time = float(interval.get("end"))
    vehicle_count = int(interval.get("nVehContrib", 0))

    payload = {
        "loop_id": loop_id,
        "time": end_time,
        "speed": speed,
        "occupancy": occupancy,
        "vehicle_count": vehicle_count
    }

    client.publish(topic_prefix + loop_id, json.dumps(payload))
    print(f"Published to {topic_prefix + loop_id}: {payload}")
    time.sleep(0.2)

client.disconnect()
print("MQTT publishing complete.")
