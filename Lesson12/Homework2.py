# https://swapi.dev/
# Уважно вивчіть документацію цього API (https://swapi.dev/documentation)
# і напишіть програму, яка виводить на екран (і JSON-файл) інформацію про пілотів легендарного корабля Millennium Falcon.
#
# Інформація про корабель має містити такі пункти:
# назва,
# максимальна швидкість,
# клас,
# список пілотів.
#
# Усередині списку про кожен пілот має бути така інформація:
# ім'я,
# зріст,
# вага,
# рідна планета,
# посилання на інформацію про рідну планету.

import requests
import json


def starShipInfo(name):
    link = 'https://swapi.dev/api/starships'
    starship_name = name

    try:

        response = requests.get(link).json()
        results = response.get('results', [])
        for ship in results:
            if ship['name'] == starship_name:
                my_ship = ship

        print(f"Name: {my_ship.get('name')}")
        print(f"Max Speed: {my_ship.get('max_atmosphering_speed')}")
        print(f"Class: {my_ship.get('starship_class')}")
        pilots_list = []
        for link in my_ship.get('pilots'):
            pilot = requests.get(link).json()
            planet = requests.get(pilot['homeworld']).json()
            new_pilot = {
                'Name': pilot['name'],
                'Height': pilot['height'],
                'Mass': pilot['mass'],
                'Homeworld': planet['name'],
                'Homeworld_info': pilot['homeworld']
                }
            pilots_list.append(new_pilot)
        print(f'Pilots: {pilots_list}')
        ship_information = {
            'Name': my_ship.get('name'),
            'Max Speed': my_ship.get('max_atmosphering_speed'),
            'Class': my_ship.get('starship_class'),
            'Pilots': pilots_list
        }
        return ship_information
    except NameError:
        print(f"There aren't any ships with {starship_name} name")


if __name__ == '__main__':
    ship_info = starShipInfo('Millennium Falcon')
    with open('ship_info.json', 'w') as file:
        json.dump(ship_info, file, indent=4)