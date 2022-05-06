from multiprocessing.sharedctypes import Value


class Item:
    def __init__(self, name=None, price=0, quantity=0):
        if isinstance(name, int):
            raise ValueError
        else:
            self.name = name
            
        if isinstance(price, int):
            raise ValueError
        elif isinstance(price, str):
            raise ValueError
        else:
            self.price = price
            
        if isinstance(quantity, str):
            raise ValueError
        elif isinstance(quantity, float):
            raise ValueError
        else:
            self.quantity = quantity
        
    def to_dict(self):
        return self.__dict__