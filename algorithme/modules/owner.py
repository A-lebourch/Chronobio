from algorithme.modules.field import Field
from algorithme.modules.employees import Employees
from algorithme.modules.locations import Location


class Owner:
    def __init__(self):
        self.money = 100_000
        self.fields: list[Field] = [Field(Location.FIELD1), Field(Location.FIELD2), Field(Location.FIELD3), Field(Location.FIELD4), Field(Location.FIELD5)]
        self.employees: list[Employees] = []

    def can_buy_tractor(self):
        return self.money > 30_000

    def can_sell_field(self, field_index):
        return self.fields[field_index].can_harvest_sell()

    def can_pay(self, employee_index):
        return self.employees[employee_index].monthly_salary(self.money)

# ################################### 

    
    def can_buy_field(self):
        return self.money > 10_000

    def can_hire(self):
        pass

    def can_fire(self):
        return self.emp_time >= 15

    def employee_location(self):
        pass
