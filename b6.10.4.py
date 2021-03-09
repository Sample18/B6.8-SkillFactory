from wallet import OnlineWallet
ivan = OnlineWallet()
ivan.set_name('Иван')
ivan.set_surname('Петров')

class City:
    def __init__(self, city_name=''):
        self.city = city_name

    def set_city(self, city_name):
        if isinstance(self.city, str):
            self.city = city_name

    def get_city(self):
        return self.city

class Status:
    def __init__(self, status=''):
        self.status = status

    def set_status(self, status):
        if isinstance(self.status, str):
            self.status = status

    def get_status(self):
        return self.status

moscow = City()
moscow.set_city('Москва')
new_status = Status()
new_status.set_status('Наставник')
print(ivan.get_name(), ivan.get_surname()+',', 'г.', moscow.get_city()+',', 'статус', '"'+ new_status.get_status() +'"')