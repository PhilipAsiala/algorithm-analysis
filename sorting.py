"""Bubble Sort and Quicksort implementations with timing benchmarks."""

from __future__ import annotations

import random
import time
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list in ascending order using bubble sort.

    Repeatedly walks the list, swapping adjacent out-of-order pairs
    until no swaps remain. Average and worst case: O(n^2).
    """
    data = arr.copy()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def quicksort(arr: List[int]) -> List[int]:
    """Sort a list in ascending order using quicksort (Lomuto partition).

    Average case: O(n log n). Worst case (already sorted with poor pivots): O(n^2).
    Recurses into the smaller partition first so stack depth stays O(log n).
    """
    data = arr.copy()
    _quicksort_inplace(data, 0, len(data) - 1)
    return data


def _quicksort_inplace(data: List[int], low: int, high: int) -> None:
    while low < high:
        pivot_index = _partition(data, low, high)
        # Recurse on the smaller side; iterate on the larger side.
        if pivot_index - low < high - pivot_index:
            _quicksort_inplace(data, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quicksort_inplace(data, pivot_index + 1, high)
            high = pivot_index - 1


def _partition(data: List[int], low: int, high: int) -> int:
    # Random pivot avoids consistently bad splits on sorted / patterned input.
    pivot_pos = random.randint(low, high)
    data[pivot_pos], data[high] = data[high], data[pivot_pos]

    pivot = data[high]
    i = low
    for j in range(low, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


def time_sort(sort_fn, sizes: List[int], trials: int = 3) -> dict[int, float]:
    """Return average runtime in milliseconds for each input size."""
    results: dict[int, float] = {}
    for n in sizes:
        total = 0.0
        for seed in range(trials):
            sample = [random.Random(seed * 10_000 + n).randint(0, 1_000_000) for _ in range(n)]
            start = time.perf_counter()
            sort_fn(sample)
            total += time.perf_counter() - start
        results[n] = (total / trials) * 1000.0
    return results


if __name__ == "__main__":
    demo = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", demo)
    print("Bubble sort:", bubble_sort(demo))
    print("Quicksort:  ", quicksort(demo))

    sizes = [100, 250, 500, 1000, 2000]
    bubble_times = time_sort(bubble_sort, sizes)
    quick_times = time_sort(quicksort, sizes)

    print("\nInput size | Bubble (ms) | Quicksort (ms)")
    print("-" * 48)
    for n in sizes:
        print(f"{n:>10} | {bubble_times[n]:>11.3f} | {quick_times[n]:>14.3f}")
