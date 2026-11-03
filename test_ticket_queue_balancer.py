import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import assign


def ticket(t):
    return {"ticket": t, "category": "VPN"}


def agent(name, cap, load):
    return {"agent": name, "capacity": str(cap), "current_load": str(load)}


class TestQueueBalancer(unittest.TestCase):
    def test_least_loaded_chosen(self):
        result, _ = assign([ticket("T1")], [agent("A", 10, 8), agent("B", 10, 2)])
        self.assertEqual(result, [("T1", "B")])

    def test_full_agents_unassigned(self):
        result, _ = assign([ticket("T1")], [agent("A", 1, 1)])
        self.assertEqual(result, [("T1", "UNASSIGNED")])

    def test_load_increments(self):
        _, load = assign([ticket("T1"), ticket("T2")],
                         [agent("A", 10, 0), agent("B", 10, 0)])
        self.assertEqual(load, {"A": 1, "B": 1})

    def test_ratio_not_absolute(self):
        result, _ = assign([ticket("T1")], [agent("A", 100, 40), agent("B", 10, 5)])
        self.assertEqual(result, [("T1", "A")])
