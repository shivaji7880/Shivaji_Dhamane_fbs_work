import re

def extract_urls(text):

    pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'

    urls = re.findall(pattern, text)

    return urls

text = """
Visit https://www.google.com
You can also visit https://www.github.com/python
Our website is https://example.org
"""

print(extract_urls(text))