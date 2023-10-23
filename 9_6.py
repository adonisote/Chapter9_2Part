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

restaurant = Restaurant('Las delicias de alicia', 'latin')
print(restaurant.number_served)

restaurant.number_served = 40
print(restaurant.number_served)

restaurant.set_number_served(60)
print(restaurant.number_served)

restaurant.increment_number_served()
restaurant.read_number_served()

restaurant.increment_number_served()
restaurant.read_number_served()
