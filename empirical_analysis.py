import random
import time
from statistics import mean

from selection_algorithms import deterministic_select, randomized_select


def generate_input(size, input_type):
    if input_type == "random":
        return [random.randint(1, size * 10) for _ in range(size)]
    if input_type == "sorted":
        return list(range(size))
    if input_type == "reverse_sorted":
        return list(range(size, 0, -1))
    raise ValueError("Unsupported input type.")


def measure_time(function_ref, data, k, runs=5):
    timings = []

    for _ in range(runs):
        copied = data[:]
        start = time.perf_counter()
        function_ref(copied, k)
        end = time.perf_counter()
        timings.append(end - start)

    return mean(timings)


def run_experiment():
    sizes = [100, 500, 1000, 3000]
    input_types = ["random", "sorted", "reverse_sorted"]

    print("\nEmpirical Analysis of Selection Algorithms")
    print("-" * 70)

    for input_type in input_types:
        print(f"\nInput Type: {input_type}")

        for size in sizes:
            dataset = generate_input(size, input_type)
            k = size // 2

            deterministic_time = measure_time(deterministic_select, dataset, k)
            randomized_time = measure_time(randomized_select, dataset, k)

            print(
                f"Size {size:<5} | "
                f"Deterministic: {deterministic_time:.6f} sec | "
                f"Randomized: {randomized_time:.6f} sec"
            )


if __name__ == "__main__":
    run_experiment()