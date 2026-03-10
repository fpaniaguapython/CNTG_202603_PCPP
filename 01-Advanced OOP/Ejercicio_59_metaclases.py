class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj
    
class My_Class(metaclass=My_Meta):
    pass

print(My_Class.__dict__)

my_object = My_Class()

print(my_object.__dict__)
print(my_object.custom_attribute)