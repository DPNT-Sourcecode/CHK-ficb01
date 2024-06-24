# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass


price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}
@dataclass
class item:
    sku: str
    price: int
    offer_quantity: int
    offer_price: int
offers = {

}
def checkout(skus):
    print(skus)


