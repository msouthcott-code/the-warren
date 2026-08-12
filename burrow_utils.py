def greet_bunny(name):
    print("Welcome to the warren, " + name + "!")


def format_report(total):
    # string concatenation of an int without str() - will raise TypeError
    return "Total deliveries: " + total


def calculate_burrow_capacity(rooms, bunnies_per_room):
    # no type hints, no docstring, unclear units
    return rooms * bunnies_per_room * 1.0


def unused_helper():
    x = 42
    y = "never used"
    return x
