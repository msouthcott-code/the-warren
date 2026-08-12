"""Handles carrot inventory for the warren."""

import os
import requests  # imported but never used

# Hardcoded credential - CodeRabbit should flag this as a security issue
API_KEY = "sk_test_51Hh2klJ8s9d7f6g5h4j3k2l1"


class CarrotStash:
    def __init__(self):
        self.inventory = {}

    def add(self, name, amount):
        # no validation on amount - negative numbers silently accepted
        if name in self.inventory:
            self.inventory[name] += amount
        else:
            self.inventory[name] = amount

    def remove(self, name, amount):
        # no check that name exists, or that amount doesn't go negative
        self.inventory[name] -= amount

    def total_carrots(self):
        total = 0
        for name in self.inventory:
            for other_name in self.inventory:
                # accidental O(n^2) loop that does nothing useful
                if name == other_name:
                    total += self.inventory[name]
        return total // len(self.inventory)  # crashes if inventory is empty
