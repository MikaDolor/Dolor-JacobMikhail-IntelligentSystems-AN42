# ==========================================
# TASK 1: Set Up the Environment Functions
# ==========================================

def initialize_environment():
    """Asks user for the initial state of Room A and Room B."""
    rooms = {}
    print("--- Environment Setup ---")
    for room in ['A', 'B']:
        while True:
            state = input(f"Enter initial state for Room {room} (clean/dirty): ").strip().lower()
            if state in ['clean', 'dirty']:
                rooms[room] = state
                break
            print("Invalid input! Please enter 'clean' or 'dirty'.")
    return rooms

def is_dirty(rooms, room_name):
    """Checks if a room is dirty."""
    return rooms.get(room_name) == 'dirty'

def clean_room(rooms, room_name):
    """Cleans a room."""
    if room_name in rooms:
        rooms[room_name] = 'clean'


# ==========================================
# TASK 2: Implement the Rule-Based Agent
# ==========================================

class VacuumAgent:
    def __init__(self, start_room='A'):
        self.current_room = start_room

    def move(self):
        """Switches the agent's location to the other room."""
        if self.current_room == 'A':
            self.current_room = 'B'
        else:
            self.current_room = 'A'

    def perceive_and_act(self, environment):
        """
        Perceives room state and executes rules:
        - Rule 1: If dirty, clean it.
        - Rule 2: If clean, move to the other room.
        """
        if is_dirty(environment, self.current_room):
            clean_room(environment, self.current_room)
            return "Cleaned"
        else:
            self.move()
            return "Moved"


# ==========================================
# TASK 3: Run the Simulation
# ==========================================

def main():
    # 1. Initialize environment from user input (Task 1)
    environment = initialize_environment()
    
    # Initialize agent in Room A (Task 2)
    agent = VacuumAgent(start_room='A')

    # 2. Ask user for number of steps (Task 3)
    print("\n--- Simulation Configuration ---")
    while True:
        try:
            num_steps = int(input("Enter number of steps to run the simulation: "))
            if num_steps > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"\nInitial Environment State: {environment}")
    print("Starting simulation...\n" + "=" * 40)

    # 3. Run the agent in a loop for the specified steps (Task 3)
    for step in range(1, num_steps + 1):
        # Record location before action (for logging)
        location_before = agent.current_room
        
        # Agent perceives and acts
        action = agent.perceive_and_act(environment)

        # 4. Print status after each step
        print(f"Step {step}:")
        print(f"  • Current Location: Room {location_before}")
        print(f"  • Action Taken:     {action}")
        print(f"  • Environment State: {environment}")
        print("-" * 40)

if __name__ == "__main__":
    main()