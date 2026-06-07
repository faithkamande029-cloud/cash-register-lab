#!/usr/bin/env python3

class CashRegister:
    total = 0
    items = []
    previous_transaction = []

    def __init__(self, discount, total, items, previous_transaction):
        self.discount = discount
        self.total = total
        self.items = items
        self.previous_transaction = previous_transaction

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self.dicount = value
        
        

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

    def apply_discount(self, discount):
        if not self.previous_transaction:
            print("There is no discount to apply.")
            return
        
        self.total -= self.total * (discount / 100)

        self.void_last_transaction()
        
    
