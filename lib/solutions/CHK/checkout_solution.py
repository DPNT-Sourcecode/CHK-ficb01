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
    offers: set[Offer]
    discounts = dict[int, int]
    def calculate_offers(self, count):
        price = 0
        if count > 0:
            if len(self.offers)>0:
                offer_count = count
                while offer_count > 0:
                    for offer in self.offers:
                        if offer_count >= offer.quantity:
                            price -= price_table[offer.free_sku].price
                            offer_count -= offer.quantity

            while count > 0 :
                for quantity, discount in self.discounts.items():
                    if count >= quantity:
                        price += discount
                        count -= quantity
                        break
                if count < self.discounts.keys()[-1]:
                    price += self.price * count
                    count = 0


price_table = {
    'A': Item(50, None, {5: 200, 3: 130}),
    'B': Item(30, None, {2: 45}),
    'C': Item(20, []),
    'D': Item(15, []),
    'E': Item(40, [Offer(2, None, 'B')], None),
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
        
    return price




