import pytest

#testing mutable objects...caution!
def reverse_list(list: list):
  list.reverse()
  return list

# slice reverse before modifying the list with reverse() method
def test_list_reversed_LHS():
  test_list = [1,2,3,4]
  assert test_list[::-1] == reverse_list(test_list)

# slice reverse after modification - always opposite order
def test_list_reversed_RHS():
  test_list = [1,2,3,4]
  assert reverse_list(test_list) == test_list[::-1]