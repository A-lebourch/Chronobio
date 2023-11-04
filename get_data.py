game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'user', 'money': 100030, 'score': 100030, 'fields': [{'content': 'PATATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD1'}, {'content': 'PATATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD2'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'PATATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD1'}, {'content': 'PATATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD2'}, {'content': 'OIGNON', 'needed_water': 0, 'bought': True, 'location': 'FIELD3'}, {'content': 'OIGNON', 'needed_water': 0, 'bought': True, 'location': 'FIELD4'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD1'}, {'content': 'PATATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD2'}, {'content': 'COURGETTE', 'needed_water': 0, 'bought': True, 'location': 'FIELD3'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD4'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'OIGNON', 'needed_water': 0, 'bought': True, 'location': 'FIELD1'}, {'content': 'POIREAU', 'needed_water': 0, 'bought': True, 'location': 'FIELD2'}, {'content': 'POIREAU', 'needed_water': 0, 'bought': True, 'location': 'FIELD3'}, {'content': 'COURGETTE', 'needed_water': 0, 'bought': True, 'location': 'FIELD4'}, {'content': 'TOMATE', 'needed_water': 0, 'bought': True, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}


def priorité_plantation(game_data):
    quantity = {'PATATE': 0, 'POIREAU': 0, 'TOMATE': 0, 'OIGNON': 0, 'COURGETTE': 0}
    for keys in game_data:
        count = []
        for i in range(len(game_data["farms"]) - 1):
            for field in range(len(game_data["farms"][i]['fields'])-1):
                if game_data["farms"][i]["fields"][field]["bought"] is True:
                    count.append(game_data["farms"][i]['fields'][field]['content'])

    for key in quantity.keys():
        quantity[key] = count.count(key)

    quantity = dict(sorted(quantity.items(), key=lambda item: item[1]))
    quantity = list(quantity.keys())
    return (quantity)


def observateur(game_data):
    for farm in range(len(game_data['farms'])):
        if game_data['farms'][farm]['name'] == 'user':
            my_farm = game_data['farms'][farm]['fields']
            for field in range(len(my_farm)):
                if my_farm[field]['needed_water'] != 10:
                    print('need water at ' + my_farm[field]['location'])
                if my_farm[field]['needed_water'] == 10:
                    print('need to be harvested at ' + my_farm[field]['location'])
                if my_farm[field]['bought'] and my_farm[field]['content'] == 'NONE':
                    print('need to be planted at' + my_farm[field]['location'])


def watch_money(game_data):
    pass
