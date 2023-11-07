class Employee:
    def __init__(self):
        self.month = 0
        self.salary = 1000
        self.fire_salary = 0
        self.busy = False

    def fire(self, money):
        if self.month >= 15:
            return True
        elif money > self.fire_salary:
            return True
        else:
            return False

    def monthly_salary(self, money):
        for i in range(self.month):
            self.salary = self.salary * 0.01 + self.salary

        self.fire_salary = self.salary + self.salary * 0.01 + self.salary
        return self.salary < money

    def is_busy(self):
        return self.busy
