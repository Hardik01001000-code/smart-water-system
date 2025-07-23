# Displays graphs and indications about the state of the system.
# Graphs.py
import json
from datetime import datetime
import matplotlib.pyplot as plt

def load_data(filepath="Data.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Data file not found.")
        return []

def convert_to_minutes(duration_str):
    """Convert 'Xh Ym Zs' to total minutes."""
    parts = duration_str.split()
    h = int(parts[0][:-1]) if 'h' in parts[0] else 0
    m = int(parts[1][:-1]) if len(parts) > 1 else 0
    s = int(parts[2][:-1]) if len(parts) > 2 else 0
    return h * 60 + m + s / 60

def plot_data():
    data = load_data()
    if not data:
        return

    timestamps = [datetime.strptime(entry["Time"], "%Y-%m-%d %H:%M:%S") for entry in data]
    start_levels = [entry["Tank starting level"] for entry in data]
    end_levels = [entry["Tank ending level"] for entry in data]
    durations = [convert_to_minutes(entry["Motor on time"]) for entry in data]
    overflows = [float(entry["Overflow"].split()[0]) for entry in data]

    # Plot 1: Tank Levels
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, start_levels, label="Start Level (%)", marker='o')
    plt.plot(timestamps, end_levels, label="End Level (%)", marker='x')
    plt.title("Tank Levels Over Time")
    plt.xlabel("Time")
    plt.ylabel("Tank Level (%)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 2: Motor Duration
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, durations, color='orange', marker='s')
    plt.title("Motor Run Duration (minutes)")
    plt.xlabel("Time")
    plt.ylabel("Duration (min)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 3: Overflow
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, overflows, color='red', marker='^')
    plt.title("Overflow Over Time (litres)")
    plt.xlabel("Time")
    plt.ylabel("Overflow (litres)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data()