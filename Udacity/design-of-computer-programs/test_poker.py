from poker import poker 

def test_poker():
    straight_flush = "6C 7C 8C 9C TC".split()
    four_of_kind = "9D 9H 9S 9C 7D".split()
    full_house = "TD TC TH 7C 7D".split()
    
    assert poker([straight_flush, four_of_kind, full_house]) == straight_flush
    assert poker([four_of_kind, full_house]) == four_of_kind
    assert poker([full_house, full_house]) == full_house

def test_max_function():
    assert max([3,4,5,-9]) == 5
    assert max([3,4,5,-9], key=abs) == -9
