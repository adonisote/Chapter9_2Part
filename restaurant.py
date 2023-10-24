class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'{self.name.title()} {self.type.title()}')


    def set_number_served(self, new_value):
        self.number_served = new_value
    def increment_number_served(self):
        self.number_served += 20
    def read_number_served(self):
        print(f'The number of customer served is {self.number_served}')


r1 = Restaurant('Pilatus', 'Food')
r1.describe_restaurant()