from algorithme.modules.owner import Owner
from algorithme.modules.locations import Location
from algorithme.modules.aliments import Aliment
from algorithme.modules.employees import Employees


def test_can_sell_field_1():
    owner = Owner()
    index_field = 1
    owner.fields[index_field].sow(Aliment.POTATO)
    while owner.fields[index_field].needed_water():
        owner.fields[index_field].water()
    assert owner.can_sell_field(index_field)


def test_can_sell_field_2():
    owner = Owner()
    index_field = 1
    assert not owner.can_sell_field(index_field)


def test_can_buy_tractor_1():
    owner = Owner()
    assert owner.can_buy_tractor()


def test_can_buy_tractor_2():
    owner = Owner()
    owner.money = 10_000
    assert not owner.can_buy_tractor()


def test_can_pay():
    owner = Owner()
    owner.money = 10_000
    owner.employees.append(Employees())
    owner.employees[0].month = 4
    assert owner.can_pay(0)

# def test_buy_fields():
#     owner = Owner()
#     owner.


# TODO tester si le owner est déjà occupé, dans ce cas on ne peut pas vendre
