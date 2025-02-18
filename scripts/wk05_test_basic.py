import pytest

# basic test #1: always pass
def test_permapass():
  assert 1 == 1

# basic test #2: always fail
def test_permafail():
  assert 2 > 300

# basic test #2 with custom error message
def test_permafail_msg():
  assert 2 > 300, "I wrote this message. My summary has less info."




#palindrome function
def is_palindrome(word:str) -> bool:
  if word == word[::-1]:
    return True
  else:
    return False

# unparametrized (individually writing assert statements)
#  written this way, all tests will reduce to a single PASS/FAIL
@pytest.mark.skip(reason="skipping palindrome")
def test_palindrome():
  assert is_palindrome('tacocat') == True
  assert is_palindrome('taco') == False
  assert is_palindrome('ada') == True

# parametrized version - all values will be run with separate PASS/FAIL status
@pytest.mark.skip(reason="skipping palindrome")  
@pytest.mark.parametrize("test_input, expected", 
                         [('tacocat',True), 
                          ('taco', False), 
                          ('ada', True)])
def test_palindrome_par(test_input, expected):
  assert is_palindrome(test_input) == expected