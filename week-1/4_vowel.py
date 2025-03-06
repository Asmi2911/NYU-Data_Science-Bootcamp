def count_vowels(word):
    vowels = set("aeiouAEIOU")  # Using a set for faster lookup
    return sum(1 for char in word if char in vowels)  # Count vowels in the word

word = input("Enter a word: ")  # Takes user input
print(f"Number of vowels in '{word}' is: {count_vowels(word)}")
