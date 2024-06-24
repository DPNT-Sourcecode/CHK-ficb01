# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
import re
from typing import Optional

@dataclass
class Offer:
    quantity: int
    free_sku: Optional[str]
@dataclass
class Item:
    price: int
    offer: Optional[Offer]
    discounts = dict[int, int]
    def calculate_offers(self, count):
        price = 0
        if count > 0:
            if self.offer is not None:
                offer_count = count
                while offer_count > 0:
                    if offer_count >= self.offer.quantity:
                        price -= price_table[self.offer.free_sku].price
                        offer_count -= self.offer.quantity
                    else:
                        break
            while count > 0 :
                for quantity, discount in self.discounts.items():
                    if count >= quantity:
                        price += discount
                        count -= quantity
                        break
                if len(self.discounts) == 0 or count < self.discounts.keys()[-1]:
                    price += self.price * count
                    count = 0


price_table = {
    'A': Item(50, None, {5: 200, 3: 130}),
    'B': Item(30, None, {2: 45}),
    'C': Item(20, None, {}),
    'D': Item(15, None, {}),
    'E': Item(40, Offer(2, None, 'B'), None),
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
        price += price_table[sku].calculate_offers(count)
    return price






