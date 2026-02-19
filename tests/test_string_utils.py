from test_python_project.string_utils import (
    reverse_string,
    capitalize_words,
    count_vowels,
    validate_email,
    is_palindrome,
    truncate,
    classify_string,
    format_list,
)


class TestReverseString:
    def test_simple(self):
        assert reverse_string("hello") == "olleh"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"


class TestCapitalizeWords:
    def test_simple(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello") == "Hello"


class TestCountVowels:
    def test_simple(self):
        assert count_vowels("hello") == 2

    def test_no_vowels(self):
        assert count_vowels("xyz") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_uppercase(self):
        assert count_vowels("HELLO") == 2


class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") is True

    def test_invalid_email_no_at(self):
        assert validate_email("userexample.com") is False

    def test_invalid_email_no_domain(self):
        assert validate_email("user@") is False


class TestIsPalindrome:
    def test_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("taco cat") is True


class TestTruncate:
    def test_short_string(self):
        assert truncate("hi", 10) == "hi"

    def test_long_string(self):
        assert truncate("hello world", 5) == "hello..."


class TestClassifyString:
    def test_empty(self):
        assert classify_string("") == "empty"

    def test_numeric(self):
        assert classify_string("12345") == "numeric"

    def test_alphabetic(self):
        assert classify_string("hello") == "alphabetic"

    def test_alphanumeric(self):
        assert classify_string("hello123") == "alphanumeric"

    def test_whitespace(self):
        assert classify_string("   ") == "whitespace"

    def test_mixed(self):
        assert classify_string("hello world!") == "mixed"


class TestFormatList:
    def test_strings(self):
        assert format_list(["a", "b", "c"]) == "a, b, c"

    def test_numbers(self):
        assert format_list([1, 2, 3]) == "1, 2, 3"

    def test_custom_separator(self):
        assert format_list(["a", "b"], separator=" | ") == "a | b"
