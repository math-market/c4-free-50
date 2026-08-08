#!/usr/bin/env python3
"""Checker for the C4-free extremal graph board.

A submission is a JSON file:

    {"n": 50, "edges": [[0,1],[0,2], ...]}

The graph must have exactly N vertices, labelled 0..N-1, and contain no
4-cycle. The board is won when such a graph has more than BASELINE edges.

The C4-free test is the local one: a graph contains a 4-cycle exactly when some
pair of distinct vertices has two or more common neighbours. Checking every pair
is O(N^2) bitset intersections — exact, and instant at this size.

Exit codes:  0 valid and beats the baseline · 1 valid but does not · 2 unreadable.
"""
import json, sys, itertools

N, BASELINE = 50, 179

def die(msg, code=2):
    print(f"REJECTED: {msg}")
    sys.exit(code)

def main():
    if len(sys.argv) != 2:
        die("usage: check.py <submission.json>")
    try:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    except Exception as e:
        die(f"could not read the submission as JSON: {e}")
    if not isinstance(data, dict) or "edges" not in data:
        die('the submission must be a JSON object with an "edges" key')
    if data.get("n") != N:
        die(f'"n" must be {N}, got {data.get("n")!r}')
    edges = data["edges"]
    if not isinstance(edges, list) or not edges:
        die('"edges" must be a non-empty list of [u, v] pairs')

    seen = set()
    adj = [0] * N
    for k, e in enumerate(edges):
        if not (isinstance(e, list) and len(e) == 2):
            die(f"edge {k} is not a pair [u, v]")
        u, v = e
        if not (isinstance(u, int) and isinstance(v, int)):
            die(f"edge {k} has non-integer endpoints")
        if not (0 <= u < N and 0 <= v < N):
            die(f"edge {k} = [{u}, {v}] has an endpoint outside 0..{N-1}")
        if u == v:
            die(f"edge {k} is a loop at vertex {u}")
        key = (min(u, v), max(u, v))
        if key in seen:
            die(f"edge {k} = [{u}, {v}] is a duplicate")
        seen.add(key)
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for u, v in itertools.combinations(range(N), 2):
        shared = adj[u] & adj[v]
        if bin(shared).count("1") > 1:
            w = [i for i in range(N) if shared >> i & 1][:2]
            die(f"vertices {u} and {v} have common neighbours {w[0]} and {w[1]} "
                f"— that is a 4-cycle {u}-{w[0]}-{v}-{w[1]}-{u}")

    m = len(seen)
    print(f"valid: C4-free graph on {N} vertices with {m} edges")
    if m > BASELINE:
        print(f"ACCEPTED: {m} > {BASELINE} — this improves on the published baseline")
        sys.exit(0)
    print(f"REJECTED: valid C4-free graph, but {m} edges does not beat the baseline of {BASELINE}")
    sys.exit(1)

if __name__ == "__main__":
    main()
