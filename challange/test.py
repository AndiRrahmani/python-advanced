from abc import ABC, abstractmethod


# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # Encapsulation using @property
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than 0.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self._height = value

    # Abstract methods
    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


# Adult Class
class Adult(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()

        print("\n--- Adult BMI Information ---")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Weight   : {self.weight} kg")
        print(f"Height   : {self.height} m")
        print(f"BMI      : {bmi:.2f}")
        print(f"Category : {category}")


# Child Class
class Child(Person):

    def calculate_bmi(self):
        # Adjusted BMI formula
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        # Example child thresholds
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 22:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()

        print("\n--- Child BMI Information ---")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Weight   : {self.weight} kg")
        print(f"Height   : {self.height} m")
        print(f"Adjusted BMI : {bmi:.2f}")
        print(f"Category : {category}")


# Main Program
def main():
    print("===== BMI Calculator =====")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    # Decide Adult or Child
    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    # Display information
    person.print_info()


# Run Program
if __name__ == "__main__":
    main()