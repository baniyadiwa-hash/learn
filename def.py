
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}")

    def set_name(self, name, age, salary):
        return

a = Person("Ram", 67, 343456)
print(a.get_name())
