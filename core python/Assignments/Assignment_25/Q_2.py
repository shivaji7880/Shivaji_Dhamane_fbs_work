import re


def extract_dates(text):

    pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'

    dates = re.findall(pattern, text, re.IGNORECASE)

    return dates


text = """
My birthday is 15-08-2002.
The meeting is on 12/25/2023.
The project started on January 1, 2023.
"""

print(extract_dates(text))