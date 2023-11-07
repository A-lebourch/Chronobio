from algorithme.owner import Owner
from algorithme.locations import Location
from algorithme.aliments import Aliment


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


# TODO tester si le owner est déjà occupé, dans ce cas on ne peut pas vendre
