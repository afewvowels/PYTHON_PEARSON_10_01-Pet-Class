# Create a pet class that stores an
# animal's name, type, and age with
# accessors and mutators
class Pet:
    #initialize with null values
    def __init__(self):
        self.__name = 'null'
        self.__animal_type = 'null'
        self.__age = -1

    # Set name mutator
    def set_name(self, name):
        self.__name = name

    # Set animal type mutator
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Set age mutator
    def set_age(self, age):
        self.__age = age

    # Get name accessor
    def get_name(self):
        return self.__name

    # Get animal type accessor
    def get_animal_type(self):
        return self.__animal_type

    # Get age getter
    def get_age(self):
        return self.__age
