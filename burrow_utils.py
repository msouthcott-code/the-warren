def greet_bunny(name):
    print("Welcome to the warren, " + name + "!")


def format_report(total):
    return "Total deliveries: " + str(total)


def calculate_burrow_capacity(rooms: int, bunnies_per_room: int) -> float:
    """Return total burrow capacity in bunnies."""
    return rooms * bunnies_per_room * 1.0
