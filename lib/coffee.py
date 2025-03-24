#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size in ["Small","Medium","Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")