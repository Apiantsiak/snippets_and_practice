from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP = open for extension, close for modification
#  Bad extension characteristic
#  2 --> 3
#  3 --> 7 c s w cs sw cw csw
#  To heal this smell will be used Specification pattern

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


#  Specification

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Combinator

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(
                lambda spec: spec.is_satisfied(item), self.args
            )
        )


class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product(name="Apple", color=Color.GREEN, size=Size.SMALL)
    tree = Product(name="Tree", color=Color.GREEN, size=Size.LARGE)
    house = Product(name="House", color=Color.BLUE, size=Size.LARGE)

    products = [apple, tree, house]

    # Old implementation

    pf = ProductFilter()
    print(f"Green products (old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green:")

    # New implementation

    bf = BetterFilter()
    green_spec = ColorSpecification(Color.GREEN)
    print(f"Green products (new):")
    for p in bf.filter(products, green_spec):
        print(f" - {p.name} is green:")

    large_spec = SizeSpecification(Size.LARGE)
    print(f"Large products (new):")
    for p in bf.filter(products, large_spec):
        print(f" - {p.name} is large:")

    print(f"Large blue items:")
    blue_spec = ColorSpecification(Color.BLUE)
    large_blue_spec = AndSpecification(large_spec, blue_spec)
    for p in bf.filter(products, large_blue_spec):
        print(f" - {p.name} is large and blue:")

    print(f"Large blue items with overrides & (binary and):")
    blue_spec = ColorSpecification(Color.BLUE)
    large_blue_spec = large_spec & blue_spec
    for p in bf.filter(products, large_blue_spec):
        print(f" - {p.name} is large and blue:")
