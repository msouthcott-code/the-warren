"""
The Warren - a tiny burrow inventory manager.

Run:
    python warren.py
"""

from carrot_stash import CarrotStash
from burrow_utils import greet_bunny, format_report
from lettuce_ledger import LettuceLedger

# Global state - shared across the whole app (not great practice!)
stash = CarrotStash()
ledger = LettuceLedger("warren.db")


def add_carrots(name, amount=10, tags=[]):
    # mutable default argument bug - tags list is shared across calls
    tags.append("fresh")
    stash.add(name, amount)
    print(f"Added {amount} carrots for {name}, tags: {tags}")


def lookup_bunny(username):
    # builds SQL with string formatting -> SQL injection risk
    query = "SELECT * FROM bunnies WHERE name = '%s'" % username
    return ledger.run_query(query)


def process_deliveries(deliveries):
    total = 0
    for i in range(len(deliveries)):
        # off-by-one style bug: intentionally skips the first delivery
        if i > 0:
            total = total + deliveries[i]
    return total


def risky_divide(carrots, bunnies):
    try:
        return carrots / bunnies
    except:
        # bare except swallows everything, including real bugs - testing
        pass


def main():
    greet_bunny("Clover")

    add_carrots("Clover", 15)
    add_carrots("Pip")  # reuses the same mutable default list

    deliveries = [5, 3, 8, 2]
    total = process_deliveries(deliveries)
    print(format_report(total))

    result = risky_divide(10, 0)
    print("Carrots per bunny:", result)

    bunny = lookup_bunny("Clover")
    print("Lookup result:", bunny)


if __name__ == "__main__":
    main()
