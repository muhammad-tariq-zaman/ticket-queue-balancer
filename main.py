"""Assign open tickets to the least-loaded agents.

Usage: python3 main.py tickets.csv agents.csv
tickets.csv columns: ticket,category. agents.csv columns:
agent,capacity,current_load. Each ticket goes to the agent with the
lowest load ratio (current/capacity) still under capacity; tickets
that cannot be placed are reported UNASSIGNED.
"""
import argparse, csv, sys


def assign(tickets, agents):
    load = {a["agent"]: int(a["current_load"]) for a in agents}
    capacity = {a["agent"]: int(a["capacity"]) for a in agents}
    result = []
    for ticket in tickets:
        candidates = [a for a in load if load[a] < capacity[a]]
        if not candidates:
            result.append((ticket["ticket"], "UNASSIGNED"))
            continue
        chosen = min(candidates, key=lambda a: load[a] / capacity[a])
        load[chosen] += 1
        result.append((ticket["ticket"], chosen))
    return result, load


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tickets")
    parser.add_argument("agents")
    args = parser.parse_args(argv)
    with open(args.tickets, newline="", encoding="utf-8") as f:
        tickets = list(csv.DictReader(f))
    with open(args.agents, newline="", encoding="utf-8") as f:
        agents = list(csv.DictReader(f))
    result, _ = assign(tickets, agents)
    unassigned = 0
    for ticket, agent in result:
        if agent == "UNASSIGNED":
            unassigned += 1
        print(f"{ticket} -> {agent}")
    print(f"{unassigned} ticket(s) unassigned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
