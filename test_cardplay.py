import cardplay
import pytest

def test_silly_function_works():
    value = 3
    assert cardplay.silly_function(value) == 4

#def test_silly_function_fails():
#    value = 3
#    assert cardplay.silly_function(value) == 5

def test_silly_function_works1():
    value = 0
    assert cardplay.silly_function(value) == 1

def test_silly_function_works2():
    value = -1
    assert cardplay.silly_function(value) == 0

def test_silly_function_works3():
    value = 1000000
    assert cardplay.silly_function(value) == 1000001

def test_my_sum_works():
    my_list = [1, 2, 3, 4, 5]
    assert cardplay.my_sum(my_list) == 15

def test_my_sum_non_numeric():
    my_list = ['this', 'is', 'a', 'bad', 'list']
    with pytest.raises(TypeError):
        cardplay.my_sum(my_list)

class TestTypeOfDeck():
    def test_standard_deck_name(self):
        tod = cardplay.Standard_52_Card_Deck
        assert str(tod) == 'Standard 52-card'

    def test_custom_deck_name(self):
        tod = cardplay.TypeOfDeck('TESTING TESTING', cardplay.Suit, cardplay.Rank)
        assert str(tod) == 'TESTING TESTING'

