"""String utilities with intentional SonarQube issues."""

import re


def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count


# SonarQube: regular expression denial of service (python:S2631)
def validate_email(email):
    pattern = r"^([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+@([a-zA-Z0-9]+\.)+[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


# SonarQube: boolean literal in conditional (python:S1125)
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False


def truncate(s, max_length):
    if len(s) <= max_length:
        return s
    return s[:max_length] + "..."


# SonarQube: too many return statements (python:S1142)
def classify_string(s):
    if not s:
        return "empty"
    if s.isdigit():
        return "numeric"
    if s.isalpha():
        return "alphabetic"
    if s.isalnum():
        return "alphanumeric"
    if s.isspace():
        return "whitespace"
    return "mixed"


# SonarQube: variable shadowing built-in (python:S5765)
def format_list(list, separator=", "):
    return separator.join(str(item) for item in list)
