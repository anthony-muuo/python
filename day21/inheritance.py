# inheritance test code in py


class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print(f"inhale exhale and also i have {self.eyes} eyes")

class Fish(Animal):

    def __init__(self):
        super().__init__()
        print('fish created')
    
    def breathe(self):
        super().breathe()
        print("doing this through gills and and underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.breathe()