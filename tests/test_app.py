from Day3_pytestExercise import add

def test_add():
    assert add(2, 3) == 5

from Day3_pytestExercise import sub

def test_sub():
    assert sub(2, 3) == -1

from Day3_pytestExercise import multi
def test_multi():
    assert multi(2, 3) == 6

from Day3_pytestExercise import zero
def test_zero():
    assert zero(2,3)*0 == 0

from Day3_pytestExercise import evennum
def test_evennum():
    assert evennum (2, 3) 