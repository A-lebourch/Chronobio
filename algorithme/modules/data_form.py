from typing import Union
from pydantic import BaseModel


class Field(BaseModel):
    content: str
    needed_water: int
    bought: bool
    location: str


class Tractor(BaseModel):
    location: str
    id: int


class Loan(BaseModel):
    amount: int
    start_day: int


class Soup_factory(BaseModel):
    days_off: int
    stock: dict


class Employee(BaseModel):
    id: int
    location: str
    tractor: Union[None, Tractor]
    salary: int


class Owner(BaseModel):
    blocked: bool
    name: str
    money: int
    score: int
    fields: list[Field]
    tractors: list[Tractor]
    loans: list[Loan]
    soup_factory: Soup_factory
    employees: list[Employee]
    events: list


class General(BaseModel):
    day: int
    greenhouse_gas: int
    events: list
    farms: list[Owner]