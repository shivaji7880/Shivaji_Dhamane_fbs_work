import re


def replace_forbidden(text, forbidden_words):
    pattern = "|".join(forbidden_words)

    result = re.sub(pattern, "*", text, flags=re.IGNORECASE)

    return result


text = "This is a bad and stupid example."
forbidden_words = ["bad", "stupid"]

print(replace_forbidden(text, forbidden_words))