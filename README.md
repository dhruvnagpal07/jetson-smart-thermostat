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

## 🔌 Hardware Wiring & Pinout Reference

To protect the Jetson Nano's 3.3V logic rails, the **HW-039 (BTS7960)** driver isolates high-current inductive motor spikes using a dual-channel configuration, while logic rails are linked to the expansion header.

### 1. Jetson Nano to HW-039 (BTS7960) Driver Map
| Jetson Nano Physical Pin | Pin Name / Function | HW-039 Driver Connection | Description |
| :--- | :--- | :--- | :--- |
| **Pin 2** | 5V Power | `VCC`, `R_EN`, `L_EN` | Powers logic gates & pulls Enable lines HIGH |
| **Pin 6** | GND (Ground) | `GND` | Establishes common logic ground reference |
| **Pin 11** | GPIO 17 (Digital Output) | `RPWM` | Sends digital signal to trigger forward drive |
| -- | External Battery (-) | `B-` | High-current ground return path for 9V rail |
| -- | External Battery (+) | `B+` | High-current power supply for DC motor |

### 2. Jetson Nano to DHT11 Sensor Map
| Jetson Nano Physical Pin | Pin Name / Function | DHT11 Sensor Pin | Description |
| :--- | :--- | :--- | :--- |
| **Pin 4** | 5V Power | `VCC` | Powers the sensor internal logic |
| **Pin 12** | GPIO 18 (Digital Input) | `DATA` / `OUT` | Pulls raw environmental pulse data stream |
| **Pin 14** | GND (Ground) | `GND` | Ground reference line |

## 💻 Software Installation & Usage
1. Clone the repository and install requirements:
   ```bash
   pip3 install -r requirements.txt

