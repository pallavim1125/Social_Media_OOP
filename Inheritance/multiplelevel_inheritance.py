class grand_parent:
    def __init__(self, property):
        self.grand_father_property = property

    def display_property1(self):
        print("Grand Parent Property:", self.grand_father_property)


class father(grand_parent):
    def __init__(self, property, grand_father_property):
        super().__init__(grand_father_property)
        self.father_property = property

    def display_property2(self):
        print("Father Property:", self.father_property)


class son(father):
    def __init__(self, property, father_property, grand_father_property):
        super().__init__(father_property, grand_father_property)
        self.child_property = property

    def display_property3(self):
        print("Child Property:", self.child_property)


son_obj = son("Wealth", "Bike", "Car")


def display_all_properties(son_obj):
    son_obj.display_property1()
    son_obj.display_property2()
    son_obj.display_property3()


display_all_properties(son_obj)
