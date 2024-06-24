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
    discounts: dict[int, int]
    def calculate_offers(self, count, skus):
        free_items = []
        if count > 0:
            if self.offer is not None:
                while count > 0:
                    if self.offer.free_sku in skus and count >= self.offer.quantity:
                        count -= self.offer.quantity
                        skus.remove(self.offer.free_sku)
                        free_items.append(self.offer.free_sku)
                    else:
                        break
        return free_items
    def calculate_discounts(self, count):
        price = 0
        if count > 0:
            while count > 0 :
                for quantity, discount in self.discounts.items():
                    if count >= quantity:
                        price += discount
                        count -= quantity
                        break
                if len(self.discounts) == 0 or count < list(self.discounts)[-1]:
                    price += self.price * count
                    count = 0
        return price

price_table = {
    'A': Item(50, None, {5: 200, 3: 130}),
    'B': Item(30, None, {2: 45}),
    'C': Item(20, None, {}),
    'D': Item(15, None, {}),
    'E': Item(40, Offer(2, 'B'), {}),
    'F': Item(10, Offer(2, 'F'), {}),
}

sku_regex = re.compile('^[A-F]+$')

def checkout(skus):
    if skus == "":
        return 0
    if not sku_regex.match(skus) :
        return -1
    price = 0
    print(skus)
    sku_list = [*skus]
    for sku in price_table:
        count = sku_list.count(sku)
        for free_sku in price_table[sku].calculate_offers(count, [*skus]):
            sku_list.remove(free_sku)
    for sku in price_table:
        count = sku_list.count(sku)
        price += price_table[sku].calculate_discounts(count)
    return price







