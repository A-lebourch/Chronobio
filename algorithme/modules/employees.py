class Employees:
    def __init__(self):
        self.month = 0
        self.salary = 1000

    def fire(self):
        if self.month >= 15:
            return True
        else:
            return False

    def monthly_salary(self, money):
        for i in range(self.month):
            self.salary = 1000 * 0.01 + self.salary
            print(self.salary)
        return self.salary < money
    
    
