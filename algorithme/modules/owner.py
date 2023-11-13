from algorithme.modules.field import Field
from algorithme.modules.employees import Employee
from algorithme.modules.locations import Location


class Owner:
    """
    a class for farm owner
    """

    def __init__(self):
        self.money = 100_000
        self.fields: list[Field] = [
            Field(Location.FIELD1),
            Field(Location.FIELD2),
            Field(Location.FIELD3),
            Field(Location.FIELD4),
            Field(Location.FIELD5),
        ]
        self.employees: list[Employee] = []
        self.day_invalid: int = 0

    def can_buy_tractor(self):
        if self.day_invalid == 0:
            return self.money > 30_000
        else:
            return False

    def can_sell_field(self, field_index):
        if self.day_invalid == 0:
            return self.fields[field_index].can_harvest_sell()
        else:
            return False

    def can_pay(self):
        value = None
        for i in range(len(self.employees)):
            value = self.employees[i].monthly_salary(self.money)
            self.money -= self.employees[i].salary
        return value

    def sell_field(self, field_index):
        if self.can_sell_field(field_index):
            self.day_invalid = 2
            return True
        else:
            return False

    def can_buy_field(self):
        if self.day_invalid == 0:
            return self.money > 10_000
        else:
            return False

    def can_hire(self):
        if self.day_invalid == 0:
            if self.money > 1000:
                return True
            else:
                return False
        else:
            return False

    def hire(self):
        if self.can_hire():
            self.employees.append(Employee())

    # def can_fire(self):
    #     if self.day_invalid == 0:
    #         return self.emp_time >= 15
    #     else:
    #         return False

    def employee_add_order(self, order, employee):
        pass
