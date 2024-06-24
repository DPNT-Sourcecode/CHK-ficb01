# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
import re
from typing import Optional

@dataclass
class Offer:
    quantity: int
    price: Optional[int]
    free_sku: Optional[str]
@dataclass
class Item:
    price: int
    offers: set[Offer]

price_table = {
    'A': Item(50, [Offer(3, 130, None), Offer(5, 200, None)]),
    'B': Item(30, 2, 45),
    'C': Item(20, None, None),
    'D': Item(15, None, None),
}

sku_regex = re.compile('^[A-D]+$')

def checkout(skus):
    if skus == "":
        return 0
    if not sku_regex.match(skus) :
        return -1
    price = 0
    print(skus)
    for sku in price_table:
        count = skus.count(sku)
        if count > 0:
            while count > 0:
                if price_table[sku].offer_quantity is not None and count >= price_table[sku].offer_quantity:
                    price += price_table[sku].offer_price
                    count -= price_table[sku].offer_quantity
                else:
                    price += price_table[sku].price * count
                    count = 0
    return price



