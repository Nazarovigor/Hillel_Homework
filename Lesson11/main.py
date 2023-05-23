from Homework import  *

if __name__ == '__main__':
    Human.default_info()
    person = Human('John Snow', 25)
    person.info()
    house = SmallHouse(3000)
    person.buy_house(house, 20)
    person.earn_money()
    person.buy_house(house, 20)
    person.info()