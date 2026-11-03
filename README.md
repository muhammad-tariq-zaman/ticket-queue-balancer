# ticket-queue-balancer

Distribute open tickets to the agent with the lowest load ratio still under capacity, instead of piling them on whoever is already busiest.

## How to run

```sh
python3 main.py tickets.csv agents.csv
```

## Example output

```
T-101 -> Ali
T-102 -> Sara
0 ticket(s) unassigned.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
