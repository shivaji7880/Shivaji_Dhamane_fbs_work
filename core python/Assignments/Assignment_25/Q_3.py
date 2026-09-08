import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


text = "Python is easy and Python is powerful"

result = count_words(text)

print(result)