from operation import *

def test_add():
    assert add(4,5) == 9
    
def test_sub():
    assert sub(10,4) == 6
    
def test_div():
    assert div(25,5) == 5
    
def test_mul():
    assert mul(3,5) == 15