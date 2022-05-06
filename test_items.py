import pytest
from models.items import Item

def test_items_attributes():
    apple = Item(name="Apple", price=2.50, quantity=2)
    assert apple.name == "Apple"
    assert apple.price == 2.50
    assert apple.quantity == 2
    
def test_items_to_dict():
    apple = Item(name="Apple", price=2.50, quantity=2)
    assert apple.to_dict() == {"name": "Apple", "price": 2.50, "quantity": 2}

def test_items_invalid():
    with pytest.raises(ValueError):
        Item(name=123, price=2.50)
    with pytest.raises(ValueError):
        Item(name="Apple", price=2)
    with pytest.raises(ValueError):
        Item(name="Apple", price="2.50")
    with pytest.raises(ValueError):
        Item(name="Apple", price=2.50, quantity="2")
    with pytest.raises(ValueError):
        Item(name="Apple", price=2.50, quantity=2.0)