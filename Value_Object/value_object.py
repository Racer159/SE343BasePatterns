""" Value Object Implementation """


class Quarter:

    __val = 0.25

    @staticmethod
    def get_value():
        return Quarter.__val

    @staticmethod
    def set_value(new):
        print("You Can Not Change the Amount of the Quarter!!!")

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, new):
        print("You Can Not Change the Amount of the Quarter!!!")

    def __init__(self):
        pass

    def __eq__(self, other):
        return self.value == other.value


class Dollar:

    __val = 1.00

    @staticmethod
    def get_value():
        return Dollar.__val

    @staticmethod
    def set_value(new):
        print("You Can Not Change the Amount of the Dollar!!!")

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, new):
        print("You Can Not Change the Amount of the Dollar!!!")

    def __init__(self):
        pass

    def __eq__(self, other):
        return self.value == other.value

    @staticmethod
    def convert_to_quarters(num_dollars):
        total = Dollar.get_value() * num_dollars
        num_quarters = int(total / Quarter.get_value())

        return [Quarter() for i in range(0, num_quarters)]


def main():
    print(Quarter.get_value())
    print(Dollar.get_value())

    list_quarters = Dollar.convert_to_quarters(5)
    print(len(list_quarters))

    first = list_quarters[0]
    print("First Quarter instance: ")
    print(first)

    print("Mem Locations of Quarters in List and Equality to First Quarter")
    for i in range(0, len(list_quarters)):
        print(list_quarters[i])
        print(first == list_quarters[i])

    print("Try to change the quarters value")
    Quarter.set_value(100)


if __name__ == "__main__":
    main()