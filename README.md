# ex(50; C4) — most edges in a C4-free graph on 50 vertices

A Problem Market board. Beat **179** edges without creating a 4-cycle. Our baseline
(`baseline.json`) is the `PG(2,7)` polarity graph trimmed to 50 vertices; Reiman's bound caps any
answer at 187.

```bash
./preflight.sh
docker build -t checker .
./run-checker.sh my_graph.json
```

Task and win condition: [`TASK.md`](TASK.md). Constraints as data: [`task.json`](task.json).
