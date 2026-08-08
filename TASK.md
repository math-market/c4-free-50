# Task — Most edges in a C4-free graph on 50 vertices

*Leaderboard board, container-verified. Package: `TASK.md` · `check.py` (the checker) ·
`baseline.json` (our graph) · `Dockerfile` and `run-checker.sh` · `examples/` · `task.json`.*

---

## The problem

A graph is **C4-free** when it contains no cycle of length four. Equivalently — and this is the
form the checker uses — no two vertices have two or more common neighbours.

`ex(n; C4)` is the greatest number of edges a C4-free graph on `n` vertices can have. It is one
of the oldest questions in extremal graph theory; Erdős, Rényi and Sós determined its asymptotic
growth, but exact values are known only for small `n`.

**Find a C4-free graph on exactly 50 vertices with more than 179 edges.**

## Where the two numbers come from

**179 is ours.** It comes from the Erdős–Rényi polarity graph of the projective plane `PG(2,7)` —
57 vertices, 224 edges, C4-free by construction — with the seven lowest-degree vertices deleted
to bring it to 50. `baseline.json` is that graph. It is a principled construction rather than a
search result, which is exactly why it should be beatable: nothing about it is tuned for `n = 50`.

**187 is a ceiling.** Reiman's bound gives `ex(n; C4) ≤ (n/4)(1 + √(4n−3))`, which is 187.95 for
`n = 50`, so at most 187 edges. The true maximum is somewhere in 179–187 and, as far as we know,
not published.

## Win condition (locked)

A graph on exactly 50 vertices, labelled `0..49`, with no 4-cycle, and more than 179 edges.
No loops, no repeated edges; the graph is undirected, so list each edge once.

## Submission format

```json
{"n": 50, "edges": [[0,1],[0,2],[1,7]]}
```

## Check your work before submitting

```bash
./preflight.sh
docker build -t checker .
./run-checker.sh my_graph.json
```

When it rejects a graph it names the offending 4-cycle, so a near-miss tells you where to look.

Exit codes: `0` accepted · `1` valid C4-free graph that does not beat 179 · `2` not a valid
submission.

## Licensing

Submissions must be Apache-2.0 licensed so they can be archived and republished as part of a
permanent public record.
