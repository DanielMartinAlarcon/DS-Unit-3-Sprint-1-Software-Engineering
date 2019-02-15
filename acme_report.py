ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    """
    Generates a given number of products
    """
    from acme import Product
    from random import choice, randint, random

    inventory = []
    for i in range(n):
        name = choice(ADJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = random() * 2.5
        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)

        inventory.append(prod)
    return inventory


def inventory_report(inventory):
    """Prints out statistics for an inventory"""
    def mean(list):
        return sum(list)/len(list)

    n_unique = len(set([x.name for x in inventory]))
    mean_price = mean([x.price for x in inventory])
    mean_weight = mean([x.weight for x in inventory])
    mean_flammability = mean([x.flammability for x in inventory])

    # Create a dict of item categories
    names = [x.name for x in inventory]
    nouns = [x.split(' ')[1] for x in names]
    noun_set = set(nouns)
    item_dict = {}
    for i in noun_set:
        count = 0
        for j in nouns:
            if i == j:
                count += 1
        item_dict[i] = count

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {n_unique}')
    print(f'Average price: {mean_price}')
    print(f'Average weight: {mean_weight}')
    print(f'Average flammability: {mean_flammability}')
    print()
    print('Item categories:')
    for key, value in item_dict.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    inventory_report(generate_products())
