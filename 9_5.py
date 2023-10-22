class User:
    def __init__(self, first_name, last_name, age = None, alias =None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.alias = alias
        self.login_attempt = 0
    def describe_user(self):
        print(f'\nUser information. \nFirst Name: {self.first_name.title()}'
            f'\nLast Name: {self.last_name.title()}'
            f'\nAge: {self.age}'
            f'\nAlias: {self.alias}')
    def greet_user(self):
        print(f'Hello, {self.first_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempt +=1
    def reset_login_attempts(self):
        self.login_attempt = 0

instance0 = User('Pontious', 'Pilatus')
instance0.increment_login_attempts()
instance0.increment_login_attempts()
instance0.increment_login_attempts()
print(instance0.login_attempt)
instance0.reset_login_attempts()
print(instance0.login_attempt)




