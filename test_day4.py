import pytest

@pytest.fixture

def sample_data():
    return {"My Name": "Billa", "City": "Vijayawada", "Country": "India", "Even Number": 4}
    

def test_name(sample_data):
    assert sample_data["My Name"] == "Billa"

def test_city(sample_data):
    assert sample_data["City"] == "Vijayawada"  

def test_country(sample_data):
    assert sample_data["Country"] == "India"    

def test_evennumbercheck():
    assert 4 % 2 == 0
    
@pytest.mark.parametrize("input_string, expected_output", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("abcd", "dcba"),
])

def test_reverse_string(input_string, expected_output):

    from Day4Practice import reverse_string
    assert reverse_string(input_string) == expected_output

@pytest.mark.parametrize("a, b, expected", [
    
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 5, 15),
])

def test_add(a, b, expected):
    from Day3_pytestExercise import add
    assert add(a, b) == expected        

@pytest.mark.parametrize("input,output", [
    (2, True),
    (3, False),
    (4, True),  
    (9, False) 
    ])

def test_evennum(input, output):
    from Day3_pytestExercise import evennum
    assert evennum(input) == output