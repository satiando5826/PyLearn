class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return "Title: {} Author: {} \nPrice: {} $".format(self.name, self.author, self.price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.strip()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = int(price)
        except ValueError:
            print("Price Invalid")

    def __eq__(self, other):
        if (self.__name == other.name) & (self.author == other.author) & (self.__price == other.price):
            return True
        else:
            return False


if __name__ == '__main__':
    print()
    a = Book("basicPython", "God", 24)
    b = Book("  AdvPy", "Inw", 30)
    bc = Book("AdvPy", "Inw", 30)
    print(b == b)
    print(b == bc)
    print(b.__eq__(bc))  # __eq__ -----> ==
    print(id(b), id(bc))
