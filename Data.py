from datetime import datetime
import json
from Water_level import tank_level

# Load or initialize tank configuration data (only needed once per setup)
def store_data_tank():
    try:
        with open('Constant.json', 'r') as openfile:
            # Trying to open Constant.json file
            json_object = json.load(openfile)
            return json_object
    except:
        # If file doesn't exist, prompt for initial configuration (simulates sensor calibration)
        Tank_Capacity = int(input("Enter the tank capacity in liters: "))
        Pipe_Diameter = float(input("Enter the pipe diameter in cm: "))
        Pipe_Length = float(input("Enter the pipe length in meters: "))
        Flow_Rate = float(input("Enter the flow rate in liters per minute (L/min): ")) # Use sensor/calibrate for accurate flow rate
        time_delay = int(input("Enter the time delay in seconds: "))  # seconds

        data = {
            "Tank_Capacity": Tank_Capacity,
            "Pipe_Diameter": Pipe_Diameter,
            "Pipe_Length": Pipe_Length,
            "Flow_Rate": Flow_Rate,
            "Time_Delay": time_delay
        }
        json_object = json.dumps(data, indent=4)
        with open("Constant.json", "w") as outfile:
            outfile.write(json_object)

        with open('Constant.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object

# Store each cycle's data in Data.json for later analysis
def cycle_data(start_level, end_level, json_object, duration, overflow):
    data = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Tank starting level": tank_level(start_level, json_object), # Taken form Water_level.py
        "Tank ending level": tank_level(end_level, json_object), # Taken form Water_level.py
        "Motor on time": str(duration), # in HH:MM:SS
        "Overflow": f"{overflow} Litres", # Litres
    }
    # Still have to improve
    try:
        with open("Data.json", "r") as file:
            logs = json.load(file)
    except:
        logs = []

    logs.append(data)

    try:
        with open("Data.json", "w") as file:
            json.dump(logs, file, indent=4)
    except Exception as e:
        print(f"Failed to save log: {e}")