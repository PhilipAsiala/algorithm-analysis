"""Benchmark bubble sort vs quicksort and save a performance graph."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt

from sorting import bubble_sort, quicksort, time_sort

ROOT = Path(__file__).resolve().parent
SIZES = [100, 250, 500, 1000, 2000, 4000]
TRIALS = 3


def main() -> None:
    bubble_times = time_sort(bubble_sort, SIZES, trials=TRIALS)
    quick_times = time_sort(quicksort, SIZES, trials=TRIALS)

    rows = [
        {
            "n": n,
            "bubble_ms": round(bubble_times[n], 4),
            "quicksort_ms": round(quick_times[n], 4),
        }
        for n in SIZES
    ]

    csv_path = ROOT / "benchmark_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["n", "bubble_ms", "quicksort_ms"])
        writer.writeheader()
        writer.writerows(rows)

    json_path = ROOT / "benchmark_results.json"
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8, 5))
    ns = [row["n"] for row in rows]
    ax.plot(ns, [row["bubble_ms"] for row in rows], marker="o", label="Bubble sort O(n²)")
    ax.plot(ns, [row["quicksort_ms"] for row in rows], marker="s", label="Quicksort O(n log n)")
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Average runtime (ms)")
    ax.set_title("Sorting Performance: Bubble Sort vs Quicksort")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    graph_path = ROOT / "performance_graph.png"
    fig.savefig(graph_path, dpi=150)
    print(f"Saved {graph_path}")
    print(f"Saved {csv_path}")
    print(f"Saved {json_path}")
    for row in rows:
        print(
            f"n={row['n']:>5}: bubble={row['bubble_ms']:>10.3f} ms, "
            f"quicksort={row['quicksort_ms']:>8.3f} ms"
        )


if __name__ == "__main__":
    main()
