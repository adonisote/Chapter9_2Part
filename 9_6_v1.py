class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'{self.name.title()}, {self.type()}')
    def describe_restaurant(self):
        print(f'{self.name.title()} is open now!')

    def set_number_served(self, new_value):
        self.number_served = new_value
    def increment_number_served(self):
        self.number_served += 20
    def read_number_served(self):
        print(f'The number of customer served is {self.number_served}')


class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors):
        super().__init__(name,type)
        self.flavors = flavors

    def display_flavors(self):
        return self.flavors

ice_stand0 = IceCreamStand('Pilatus\'s', 'Ice Cream Stand', ['strawberry', 'chocolate', 'napolitano'])

print(ice_stand0.display_flavors())