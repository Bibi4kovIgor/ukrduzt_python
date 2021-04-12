import copy


class Parallelogram:
    def __init__(self, a, b, h):
        self.__a = a
        self.__b = b
        self.__h = h

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Size of geometric figure must be greater than 0 ")
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Size of geometric figure must be greater than 0 ")
        self.__b = value

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        if value <= 0:
            raise ValueError("Height of geometric figure must be greater than 0 ")
        self.__h = value

    def get_perimeter(self):
        return (self.__a + self.b) * 2

    def get_area(self):
        return self.__b * self.__h

    def is_equal(self, p2):
        return self.__a == p2.__a and self.__b == p2.__b and self.__h == p2.__h

    def __str__(self):
        return "Parallelogram: \n A: {} \t B: {} \t H: {}".format(self.__a, self.__b, self.__h)


if __name__ == '__main__':
    p1 = Parallelogram(2, 4, 6)
    p2 = copy.deepcopy(p1)
    p3 = Parallelogram(7, 8, 9)

    print(p1)
    print(p2)
    print(p3)

    print("Perimeter p1 = ", p1.get_perimeter(), "Area p1 = ", p1.get_area())
    print("Perimeter p3 = ", p3.get_perimeter(), "Area p3 = ", p3.get_area())

    print("p1 is equal to p2 ", p1.is_equal(p2))
    print("p1 is equal to p3 ", p1.is_equal(p3))
