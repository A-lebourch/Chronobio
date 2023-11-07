from algorithme.modules.employees import Employee


def test_fire_employee_1():
    employee = Employee()
    employee.month = 15
    assert employee.fire(10_000)


def test_fire_employee_2():
    employee = Employee()
    employee.month = 10
    assert not employee.fire(0)


def test_monthly_salary_1():
    employee = Employee()
    employee.month = 12
    assert employee.monthly_salary(money=100_000)


def test_monthly_salary_2():
    employee = Employee()
    employee.month = 15
    assert not employee.monthly_salary(1_000)


def test_busy_employee_1():
    employee = Employee()
    employee.busy = True
    assert employee.is_busy()
