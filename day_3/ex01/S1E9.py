from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, first_name, is_alive=True, family_name="", eyes="", hairs=""):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        if not self.is_alive:
            print(f"{self.first_name} is already dead!")
        else:
            self.is_alive = False
            print(f"{self.first_name} died!")

class Stark(Character):
    def __init__(self, first_name, is_alive=True):
            super().__init__(first_name, is_alive)
