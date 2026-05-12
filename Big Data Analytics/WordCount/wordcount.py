# MapReduce Word Frequency in Python

word_to_find = "hadoop"

# Open file
with open("Big Data Analytics\WordCount\input.txt", "r") as file:
    data = file.read().lower()

# Split into words
words = data.split()

# Count frequency
count = words.count(word_to_find)

# Output
print("Word :", word_to_find)
print("Frequency :", count)