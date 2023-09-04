from S1E9 import Character

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive, "Lannister", "blue", "light")
        
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def do_smth(self):
        return vars(self).fromkeys(["family_name", "eyes", "hairs"])


class Baratheon(Character):
        def __init__(self, first_name, is_alive=True):
            super().__init__(first_name, is_alive, "Baratheon", "brown", "dark")
            
        def __str__(self):
            return self.__repr__()

        def __repr__(self):
            return f"Vector: {self.family_name, self.eyes, self.hairs}"

        def do_smth(self):
            return vars(self).fromkeys(["family_name", "eyes", "hairs"])

