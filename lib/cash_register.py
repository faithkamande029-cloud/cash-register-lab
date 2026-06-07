#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transaction = []

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self.discount = value
        
        

    def add_item(self, item, price, quantity):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transaction.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def void_last_transaction(self):
        if not self.previous_transaction:
            return
    
        last = self.previous_transaction.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in  range(last["quantity"]):
            self.items.remove(last["item"])

    def apply_discount(self):
        if not self.previous_transaction:
            print("There is no discount to apply.")
            return
        
        self.total -= self.total * (self.discount / 100)

        self.void_last_transaction()
        
    
