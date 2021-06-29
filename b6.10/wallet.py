class OnlineWallet:
    def __init__(self, name="", surname="", money=0):
        self.name = name
        self.surname = surname
        self.money = money

    def set_name(self, name):
        if isinstance(self.name, str):
            self.name = name
    def set_surname(self, surname):
        if isinstance(self.surname, str):
            self.surname = surname
    def set_money(self, money):
        if self.money >= 0 and isinstance(self.money, int):
            self.money = money

    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_money(self):
        return str(self.money)

ivan = OnlineWallet()
ivan.set_name('Иван')
ivan.set_surname('Петров')
ivan.set_money(50)

print('Клиент:', ivan.get_name(), ivan.get_surname()+'.', 'Баланс:', ivan.get_money(), 'руб.')