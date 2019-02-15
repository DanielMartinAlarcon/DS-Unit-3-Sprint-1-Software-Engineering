#!/usr/bin/env python
"""
A python module for Acme products

Examples
--------
>>> from acme import Product
>>> prod = Product('A Cool Toy')
>>> prod.name
'A Cool Toy'
>>> prod.price
10
>>> prod.weight
20
>>> prod.flammability
0.5
>>> prod.stealability()
'Kinda stealable.'
>>> prod.explode()
'...boom!'
"""


class Product:
    """Parent class of all Acme products
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio <= 0.5 <= 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."
        elif product <= 10 <= 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    Everyone has a plan until they get punched in the face. -- Mike Tyson
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight <= 5 <= 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
