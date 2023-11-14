class Employee:
    def __init__(self):
        self.salary = 1000
        self.fire_salary = 0
        self.busy = False

    def fire(self, money):
        if self.salary >= 1161:
            return True
        elif money > self.fire_salary:
            return True
        else:
            return False

    def monthly_salary(self, money):
        self.salary = int(self.salary * 0.01) + self.salary

        self.fire_salary = int(self.salary) + int(self.salary * 0.01)
        +int(self.salary)
        return self.salary < money

    def is_busy(self):
        return self.busy
