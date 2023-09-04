from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        pass

class Stark(Character):
    def __init__(self, first_name, is_alive=True):
            super().__init__(first_name, is_alive)

    def die(self):
        if not self.is_alive:
            print(f"{self.first_name} is already dead!")
        else:
            self.is_alive = False
            print(f"{self.first_name} died!")
    

    def reborn(self):
        """
        this is a beutiful docstring
        """
        if not self.is_alive:
            self.is_alive = True
            print(f"{self.first_name} was reborn!")
        else:
            print(f"{self.first_name} is alive!")





def main():

    try:
        c = Character("name")
    except Exception as e:
        print(e)

    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    Lyanna.reborn()
    Lyanna.reborn()
    print(Lyanna.reborn.__doc__)



if __name__ == "__main__":
    main()
    