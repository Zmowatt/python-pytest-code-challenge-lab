from lib.palindrome import longest_palindromic_substring

def test_babad_multiple_valid():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_cbbd_even_length():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_two_nonmatching_chars():
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"

def test_numbers_allowed():
    assert longest_palindromic_substring("123454321") == "123454321"

def test_long_string_with_palindrome_in_middle():
    s = "xyz" + "abba" + "mnop"
    assert longest_palindromic_substring(s) == "abba"

def test_result_is_actually_a_substring_and_palindrome():
    s = "bananas"
    result = longest_palindromic_substring(s)
    assert result in s
    assert result == result[::-1]
