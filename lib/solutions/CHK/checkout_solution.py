# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
import re
from typing import Optional

@dataclass
class offer:
    quantity: int
    price: Optional[int]
    free_sku: Optional[str]
@dataclass
class item:
    price: int
    offer_quantity: Optional[int]
    offer_price: Optional[int]

price_table = {
    'A': item(50, 3, 130),
    'B': item(30, 2, 45),
    'C': item(20, None, None),
    'D': item(15, None, None),
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


