"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""

class Counter:

    def __init__(self):
        if not hasattr(self, 'count'):
            self.__count = 0

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1
        return self.count

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Counter, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    counter = Counter()
    print(counter.count)
    print(counter.count)  # invoking count doesn't change anything
    print(counter.increment()) # add 1 and return the new count
    print(counter.increment())
    counter2 = Counter()
    print(counter2 is counter)
    print(counter2.count)  # shares same count
    print(counter2.increment())  # add 1 and return the new count
    print(counter.count)