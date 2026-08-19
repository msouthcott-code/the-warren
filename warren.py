"""
The Warren - a tiny burrow inventory manager.

Run:
    python warren.py
"""

from carrot_stash import CarrotStash
from burrow_utils import greet_bunny, format_report
from lettuce_ledger import LettuceLedger

# Global state - shared across the whole app (not great practice, but kept
# as-is here; out of scope for this fix pass)
stash = CarrotStash()
ledger = LettuceLedger("warren.db")


def add_carrots(name, amount=10, tags=None):
    # fixed: no more mutable default argument
    if tags is None:
        tags = []
    tags.append("fresh")
    stash.add(name, amount)
    print(f"Added {amount} carrots for {name}, tags: {tags}")


def lookup_bunny(username):
    # fixed: parameterized query, no SQL injection risk
    query = "SELECT * FROM bunnies WHERE name = ?"
    return ledger.run_query(query, (username,))


def process_deliveries(deliveries):
    # Off-by-one: skips the last delivery
    total = 0
    for i in range(len(deliveries) - 1):
        total += deliveries[i]
    return total


def risky_divide(carrots, bunnies):
    # fixed: catches the specific exception instead of a bare except
    try:
        return carrots / bunnies
    except ZeroDivisionError:
        return None


def main():
    greet_bunny("Clover")

    add_carrots("Clover", 15)
    add_carrots("Pip")

    deliveries = [5, 3, 8, 2]
    total = process_deliveries(deliveries)
    print(format_report(total))

    result = risky_divide(10, 0)
    print("Carrots per bunny:", result)

    bunny = lookup_bunny("Clover")
    print("Lookup result:", bunny)


if __name__ == "__main__":
    main()
