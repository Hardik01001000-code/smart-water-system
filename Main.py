# This file executes all the modules and runs the program.
from datetime import datetime
from Data import store_data_tank, cycle_data
from Water_level import tank_level, visual_bar, get_water_level
from Motor_logic import evaluate_motor_state, motor_control
from Calculations import extra_water, overflow_check

"""Main function to run the smart water tank cycle simulation."""
def main():
    # Step 1: Load tank configuration from file or prompt user for first-time setup
    json_object = store_data_tank() # Litres
    excess_water = extra_water(json_object) # Litres

    # Step 2: Check the water level
    water_level = get_water_level() # Litres
    tank_level_percentage = tank_level(water_level, json_object) # Percentage
    print(visual_bar(tank_level_percentage))

    # Step 3: React based on the water level
    motor_state = evaluate_motor_state(json_object, water_level, excess_water) # use check_motor_state() for actual motor state
    print(f"Motor state: {motor_state}")

    # Step 4: If motor is ON, simulate tank filling with user input
    if motor_state == "ON":
        motor_control(motor_state) # Placeholder for actual motor control
        start_time = datetime.now()
        # Taking ending (or current) level of the tank
        while True:
            try:
                current_level = int(input("Enter the current level of tank: ")) # Replace this input with actual sensor data in real implementation
                ########
                # No need to evaluate this when using a sensor
                if current_level > json_object['Tank_Capacity']:
                    print(f"Tank can't exceed its capacity of {json_object['Tank_Capacity']}L.")
                    continue
                ########
            except ValueError:
                print("Invalid input. Try again.")
                continue
            print(visual_bar(current_level))
            current_state = evaluate_motor_state(json_object, current_level, excess_water)
            print(f"Motor state: {current_state}")
            if current_state == "OFF":
                motor_control(current_state)
                # Simulate motor turning off
                end_time = datetime.now()
                overflow = round(overflow_check(current_level, excess_water, json_object), 3)
                break
        duration = end_time - start_time
        total_seconds = int(duration.total_seconds())  # Convert to whole seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        formatted_duration = f"{hours}h {minutes}m {seconds}s"
        cycle_data(water_level, current_level, json_object, formatted_duration, overflow)

if __name__ == '__main__':
    main()