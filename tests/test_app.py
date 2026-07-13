import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Day3_pytestExercise import add, sub, multi, zero, evennum


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(2, 3) == -1


def test_multi():
    assert multi(2, 3) == 6


def test_zero():
    assert zero(2,3)*0 == 0


def test_evennum():
    assert evennum (2, 3) 