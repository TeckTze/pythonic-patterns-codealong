from dataclasses import dataclass
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def compute(self):
        ...

class PercentageDiscount(DiscountStrategy):
    def compute(self, price):
        return price * 0.2

class FixedDiscount(DiscountStrategy):
    def compute(self, price):
        return 10_00
    
@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountStrategy

    def compute(self):
        discount = self.discount.compute(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount = PercentageDiscount())
    print(order)
    print(f"Total: ${order.compute()/100:.2f}")


if __name__ == "__main__":
    main()
