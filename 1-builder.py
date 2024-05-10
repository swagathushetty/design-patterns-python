
class House:
    def __init__(self):
        self.floor = None
        self.wall = None
        self.roof = None
        self.furniture = {}
    
    def __str__(self):
        return f"Floor: {self.floor}\n" \
                f"Wall: {self.wall}\n" \
                f"Roof: {self.roof}\n" \
                f"Furniture: {self.furniture}"
    
class HouseBuilder:
    def __init__(self) -> None:
        self.house = House()

    def set_floor(self,amount):
        self.house.floor = amount
        return self
    
    def set_wall(self,amount):
        self.house.wall = amount
        return self
    
    def set_roof(self,amount):
        self.house.roof = amount
        return self
    
    def get_house(self):
        return self.house

    def set_furniture(self,name:str,amount:int):
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount
        return self
    
small_house_builder = HouseBuilder()
small_house_builder.set_floor(10).set_wall(10).set_roof(23).set_furniture("chair",20).set_furniture("chair",4)
small_house = small_house_builder.get_house()
print(small_house)



big_house_builder = HouseBuilder()
big_house_builder.set_floor(10).set_wall(10).set_furniture("chair",20).set_furniture("chair",4)
big_house = big_house_builder.get_house()
print(big_house)

