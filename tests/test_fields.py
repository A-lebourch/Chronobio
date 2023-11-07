from algorithme.field import Field
from algorithme.locations import Location
from algorithme.aliments import Aliment


def test_is_sowable_1():
    field = Field(Location.FIELD1)
    assert field.is_sowable()


def test_is_sowable_2():
    field = Field(Location.FIELD1)
    field.content = Aliment.POTATO
    assert not field.is_sowable()


def test_needed_water_1():
    field = Field(Location.FIELD1)
    assert not field.needed_water()


def test_needed_water_2():
    field = Field(Location.FIELD1)
    field.content = Aliment.POTATO
    field.water_lvl = 0
    assert not field.needed_water()


def test_needed_water_3():
    field = Field(Location.FIELD1)
    field.content = Aliment.NONE
    field.water_lvl = 5
    assert not field.needed_water()


def test_needed_water_4():
    field = Field(Location.FIELD1)
    field.content = Aliment.POTATO
    field.water_lvl = 5
    assert field.needed_water()


def test_can_harvest_sell_1():
    field = Field(Location.FIELD1)
    assert not field.can_harvest_sell()


def test_can_harvest_sell_2():
    field = Field(Location.FIELD1)
    field.content = Aliment.POTATO
    field.water_lvl = 0
    assert field.can_harvest_sell()


def test_can_harvest_sell_3():
    field = Field(Location.FIELD1)
    field.content = Aliment.POTATO
    field.water_lvl = 5
    assert not field.can_harvest_sell()


def test_can_harvest_sell_4():
    field = Field(Location.FIELD1)
    field.content = Aliment.NONE
    assert not field.can_harvest_sell()


def test_sow():
    field = Field(Location.FIELD1)
    field.sow()
    assert not field.is_sowable()


def test_water():
    field = Field(Location.FIELD1)
    field.sow(Aliment.POTATO)
    field.water_lvl = 5
    field.water()
    assert field.water_lvl == 4
