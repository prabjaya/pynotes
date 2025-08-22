
class UserModel():
    
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    def user_info(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    def update_age(self, new_age):
        self.age = new_age
        return f'User {self.name} has been updated to age {self.age}'
        
    def update_name(self, new_name):
        self.name = new_name
        return f'User {self.name} has been updated'


user_obj = UserModel("Bob", 31)


result = user_obj.user_info()
print('result: ', result)

updated_age  = user_obj.update_age(new_age=20)
print('updated_age: ', updated_age)

updated_name = user_obj.update_name(new_name="Alice")
print('updated_name: ', updated_name)

updated_class_values = user_obj.user_info()
print('updated_class_values: ', updated_class_values)
    