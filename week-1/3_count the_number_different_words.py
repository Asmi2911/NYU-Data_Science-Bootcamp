import re

# Given text
string = """
I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!
"""

# Normalize text: convert to lowercase and extract words using regex
word_list = re.findall(r'\b\w+\b', string.lower())

# Get unique words
unique_words = set(word_list)

# Print the number of different words
print("Number of different words:", len(unique_words))

# Print unique words
print("\nUnique words:", unique_words)
