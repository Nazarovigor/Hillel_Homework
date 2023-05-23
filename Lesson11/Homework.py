
class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def __str__(self):
        return f"I'm your house with area {self._area}"

    @staticmethod
    def discount_validate(discount):
        while True:
            try:
                if 0 < int(discount) < 100:
                    return discount
                else:
                    print("Your discount can't be less or = 0% or more or = 100%")
            except ValueError:
                print('Wrong money value, try again.')

    def final_price(self, discount):
        discount = House.discount_validate(discount)
        new_price = self._price - (self._price*discount/100)
        return new_price


class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)


class Human:

    default_name = 'Ivan'
    default_age = 29

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'House: {self.__house}')
        print(f'Money: {self.__money}')

    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age:{Human.default_age}')

    @staticmethod
    def money_input_validate():
        while True:
            try:
                earn_money = int(input('How much money do you want to earn? '))
                if earn_money > 0:
                    return earn_money
                else:
                    print(f"You can't earn {earn_money} money")
            except ValueError:
                print('Wrong money value, try again.')

    def earn_money(self):
        new_money = Human.money_input_validate()
        self.__money = new_money
        return self.__money

    def _make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print("Deal made. House purchased.")
        else:
            print("Insufficient funds to buy the house.")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        self._make_deal(house, final_price)

