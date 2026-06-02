class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name,"working.......")

class Manager(Employee):
    def __init__(self, name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def showDetails(self):
        print("name is ",self.name,"salary is ",self.salary,"dept is ",self.department)

manag = Manager("shibu",5,"ceo")
manag.work()
manag.showDetails()