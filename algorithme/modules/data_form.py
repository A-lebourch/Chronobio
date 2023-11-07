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


class Owner(BaseModel):
    blocked: bool
    name: str
    money: int
    score: int
    fields: list[Field]
    tractors: list[Tractor]
    loans: list[Loan]
    soup_factory: Soup_factory
    employees: list[dict]
    events: list


class generale(BaseModel):
    day: int
    greenhouse_gas: int
    events: list
    farms: list[Owner]


if __name__ == "__main__":
    game_data2 = {
        "day": 76,
        "greenhouse_gas": 15200,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "user",
                "money": 102773,
                "score": 1940,
                "fields": [
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD2",
                    },
                    {
                        "content": "POTATO",
                        "needed_water": 10,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [
                    {"location": "FARM", "id": 1},
                    {"location": "FARM", "id": 2},
                ],
                "loans": [{"amount": 100000, "start_day": 0}],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 2,
                        "LEEK": 0,
                        "TOMATO": 3,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [
                    {"id": 1, "location": "FIELD3", "tractor": None, "salary": 1021},
                    {"id": 2, "location": "FARM", "tractor": None, "salary": 1021},
                ],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    game_data = generale(**game_data2)
    print(game_data.farms[0].fields[0].content)
