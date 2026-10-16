import time

# Get the number of simulation steps
def ask_steps():
    while True:
        try:
            steps = int(input("Enter the number of steps: "))

            if steps > 0:
                return steps
            print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Get the initial state of each room
def get_room_state(room_name):
    while True:
        state = input(f"Enter the state of {room_name} (dirty/clean): ").strip().lower()

        if state in ["dirty", "clean"]:
            return state

        print("Invalid input. Please enter 'dirty' or 'clean'.")


class VacuumAgent:

    def __init__(self, environment):
        self.environment = environment
        self.position = 0

    def current_room(self):
        return self.environment[self.position]

    def is_dirty(self):
        return self.current_room()["state"] == "dirty"

    def clean_room(self):
        room = self.current_room()
        room["state"] = "clean"
        print(f"Action: {room['name']} was cleaned.")

    def move(self):
        # Switch between Room A and Room B
        self.position = 1 - self.position
        print(f"Action: Moving to {self.current_room()['name']}.")

    def perceive_and_act(self):
        if self.is_dirty():
            self.clean_room()
        else:
            time.sleep(0.5)
            self.move()


# -----------------------------
# Create the environment
# -----------------------------

room_a = {
    "name": "Room A",
    "state": get_room_state("Room A")
}

room_b = {
    "name": "Room B",
    "state": get_room_state("Room B")
}

environment = [room_a, room_b]


# Display initial room conditions
print("\nInitial Environment:")
for room in environment:
    print(f"{room['name']}: {room['state']}")


# Get simulation length
total_steps = ask_steps()

agent = VacuumAgent(environment)


# -----------------------------
# Run the agent
# -----------------------------

print("\n--- Simulation Started ---")

for step in range(1, total_steps + 1):

    print(f"\nStep {step}")
    print(f"Agent Location: {agent.current_room()['name']}")

    agent.perceive_and_act()

    print("Environment State:")
    for room in environment:
        print(f"  {room['name']}: {room['state']}")


print("\n--- Simulation Finished ---")
print("The vacuum agent has completed the simulation.")