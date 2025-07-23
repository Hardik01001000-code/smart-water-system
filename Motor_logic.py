# Determines whether motor should be ON or OFF based on tank level and overflow risk

def evaluate_motor_state(json_object, water_level, overflow):
    water_percent = (water_level/json_object['Tank_Capacity']) * 100
    overflow_percent = (overflow/json_object['Tank_Capacity']) * 100
    if water_percent + overflow_percent > 95:
        return "OFF"
        # Add code to turn off the motor
    else:
        return "ON"
        # Add code to turn on the motor

def motor_control(evaluate_motor_state):
    # Placeholder for actual GPIO-based motor control (not implemented in simulation)
    pass

"""def main():
    evaluate_motor_state(...)

if __name__ == '__main__':
    main()"""