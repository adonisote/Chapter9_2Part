from user_privileges_admin import User, Admin, Privileges


admin0 = Admin('Anastasious', 'Administrator', 55, 'Anas')

admin0.privi.show_privileges()
admin0.describe_user()
print(admin0.age)