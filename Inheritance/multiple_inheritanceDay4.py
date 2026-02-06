# Single inheritance

class father:
    def __init__(self,surname,father_name):
        self.surname=surname
        self.father_name=father_name
    def display_surname(self):
        print("Surname:",self.surname)
    def display_father_name(self):
        print("Father Name:",self.father_name)

class mother:
    def __init__(self,eye_color,mother_name):
        self.eye_color=eye_color
        self.mother_name=mother_name
    def display_eye_color(self):
        print("Eye Color:",self.eye_color)
    def display_mother_name(self):
        print("Mother Name:",self.mother_name)       
        
class son(father,mother):
    def __init__(self,name,surname,father_name,eye_color,mother_name):
        father.__init__(self,surname,father_name)
        mother.__init__(self,eye_color,mother_name)
        self.name=name
    def display_name(self):
        print("Son Name:",self.name)

child_obj=son("John","K","Rajesh","Brown","Anita")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()
child_obj.display_mother_name()
child_obj.display_eye_color()