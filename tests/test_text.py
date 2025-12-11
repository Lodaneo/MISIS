import pytest
from lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "norm, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "eжик, eлка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("    ", ""),
    ],
)
def test_normalize(norm, expected):
    assert normalize(norm) == expected


###########################################
@pytest.mark.parametrize(
    "tok, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!...!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("   ", []),
    ],
)
def test_tokenize_basic(tok, expected):
    assert tokenize(tok) == expected


###########################################
@pytest.mark.parametrize(
    "freq, expected",
    [
        (["a", "b", "a", "c", "b", "b"], {"a": 2, "b": 3, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        (
            ["apple", "banana", "apple", "cherry", "banana", "apple"],
            {"apple": 3, "banana": 2, "cherry": 1},
        ),
        ([], {}),
        ([], {}),
        ([""], {"": 1}),
        (["    "], {"    ": 1}),
    ],
)
def test_count_freq(freq, expected):
    assert count_freq(freq) == expected


###########################################
@pytest.mark.parametrize(
    "top, expected",
    [
        ({"a": 2, "b": 3, "c": 1}, [("b", 3), ("a", 2), ("c", 1)]),
        ({"aa": 2, "bb": 2, "cc": 1}, [("aa", 2), ("bb", 2), ("cc", 1)]),
        (
            {"apple": 3, "banana": 2, "cherry": 1},
            [("apple", 3), ("banana", 2), ("cherry", 1)],
        ),
        ({}, []),
        ({}, []),
        ({"": 2}, [("", 2)]),
        ({"  ": 2}, [("  ", 2)]),  # same number of chars(spaces)
    ],
)
def test_top_n_tie_breaker(top, expected):
    assert top_n(top, 3) == expected


###########################################
###########################################
def test_count_freq_top_n_default():
    top_freq = count_freq(["a", "b", "a", "c", "d", "d", "a", "b", "e", "f", "b", "b"])
    assert top_freq == {"a": 3, "b": 4, "c": 1, "d": 2, "e": 1, "f": 1}
    assert top_n(top_freq) == [("b", 4), ("a", 3), ("d", 2), ("c", 1), ("e", 1)]


###########################################
def test_all_func():
    text = "Hello world! Hello everyone. The world is     beautiful."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "hello world! hello everyone. the world is beautiful."
    assert tokens == [
        "hello",
        "world",
        "hello",
        "everyone",
        "the",
        "world",
        "is",
        "beautiful",
    ]
    assert freq == {
        "beautiful": 1,
        "everyone": 1,
        "hello": 2,
        "is": 1,
        "the": 1,
        "world": 2,
    }
    assert top_words == [("hello", 2), ("world", 2)]
