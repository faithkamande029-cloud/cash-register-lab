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
    def dicount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        value = range(0, 101)

        if not isinstance(value, int):
            print("Not valid discount")
        
        

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)
        self.previous_transaction.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def void_last_transaction(self):
        if self.previous_transaction:
            last = self.previous_transaction.pop()

            self.total -= last["price"] * last["quantity"]

            if last["item"] in self.items:
                self.items.remove(last["item"])

    def apply_discount(self, percent):
        if not self.previous_transaction:
            print("There is no discount to apply.")
            return
        
        self.discount = self.total*(percent / 100)
        self.total -= self.dicount

        self.void_last_transaction()
        
    
