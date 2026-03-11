class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        print('Ejecutando método __new__')
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj
    
class My_Class(metaclass=My_Meta):
    def __init__(self):
        print('Ejecutando método __main__')

print(My_Class.__dict__)

my_object = My_Class()

print(my_object.__dict__)
print(my_object.custom_attribute)