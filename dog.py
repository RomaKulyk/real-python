class Dog:
    species = "Canis familiaris" # CLASS ATTRIBUTES
    def __init__(self, name, age):
        
        """
        Every time you create a new Dog object, __init__() sets the initial
        state of the object by assigning the values of the object properties.
        """
        self.name = name # creates an INSTANCEATTRIBUTE called name and 
        # assigns the value of the name parameter to it.
        self.age = age # creates ans INSTANCEATTRIBUTE called name and 
        # assigns the valuef of the age parameter to it.
        # Attributes created in __init__() are called INSTANCE ATTRIBUTES.
        # An instance attribute's value is specific to a particular instance
        # of the class.
    
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks {sound}"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
       return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

