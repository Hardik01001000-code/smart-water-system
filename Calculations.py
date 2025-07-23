# Taking right dimensions is very important

# Water flowed after turning off the motor due to the time delay
def extra_water(json_object):
    time_delay = json_object['Time_Delay']  # seconds
    water = json_object['Flow_Rate']*(time_delay/60) # Litres
    return round(water, 3)

# Overflow calculation
def overflow_check(current_level, added_water, json_object):
    tank_capacity = json_object["Tank_Capacity"]
    final_level = current_level + added_water
    overflow = max(0, final_level - tank_capacity)
    if overflow > 0:
        print(f"⚠️ Overflow occurred: {overflow:.3f} litres")
        return overflow
    else:
        print("No overflow")
    return 0

"""def main():
    return extra_water(...)

if __name__ == '__main__':
    main()
"""