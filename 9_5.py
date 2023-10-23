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



class Admin(User):
    def __init__(self, first_name, last_name, age = None, alias = None):
        super().__init__(first_name, last_name, age, alias)
        self.privi = Privileges()
    



class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        return self.privileges

admin0 = Admin('Pontious', 'Pilatus')
admin0.describe_user()
admin0.greet_user()

print(admin0.privi.show_privileges())