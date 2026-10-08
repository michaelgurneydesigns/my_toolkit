def calculate_average(numbers):
    """Return the average of a list of numbers, or 0 for an empty list."""
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def find_max_and_min(numbers):
    """Return (highest, lowest) using a loop, or (None, None) if empty."""
    if len(numbers) == 0:
        return (None, None)

    highest = numbers[0]
    lowest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

    return (highest, lowest)


def count_occurrences(items, target):
    """Return how many times the target appears in the list."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Check whether text reads the same backward, ignoring case and spaces."""
    cleaned_text = text.lower().replace(" ", "")
    reversed_text = cleaned_text[::-1]

    return cleaned_text == reversed_text


def create_report(title, scores):
    """Return a formatted report with the count, average, and score extremes."""
    average = calculate_average(scores)
    highest, lowest = find_max_and_min(scores)

    if len(scores) == 0:
        highest = "N/A"
        lowest = "N/A"

    return (
        f"========================================\n"
        f"{title}\n"
        f"========================================\n"
        f"Total scores: {len(scores)}\n"
        f"Average score: {average:.1f}\n"
        f"Highest score: {highest}\n"
        f"Lowest score: {lowest}"
    )


if __name__ == "__main__":
    # Required tests
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # Average edge cases
    print("\n--- Average edge cases ---")
    print(f"Empty list: {calculate_average([])} — expected: 0")
    print(f"One number: {calculate_average([75])} — expected: 75.0")
    print(
        f"Negative numbers: {calculate_average([-10, -20, -30])}"
        f" — expected: -20.0"
    )

    # Highest and lowest edge cases
    print("\n--- Max/Min edge cases ---")
    print(f"Empty list: {find_max_and_min([])} — expected: (None, None)")
    print(f"One number: {find_max_and_min([75])} — expected: (75, 75)")
    print(
        f"Negative numbers: {find_max_and_min([-10, -20, -30])}"
        f" — expected: (-10, -30)"
    )
    print(
        f"Identical numbers: {find_max_and_min([5, 5, 5])}"
        f" — expected: (5, 5)"
    )

    # Counting edge cases
    print("\n--- Counting edge cases ---")
    print(
        f"Multiple matches: {count_occurrences([85, 70, 85, 85], 85)}"
        f" — expected: 3"
    )
    print(
        f"No matches: {count_occurrences([1, 2, 3], 9)}"
        f" — expected: 0"
    )
    print(f"Empty list: {count_occurrences([], 85)} — expected: 0")
    print(
        f"Words: {count_occurrences(['cat', 'dog', 'cat'], 'cat')}"
        f" — expected: 2"
    )

    # Palindrome edge cases
    print("\n--- Palindrome edge cases ---")
    print(
        f"Phrase: {is_palindrome('A man a plan a canal Panama')}"
        f" — expected: True"
    )
    print(f"Mixed case: {is_palindrome('RaceCar')} — expected: True")
    print(f"Single character: {is_palindrome('a')} — expected: True")
    print(f"Empty string: {is_palindrome('')} — expected: True")
    print(f"Only spaces: {is_palindrome('   ')} — expected: True")
    print(f"Non-palindrome: {is_palindrome('Python')} — expected: False")

    # Report edge cases
    print("\n--- Empty report: 0 scores, 0.0 average, N/A extremes ---")
    print(create_report("Empty Scores", []))

    print("\n--- Single-score report: average, highest, lowest all 75 ---")
    print(create_report("One Score", [75]))

  