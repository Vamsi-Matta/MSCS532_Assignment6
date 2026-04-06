import random


def insertion_sort(values):
    """Sort a small list using insertion sort and return a new sorted list."""
    arr = values[:]
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def partition_three_way(arr, pivot):
    """
    Partition array into three lists:
    less than pivot, equal to pivot, greater than pivot.
    """
    lower = []
    equal = []
    higher = []

    for item in arr:
        if item < pivot:
            lower.append(item)
        elif item > pivot:
            higher.append(item)
        else:
            equal.append(item)

    return lower, equal, higher


def deterministic_select(arr, k):
    """
    Return the k-th smallest element (0-based index)
    using the Median of Medians algorithm.

    Example:
    deterministic_select([7, 2, 9, 1], 0) -> 1
    """
    if not arr:
        raise ValueError("Input array cannot be empty.")

    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds.")

    if len(arr) <= 5:
        return insertion_sort(arr)[k]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = []

    for group in groups:
        sorted_group = insertion_sort(group)
        medians.append(sorted_group[len(sorted_group) // 2])

    pivot = deterministic_select(medians, len(medians) // 2)

    lower, equal, higher = partition_three_way(arr, pivot)

    if k < len(lower):
        return deterministic_select(lower, k)
    elif k < len(lower) + len(equal):
        return pivot
    else:
        new_k = k - len(lower) - len(equal)
        return deterministic_select(higher, new_k)


def randomized_select(arr, k):
    """
    Return the k-th smallest element (0-based index)
    using Randomized Quickselect.
    """
    if not arr:
        raise ValueError("Input array cannot be empty.")

    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds.")

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lower, equal, higher = partition_three_way(arr, pivot)

    if k < len(lower):
        return randomized_select(lower, k)
    elif k < len(lower) + len(equal):
        return pivot
    else:
        new_k = k - len(lower) - len(equal)
        return randomized_select(higher, new_k)


def verify_selection_algorithms():
    """Basic correctness checks."""
    sample = [12, 3, 5, 7, 19, 1, 5, 3]
    sorted_sample = sorted(sample)

    for index in range(len(sample)):
        d_result = deterministic_select(sample, index)
        r_result = randomized_select(sample, index)
        expected = sorted_sample[index]

        assert d_result == expected, f"Deterministic failed for k={index}"
        assert r_result == expected, f"Randomized failed for k={index}"

    print("Selection algorithm verification passed.")


if __name__ == "__main__":
    verify_selection_algorithms()