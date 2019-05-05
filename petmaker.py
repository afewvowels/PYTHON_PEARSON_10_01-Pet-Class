# Import from Pet class file
import pet

# Define main function
def main():
    # Create new Pet object
    newpet = pet.Pet()

    # Get pet info from user input
    newpet.set_name(input('What\'s your pet\'s name? '))
    newpet.set_animal_type(input('What kind of animal is your pet? '))
    newpet.set_age(int(input('How old is your animal? ')))

    # Output information recieved from user
    print('Your pet\'s name is ', newpet.get_name())
    print('Your pet is a ', newpet.get_animal_type())
    print('Your pet\'s age is ', newpet.get_age())

# Call main function
main()
