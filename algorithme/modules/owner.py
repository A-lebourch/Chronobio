from algorithme.modules.data_form import SoupFactory, General
from algorithme.modules.field import Field
from algorithme.modules.employees import Employee


class Owner:
    """
    a class for farm owner
    """

    def __init__(self):
        self.money = 100_000
        self.fields: list[Field] = [
            Field(),
            Field(),
            Field(),
            Field(),
            Field(),
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

    def can_fire(self, employee):
        if self.day_invalid == 0:
            if self.employees[employee].salary > 1161:
                return True
        else:
            return False

    def employee_add_order(self, order, employee):
        pass


def all_vegetables(factory: SoupFactory) -> bool:
    return all(
        vegetable_stock != 0 for vegetable_stock in factory.stock.values()
    )


def is_factory_stopped(soup_factory: SoupFactory):
    return soup_factory.days_off != 0


def priority_plantation(game_data: General):
    quantity = {
        "PATATE": 0,
        "POIREAU": 0,
        "TOMATE": 0,
        "OIGNON": 0,
        "COURGETTE": 0,
    }
    count = []
    for owner in range(len(game_data.farms)):
        for field in range(len(owner.farms[owner].fields)):
            if game_data.farms[owner].fields["bought"] is True:
                count.append(game_data.farms[owner].fields["content"])

    for key in quantity.keys():
        quantity[key] = count.count(key)

    quantity = dict(sorted(quantity.items(), key=lambda item: item[1]))
    quantity = list(quantity.keys())
    return quantity
