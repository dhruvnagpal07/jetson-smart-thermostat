# 🌡️ Jetson Nano Smart Thermostat Web App

An automated climate control system built on the **Nvidia Jetson Nano**, featuring a live mobile web dashboard, a **DHT11 Temperature Sensor**, and an **HW-039 (BTS7960) High-Power H-Bridge Driver** to dynamically switch a cooling fan.

## 🚀 Features
- **Mobile IoT Dashboard:** Built a responsive Flask web interface accessible across any local Wi-Fi device to set real-time temperature thresholds.
- **Hardware Integration:** Configured physical pin tracking via Python `Jetson.GPIO` to trigger high-current motor drivers safely.
- **Automated Control Logic:** The H-bridge gates engage instantly when local environment metrics exceed user-defined temperature limits.

## 🛠️ Hardware Component List
- Nvidia Jetson Nano (Developer Kit)
- HW-039 / BTS7960 High-Power Motor Driver
- DHT11 Temperature & Humidity Sensor
- DC Cooling Fan & 9V External Battery Supply
- Solderless Breadboard & Jumper Wires

## 🔌 Hardware Wiring Diagram Setup
- **HW-039 Driver Logic:** VCC, R_EN, and L_EN tied to **Jetson Pin 2 (5V)**. GND tied to **Jetson Pin 6 (GND)**.
- **Motor Control Signal:** RPWM tied to **Jetson Pin 11 (GPIO 17)**.
- **Sensor Input:** DHT11 Data line mapped to **Jetson Pin 12 (GPIO 18)**.

## 💻 Software Installation & Usage
1. Clone the repository and install requirements:
   ```bash
   pip3 install -r requirements.txt
