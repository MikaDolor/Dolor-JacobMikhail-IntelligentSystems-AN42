# Function to initialize the environment with user input
def initialize_environment():
    rooms = {}
    print("--- Environment Setup ---")
    for room in ['A', 'B']:
        while True:
            state = input(f"Enter initial state for Room {room} (clean/dirty): ").strip().lower()
            if state in ['clean', 'dirty']:
                rooms[room] = state
                break
            print("Invalid input. Please enter 'clean' or 'dirty'.")
    return rooms

# Function to check if a specific room is dirty
def is_dirty(rooms, room_name):
    return rooms.get(room_name) == 'dirty'

# Function to clean a room
def clean_room(rooms, room_name):
    if room_name in rooms:
        rooms[room_name] = 'clean'
        print(f"Room {room_name} has been cleaned.")
    else:
        print(f"Room {room_name} does not exist.")


# Example execution
if __name__ == "__main__":
    # 1 & 2. Initialize environment with user input
    environment = initialize_environment()
    print("\nInitial Environment State:", environment)

    # 3. Check dirty status and clean
    for r in ['A', 'B']:
        if is_dirty(environment, r):
            print(f"Room {r} is dirty. Cleaning now...")
            clean_room(environment, r)
        else:
            print(f"Room {r} is already clean.")

    print("\nFinal Environment State:", environment)