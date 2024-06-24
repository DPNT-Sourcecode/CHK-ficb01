# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
from typing import Optional

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

def checkout(skus):
    price = 0
    print(skus)
    for sku in price_table:
        count = skus.lower().count(sku)
        if count > 0:
            while count > 0:
                if count >= price_table[sku].offer_quantity:
                    price += price_table[sku].offer_price
                    count -= price_table[sku].offer_quantity
                else:
                    price += price_table[sku].price * count
                    count = 0
    return price






