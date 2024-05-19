import pytest
from project import ask_question

def test_ask_question():
    assert ask_question("What is 100 * 0.5?", "50", 10) == 10
    assert ask_question("What is 2 + 2?", "4", 10) == 10
    assert ask_question("What is 99 / 3 ?", "33 ", 10) == 10
    assert ask_question("What is 100 - 11 ?", "89 ", 10) == 10
