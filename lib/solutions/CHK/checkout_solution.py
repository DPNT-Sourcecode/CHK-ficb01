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
    def calculate_offers(self, count, skus, own_sku):
        free_items = []
        if count > 0:
            if self.offer is not None:
                offer_quantity = self.offer.quantity
                if self.offer.free_sku == own_sku:
                    offer_quantity+=1
                while count > 0:
                    if self.offer.free_sku in skus and count >= offer_quantity:
                        count -= offer_quantity
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
    'G': Item(20, None, {}),
    'H': Item(10, None, {10: 80, 5: 45}),
    'I': Item(35, None, {}),
    'J': Item(60, None, {}),
    'K': Item(80, None, {2: 150}),
    'L': Item(90, None, {}),
    'M': Item(15, None, {}),
    'N': Item(40, Offer(3, 'M'), {}),
    'O': Item(10, None, {}),
    'P': Item(50, None, {5: 200}),
    'Q': Item(30, None, {3: 80}),
    'R': Item(50, Offer(3, 'Q'), {}),
    'S': Item(30, None, {}),
    'T': Item(20, None, {}),
    'U': Item(40, Offer(3, 'U'), {}),
    'V': Item(50, None, {3: 130, 2: 90}),
    'W': Item(20, None, {}),
    'X': Item(90, None, {}),
    'Y': Item(10, None, {}),
    'Z': Item(50, None, {})
}

sku_regex = re.compile('^[A-Z]+$')

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
        for free_sku in price_table[sku].calculate_offers(count, [*skus], sku):
            sku_list.remove(free_sku)
    for sku in price_table:
        count = sku_list.count(sku)
        price += price_table[sku].calculate_discounts(count)
    return price







