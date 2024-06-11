class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New" 
    
    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer" )
            self.size = None
        else:
            self.size = size
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
