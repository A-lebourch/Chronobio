from algorithme.modules.employees import Employees


def test_fire_employees_1():
    employees = Employees()
    employees.month = 15
    assert employees.fire()

def test_fire_employees_2():
    employees = Employees()
    employees.month = 10
    assert not employees.fire()

def test_monthly_salary_1():
    employees = Employees()
    employees.month = 12
    assert employees.monthly_salary(100_000)

def test_monthly_salary_2():
    employees = Employees()
    employees.month = 15
    assert not employees.monthly_salary(1_000)
