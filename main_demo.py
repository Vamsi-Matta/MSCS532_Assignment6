from selection_algorithms import deterministic_select, randomized_select
from data_structures import demonstrate_data_structures


def demonstrate_selection_algorithms():
    data = [14, 7, 9, 3, 11, 2, 6, 8, 5, 10, 1, 13, 4, 12]
    k = 5  # 0-based index, so this is the 6th smallest element

    print("----- Selection Algorithms Demo -----")
    print("Input array:", data)
    print("Sorted array:", sorted(data))
    print(f"Looking for element at index k={k} (0-based)\n")

    deterministic_result = deterministic_select(data, k)
    randomized_result = randomized_select(data, k)

    print("Deterministic Selection Result:", deterministic_result)
    print("Randomized Selection Result:", randomized_result)


def main():
    demonstrate_selection_algorithms()
    print("\n")
    demonstrate_data_structures()


if __name__ == "__main__":
    main()