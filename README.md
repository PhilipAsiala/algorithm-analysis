# Algorithm Analysis: Bubble Sort vs Quicksort

Python implementations of **bubble sort** and **quicksort**, with timing benchmarks and a performance graph.

## Run in GitHub Codespaces

1. Open this repository in a Codespace (or use `gh codespace create`).
2. Wait for the post-create step to install dependencies.
3. Run:

```bash
python sorting.py
python benchmark.py
```

`benchmark.py` writes:
- `performance_graph.png` — runtime vs input size
- `benchmark_results.csv` / `benchmark_results.json` — raw timings

## Files

| File | Purpose |
|------|---------|
| `sorting.py` | Bubble sort, quicksort, demo, and timing helper |
| `benchmark.py` | Benchmarks both algorithms and saves the graph |
| `REPORT.md` | ~300-word analysis report |
| `.devcontainer/` | Codespaces / Dev Containers setup |

## Complexity (summary)

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) |
