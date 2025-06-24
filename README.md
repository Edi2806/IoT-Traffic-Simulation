# 🚦 IoT Traffic Simulation

A smart traffic control simulation using **SUMO**, **MQTT**, **Node-RED**, and **Python** to analyze and optimize urban traffic flow. This project demonstrates how IoT sensors can monitor vehicle activity and publish real-time data for visualization and analysis.
![System Overview](docs/system_diagram.png)

---

## 🔧 Technologies Used

- **SUMO**: Microscopic traffic simulation
- **Python**: Data processing and MQTT publishing
- **Node-RED**: Real-time dashboard and control logic
- **MQTT (Mosquitto)**: Lightweight IoT messaging protocol
- **Jupyter Notebook**: Traffic data analysis

---

## 📂 Project Structure

```plaintext
📂 IoT_Traffic_Simulation/
├── sumo_config/
│   ├── iot_network.net.xml
│   ├── iot_routes.rou.xml
│   ├── iot_detectors.add.xml
│   ├── iot_detector_output.xml
│   ├── iot_simulation.sumocfg
├── mqtt/
│   ├── mqtt_publish_traffic.py
│   ├── mqtt_node_red_flow.json
├── analysis/
│   ├── analyse_detector_dat.py
│   ├── iot_traffic_analysis.ipynb
├── docs/
```

---

## 🧪 How to Run the Simulation

1. Launch SUMO with the config file:
```bash
sumo-gui sumo_config/iot_simulation.sumocfg
```

2. View detector output in `iot_detector_output.xml` after simulation.

---

## 📡 MQTT Data Publishing

Run this script to publish traffic data from detectors via MQTT:
```bash
python3 mqtt/mqtt_publish_traffic.py
```

You can use a local MQTT broker like Mosquitto, or connect to an external broker.

---

## 📊 Node-RED Dashboard

Import the flow from:
```
mqtt/mqtt_node_red_flow.json
```

View live traffic data such as:
- Vehicle count
- Speed
- Occupancy rate
- Congestion alerts

---

## 📈 Data Analysis

Open the notebook:
```
analysis/iot_traffic_analysis.ipynb
```

Analyze trends, compare signal control strategies, and visualize traffic flow with Python.

---

## 🌱 Future Improvements

- Integrate predictive traffic control using ML
- Add emergency vehicle prioritization
- Expand intersection logic and timing optimization

---
