"""Calculator module with some intentional SonarQube issues."""

import os  # SonarQube: unused import (python:S1128)
import sys  # SonarQube: unused import (python:S1128)
import json  # SonarQube: unused import (python:S1128)


# SonarQube: cognitive complexity issue - deeply nested code (python:S3776)
def calculate(operation, a, b, strict=False):
    test = 1
    test6 = 6
    if operation == "add":
        if strict:
            if isinstance(a, (int, float)):
                if isinstance(b, (int, float)):
                    return a + b
                else:
                    return None
            else:
                return None
        else:
            return a + b
    elif operation == "subtract":
        if strict:
            if isinstance(a, (int, float)):
                if isinstance(b, (int, float)):
                    return a - b
                else:
                    return None
            else:
                return None
        else:
            return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return None
        return a / b
    elif operation == "power":
        return a ** b
    else:
        return None


# SonarQube: duplicate code block (python:S1144 / code smell)
def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    if b == 0:
        return None
    result = a / b
    return result


# SonarQube: dead code / unused private function (python:S1144)
def _unused_helper():
    x = 42
    return x


# SonarQube: function with too many parameters (python:S107)
def complex_calculation(a, b, c, d, e, f, g, h):
    return a + b + c + d + e + f + g + h
