from algorithme.modules.owner import Owner
from algorithme.modules.aliments import Aliment


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


def test_can_sell_field_3():
    owner = Owner()
    index_field = 1
    owner.day_invalid = 1
    assert not owner.can_sell_field(index_field)


def test_can_buy_tractor_1():
    owner = Owner()
    assert owner.can_buy_tractor()


def test_can_buy_tractor_2():
    owner = Owner()
    owner.money = 10_000
    assert not owner.can_buy_tractor()


def test_can_buy_tractor_3():
    owner = Owner()
    owner.day_invalid = 1
    owner.money = 10_000
    assert not owner.can_buy_tractor()


def test_can_hire_1():
    owner = Owner()
    owner.money = 10_000
    assert owner.can_hire()


def test_can_hire_2():
    owner = Owner()
    owner.money = 900
    assert not owner.can_hire()


def test_can_hire_3():
    owner = Owner()
    owner.day_invalid = 1
    owner.money = 10_000
    assert not owner.can_hire()


def test_can_hire_4():
    owner = Owner()
    owner.day_invalid = 1
    owner.money = 900
    assert not owner.can_hire()


def test_hire_1():
    owner = Owner()
    owner.hire()
    assert len(owner.employees) == 1
    owner.hire()
    assert len(owner.employees) == 2


def test_can_pay_1():
    owner = Owner()
    owner.money = 10_000
    owner.hire()
    owner.hire()
    assert owner.can_pay()


def test_can_pay_2():
    owner = Owner()
    owner.money = 900
    owner.hire()
    owner.hire()
    assert not owner.can_pay()


def test_sell_field_1():
    owner = Owner()
    index_field = 1
    owner.fields[index_field].sow(Aliment.POTATO)
    while owner.fields[index_field].needed_water():
        owner.fields[index_field].water()
    assert owner.sell_field(index_field)


def test_sell_field_2():
    owner = Owner()
    index_field = 1
    assert not owner.sell_field(index_field)


def test_sell_field_3():
    owner = Owner()
    index_field = 1
    owner.fields[index_field].sow(Aliment.POTATO)
    while owner.fields[index_field].needed_water():
        owner.fields[index_field].water()
    owner.day_invalid = 1
    assert not owner.sell_field(index_field)
