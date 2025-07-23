# Handles water level input, conversion to percentage, and visualization bar

# Displays water level in the tank.
# Can be modified to use a real sensor.

# Simulates a sensor by asking user to input current tank level
def get_water_level():
    # In litres
    while True:
        try:
            level = int(input("Enter the current water level in litres: ")) # Replace this input with actual sensor data in real implementation
            return level
        except ValueError:
            print("Invalid input. Please enter a number.")

def tank_level(level, json_object):
    Tank_Capacity = json_object['Tank_Capacity']  # liters
    percent = int((level / Tank_Capacity) * 100) # Convert to percentage
    return percent

def visual_bar(level):
    percent = level
    bar = "█" * (percent // 10) + "-" * (10 - percent // 10)
    return f"Tank Level: [{bar}] {percent}%"

"""def main():
    bar(get_water_level)

if __name__ == '__main__':
    main()"""