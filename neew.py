# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Define a function to create a Person instance and display its information
def create_and_display_person(name, age):
    person = Person(name, age)
    person.display_info()

# Example usage of the function
create_and_display_person("Alice", 30)
