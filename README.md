# Rule-Based Vacuum Agent

**CS0065 – Intelligent Systems | Technical Assessment 2**
Rembrandt V. Coritana · Section AN41

A simple rule-based agent in Python that cleans two rooms (Room A and Room B). The agent perceives the state of its current room and acts according to fixed rules.

## How It Works

The program follows two rules at every step:

1. **If the current room is dirty → clean it.**
2. **If the current room is clean → move to the other room.**

These rules are implemented in the `perceive_and_act()` method of the `VacuumAgent` class.

## How to Run

```bash
python TA2_Coritana.py
```

You will be asked to enter:

1. The initial state of Room A (`dirty` or `clean`)
2. The initial state of Room B (`dirty` or `clean`)
3. The number of simulation steps (a whole number greater than 0)

Invalid inputs are rejected and the prompt is repeated.

## Program Structure

| Part | Description |
|------|-------------|
| `ask_steps()` | Asks for the number of steps and validates the input |
| `get_room_state(room_name)` | Asks for a room's initial state and validates the input |
| `VacuumAgent` | The agent class, which starts in Room A |
| `current_room()` | Returns the room the agent is currently in |
| `is_dirty()` | Checks if the current room is dirty |
| `clean_room()` | Sets the current room to clean |
| `move()` | Switches the agent between Room A and Room B |
| `perceive_and_act()` | Applies the two rules above |

Rooms are stored as dictionaries, e.g. `{"name": "Room A", "state": "dirty"}`.


