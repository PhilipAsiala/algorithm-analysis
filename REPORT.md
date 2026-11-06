# Bubble Sort vs Quicksort: Performance Analysis

## Functionality

Bubble sort repeatedly compares adjacent elements and swaps them when they are out of order. Each full pass “bubbles” the next largest value toward the end of the list. An early-exit flag stops the algorithm once a pass makes no swaps, which helps on nearly sorted input. Quicksort instead chooses a pivot, partitions smaller values to the left and larger values to the right, then recursively sorts each side. The median-of-three pivot used here reduces the chance of pathological partitions on sorted or reverse-sorted data. Both algorithms produce a correctly ordered list; they differ mainly in how much work they do as the input grows.

## Efficiency for Small vs Large Datasets

Bubble sort’s average and worst-case time complexity are both O(n²) because nested loops compare pairs of elements. For tiny datasets—roughly tens to a few hundred items—this quadratic cost is often acceptable, and the algorithm’s simplicity and tiny constant factors make it easy to implement and reason about. As n grows into the thousands, runtime rises sharply: doubling the input size roughly multiplies bubble sort’s work by four. Quicksort’s average complexity is O(n log n). Each level of recursion does linear work across the array, and there are about log n levels, so growth is much gentler. Empirically, for random arrays of a few thousand elements, quicksort finishes in milliseconds while bubble sort may take hundreds of milliseconds or more. Space use also differs: bubble sort needs only a few variables (O(1) extra memory), whereas recursive quicksort uses O(log n) stack space on average.

## Comparison and Real-World Use Cases

Bubble sort is mainly valuable for teaching, tiny in-memory lists, or situations where code clarity matters more than speed. Production systems almost never rely on it for large collections. Quicksort (or closely related dual-pivot variants) underpins many language runtimes and libraries because of strong average-case speed and good cache behaviour, though mergesort or heapsort may be preferred when a guaranteed O(n log n) worst case is required. In practice: use bubble sort only for small n or pedagogy; use quicksort or library sort routines for real workloads where input size and latency matter.
