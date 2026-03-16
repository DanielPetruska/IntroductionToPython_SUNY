class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = None
        self.phone = None

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_phone(self, phone):
        self.phone = phone

    def __str__(self):
        return f"{self.firstname} {self.lastname}, Birthdate: {self.birthdate}, Phone: {self.phone}"

class Employee(Person):
    def __init__(self, firstname, lastname, company, salary):
        super().__init__(firstname, lastname)
        self.company = company
        self.salary = salary

    def __str__(self):
        return f"{self.firstname} {self.lastname}, Birthdate: {self.birthdate}, Phone: {self.phone}, Company: {self.company}, Salary: {self.salary}"


p1 = Person("John", "Smith")
p1.set_birthdate("1999-04-12")
p1.set_phone("555123456")

e1 = Employee("Anna", "Brown", "Microsoft", 5000)
e1.set_birthdate("1995-08-21")
e1.set_phone("555987654")

print(p1)
print(e1)