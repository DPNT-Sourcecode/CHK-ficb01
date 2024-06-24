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
    'C': item(20),
    'D': item(15),
}

def checkout(skus):
    print(skus)



