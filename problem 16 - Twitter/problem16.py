#!/bin/python3

class ECommerce:
    max = 0
    current = 0
    order = {}

    def __init__(self, n):
        self.max = n

    def record(self, order_id):
        self.order.update({self.current: order_id})
        self.current = (self.current + 1) % self.max

    def get_last(self, i):
        return self.order[i]


obj = ECommerce(3)
obj.record("88")
obj.record("77")
obj.record("99")
obj.record("100")

print(obj.get_last(0))
