import string
import os
from typing import Any, Generator


def word_generator(filepath: str) -> Generator[str, Any, None]:
    """
    Generator that reads a file line by line and yields cleaned words.
    Demonstrates efficient memory usage and the 'yield' keyword.
    :param filepath: path to a file
    :return: a generator that yields cleaned words
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # Split line into words and clean them
            for word in line.split():
                clean_word = word.strip(string.punctuation).lower()
                if clean_word:
                    yield clean_word


def analyze_file(filepath: str) -> dict:
    """
    Analyzes word frequency using functional programming.
    Demonstrates: map, filter, lambda, and dictionary comprehension.
    :param filepath: path to a file
    :return dict: a dictionary that maps each word to its frequency
    """
    # 1. Using the generator to get all words
    all_words = list(word_generator(filepath))

    # 2. Functional programming: filter out short words (e.g., 'the', 'a', 'is')
    # Use a lambda function to keep only words longer than 3 characters
    filtered_words = list(filter(lambda w: len(w) > 3, all_words))

    # 3. Dictionary Comprehension: Count frequencies
    word_counts = {word: filtered_words.count(word) for word in set(filtered_words)}

    # Sort results by frequency (descending)
    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))


def main():
    target_file = "data.txt"

    # Create a dummy file for testing if it doesn't exist
    if not os.path.exists(target_file):
        with open(target_file, "w") as f:
            f.write("Python is great. Python is fast. Learning Python is fun!")

    print(f"--- Analyzing file: {target_file} ---")

    try:
        stats = analyze_file(target_file)

        print("\nTop word frequencies (words > 3 chars):")
        for word, count in list(stats.items())[:5]:
            print(f" - {word}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()