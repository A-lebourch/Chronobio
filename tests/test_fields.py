from algorithme.modules.field import Field


def test_is_sowable_1():
    field = Field()
    assert field.is_sowable()


def test_is_sowable_2():
    field = Field()
    field.content = "POTATO"
    assert not field.is_sowable()


def test_needed_water_1():
    field = Field()
    assert not field.needed_water()


def test_needed_water_2():
    field = Field()
    field.content = "POTATO"
    field.water_lvl = 0
    assert not field.needed_water()


def test_needed_water_3():
    field = Field()
    field.content = "NONE"
    field.water_lvl = 5
    assert not field.needed_water()


def test_needed_water_4():
    field = Field()
    field.content = "POTATO"
    field.water_lvl = 5
    assert field.needed_water()


def test_can_harvest_sell_1():
    field = Field()
    assert not field.can_harvest_sell()


def test_can_harvest_sell_2():
    field = Field()
    field.content = "POTATO"
    field.water_lvl = 0
    assert field.can_harvest_sell()


def test_can_harvest_sell_3():
    field = Field()
    field.content = "POTATO"
    field.water_lvl = 5
    assert not field.can_harvest_sell()


def test_can_harvest_sell_4():
    field = Field()
    field.content = "NONE"
    assert not field.can_harvest_sell()


def test_sow():
    field = Field()
    field.sow("POTATO")
    assert not field.is_sowable()


def test_water():
    field = Field()
    field.sow("POTATO")
    field.water_lvl = 5
    field.water()
    assert field.water_lvl == 4
