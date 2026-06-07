#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transaction = []
        

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transaction.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

        print(f"Total is now {self.total}")

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        self.total -= self.total * (self.discount / 100)

        print(f"Total after discount: {self.total}")

    def void_last_transaction(self):
        if not self.previous_transaction:
            return
    
        last = self.previous_transaction.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in  range(last["quantity"]):
            self.items.remove(last["item"])

        if not self.items:
            self.total = 0.0

        
    
