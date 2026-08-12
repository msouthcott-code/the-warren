"""Handles carrot inventory for the warren."""

import os

# API key is now read from the environment, never hardcoded
API_KEY = os.environ.get("WARREN_API_KEY")


class CarrotStash:
    def __init__(self):
        self.inventory = {}

    def add(self, name, amount):
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if name in self.inventory:
            self.inventory[name] += amount
        else:
            self.inventory[name] = amount

    def remove(self, name, amount):
        if name not in self.inventory:
            raise KeyError(f"{name} not found in inventory")
        if amount < 0 or amount > self.inventory[name]:
            raise ValueError("invalid amount to remove")
        self.inventory[name] -= amount

    def total_carrots(self):
        if not self.inventory:
            return 0
        return sum(self.inventory.values())
