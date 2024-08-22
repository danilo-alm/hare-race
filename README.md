
# 🐇 Hare Race Simulation with Threads, Semaphores, and Monitors

This project simulates a hare race using concurrent programming concepts such as threads, semaphores, and monitors. The goal is to demonstrate the coordination of multiple threads competing in a race while the race state is monitored and displayed in real-time.

## 🎯 Objective

The simulation creates several threads, each representing a hare. These threads compete in a race, with their progress managed by semaphores and monitored through synchronization conditions. The project showcases how to coordinate the execution of concurrent threads to achieve a common goal.

## 🛠️ Features

- **Multithreaded Race**: Each hare is represented by a thread that advances in the race by jumping and resting randomly.
- **Semaphores**: Controls the number of hares that can jump simultaneously.
- **Monitors and Locks**: Synchronizes threads to ensure data consistency and correct ranking updates.
- **Real-Time Display**: The race progress is displayed in real-time in the terminal, showing each hare's advancement until the finish line.

## 📁 Code Structure

- **`Semaphore`**: Custom semaphore implementation to control thread access to critical sections.
- **`Hare`**: Class representing a hare in the race, with methods for jumping and resting.
- **`hare_behaviour`**: Function that defines each hare's behavior during the race, including jumping, resting, and updating the ranking.
- **`monitor_race`**: Function that monitors the race's state, printing the hares' progress at regular intervals.
- **`print_race_state`**: Function that visually displays each hare's progress in the race, updating the terminal screen.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/danilo-alm/hare-race.git
   cd hare-race
   ```

2. Ensure you have Python installed on your machine.

3. Run the simulation:
   ```bash
   python race.py
   ```

## 📝 Example Output

During execution, the race state will be displayed in real-time in the terminal. Each hare's progress will be shown by a bar of `#` characters, indicating the distance covered:

```
Speedy               - ######    |
Hopper               - ####      |
Dash                 - ########  |
```

## 🔧 Configuration

You can adjust some race parameters, such as the total distance (`RACE_DISTANCE`), maximum jump distance (`JUMP_MAX_DISTANCE`), and maximum rest time (`MAX_REST_SECONDS`) in the `values.py` file.
