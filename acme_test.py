#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explosiveness(self):
        """Ensure minimum acceptable stealability and explosiveness"""
        prod = Product('TNT', weight=5, flammability=100)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """
    Making sure Acme product reports are the tops!
    """
    def test_default_num_products(self):
        """Ensure a default report contains 30 products"""
        inventory = generate_products()
        self.assertEqual(len(inventory), 30)

    def test_legal_names(self):
        """Ensure all names have the right components"""
        inventory = generate_products()
        names = [x.name for x in inventory]
        # Test that each name is two words separated by a space
        for n in names:
            self.assertEqual(len(n.split(' ')), 2)

        # test that all nouns and adjectives come from the right lists
        for n in names:
            pair = n.split(' ')
            adjective = pair[0]
            noun = pair[1]
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
