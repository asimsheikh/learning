from poker import poker 

def test_poker():
    assert poker() 

def test_max_function():
    assert max([3,4,5,-9]) == 5
    assert max([3,4,5,-9], key=abs) == -9
