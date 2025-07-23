💧 Smart Water Tank Monitoring System

A modular Python simulation to automate water tank monitoring, motor control, overflow prevention, and data logging—ready for future integration with sensors and hardware (e.g., flow sensors, ultrasonic tank level sensors).


📌 Features
📈 Tracks real-time tank water levels (manual or sensor input)

⚙️ Automatically switches motor ON/OFF

💦 Prevents overflow by estimating extra water from delay

📝 Logs each motor cycle with start/end tank level, duration, and overflow

📊 Visualizes tank data using Matplotlib

💾 Saves persistent configuration and logs using JSON files

🔧 Structured for easy integration with real sensors (GPIO or others)

🧩 File Structure
.
├── main.py             # Main execution logic
├── Data.py             # Data logging and config I/O
├── Water_level.py      # Water level input & visualization
├── Motor_logic.py      # Motor decision logic
├── Calculations.py     # Overflow and delay calculations
├── Graphs.py           # Data visualization using Matplotlib
├── Constant.json       # Tank setup config (auto-generated)
├── Data.json           # Logged tank usage history
├── requirements.txt    # Required python libraries

🚀 How to Run

python main.py

First-time setup will prompt for tank details. For later runs, it loads from Constant.json.

🛠 Future Sensor Integration
Replace the get_water_level() input with sensor reading logic (e.g., ultrasonic distance sensors for water level)
Replace input() in motor simulation with flow meter readings or GPIO controls
Use GPIO libraries (like RPi.GPIO or gpiozero) in motor_control() function in Motor_logic.py to turn motors ON/OFF

📈 Data Visualization
Run the graph viewer to visualize trends:

python Graphs.py

📦 Requirements
Python 3.x
matplotlib (for Graphs.py)

pip install matplotlib

🔐 Data Safety
Logs are stored in JSON, ensure proper permissions in embedded systems or networks

Consider log file rotation or export to cloud (if using in real-world applications)

📬 Contact
Made by Hardik ✨
Feel free to fork and improve this project!