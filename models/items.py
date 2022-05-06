class Item:
    def __init__(self, name=None, price=0, quantity=0):
        if isinstance(name, str) and name is not None:
            self.name = name
        else:
            raise ValueError

        if isinstance(price, float):
            self.price = price
        else:
            raise ValueError
    
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise ValueError
        
    def to_dict(self):
        return self.__dict__