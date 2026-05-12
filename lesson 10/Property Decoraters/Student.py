class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
         self.__age=age

    @name.setter
    def name(self,name):
         self.__name=name


studenti2 = Student("Nili",15)

print(studenti2.name)
print(studenti2.age)

studenti2.name="Driart"
studenti2.age=15

print(studenti2.name)
print(studenti2.age)