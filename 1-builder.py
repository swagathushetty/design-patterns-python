# class House:
#     def __init__(self):
#         self.floor = None
#         self.wall = None
#         self.roof = None
#         self.furniture = {}

#     def __str__(self):
#         return f"Floor: {self.floor}\n" \
#                f"Wall: {self.wall}\n" \
#                f"Roof: {self.roof}\n" \
#                f"Furniture: {self.furniture}\n" \


# class HouseBuilder:
#     def __init__(self):
#         self.house = House()

#     def set_floor(self, amount):
#         self.house.floor = amount
    
#     def set_wall(self, amount):
#         self.house.wall = amount
    
#     def set_roof(self, amount):
#         self.house.roof = amount
    
#     def set_furniture(self, name, amount):
#         if not self.house.furniture.get(name):
#             self.house.furniture[name] = 0
#         self.house.furniture[name] += amount
    
#     def get_house(self):
#         return self.house

# class SmallHouseBuilder(HouseBuilder):
#     def build_floor(self):
#         self.set_floor("Small floor")
    
#     def build_wall(self):
#         self.set_wall("Small wall")

#     def build_roof(self):
#         self.set_roof("Small roof")
    
#     def build_furnitures(self):
#         self.set_furniture("Chairs",5)
#         self.set_furniture("Chairs", 4)
#         self.set_furniture("Tables", 8)

# class BigHouseBuilder(HouseBuilder):
#     def build_floor(self):
#         self.set_floor("Big floor")

#     def build_wall(self):
#         self.set_wall("Big wall")

#     def build_roof(self):
#         self.set_roof("Big roof")
        
#     def build_furnitures(self):
#         self.set_furniture("Sofa",30)
#         self.set_furniture("Cabinets", 28)
#         self.set_furniture("Stools", 34)
#         self.set_furniture("Leg Rest", 27)

# class Contractor: #director
#     def __init__(self, builder):
#         self.builder = builder

#     def construct_house(self):
#         self.builder.build_floor()
#         self.builder.build_wall()
#         self.builder.build_roof()
#         self.builder.build_furnitures()

# #usage
# if __name__ == "__main__":
#     small_builder = SmallHouseBuilder()
#     big_builder = BigHouseBuilder()

#     contractor = Contractor(small_builder)
#     contractor.construct_house()
#     small_house = small_builder.get_house()
#     print("Small House:")
#     print(small_house)

#     contractor = Contractor(big_builder)
#     contractor.construct_house()
#     big_house = big_builder.get_house()
#     print("Big House:")
#     print(big_house)


##########################################################################################
class Sandwich:
    def __init__(self):
        self._bread = None 
        self._meat = None 
        self._cheese = None 
        self._vegetables = [] 
        self._sauces = [] 

    def __str__(self):
        ingredients = "Bread: "+self._bread + "| Meat: " + self._meat
        if self._cheese:
            ingredients += "| Cheese: " + self._cheese
        ingredients +="| Vegetables: " + ', '.join(self._vegetables)
        ingredients += "| Sauces: " + ', '.join(self._sauces)
        return ingredients

class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()
    
    def add_bread(self):
        pass
    def add_meat(self):
        pass
    def add_cheese(self):
        pass
    def add_vegetables(self):
        pass
    def add_sauces(self):
        pass
    
    def get_sandwich(self):
        return self.sandwich 

class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "White Bread"
    
    def add_meat(self):
        self.sandwich._meat = "Chicken"
    
    def add_cheese(self):
        self.sandwich._cheese = "Cheddar"
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("tomato")
        self.sandwich._vegetables.append("lettuce")

    def add_sauces(self):
        self.sandwich._sauces.append("mayo")
        self.sandwich._sauces.append("mustard")

class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "Whole Wheat Bread"
    
    def add_meat(self):
        self.sandwich._meat = "Tofu"
    
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("spinach")
        self.sandwich._vegetables.append("Bell Pepper")

    def add_sauces(self):
        self.sandwich._sauces.append("Hummus")
        self.sandwich._sauces.append("Tahini")

class Waiter:
    def __init__(self):
        self.sandwich_builder  = None 
    
    def get_builder(self, builder):
        self.sandwich_builder = builder 
    
    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_meat()
        self.sandwich_builder.add_cheese()
        self.sandwich_builder.add_vegetables()
        self.sandwich_builder.add_sauces()
    
    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()
         

if __name__ == '__main__':
    waiter = Waiter()
    waiter.get_builder(ClubSandwichBuilder())
    waiter.create_sandwich()
    print("======CLUB SANDWICH =======")
    sandwich1 = waiter.serve_sandwich() 
    print(sandwich1)

    waiter.get_builder(VeggieSandwichBuilder())
    waiter.create_sandwich()
    print("======VEGGIE SANDWICH =======")
    sandwich2 = waiter.serve_sandwich()
    print(sandwich2)


#################################################################

class GameObject:
    def __init__(self):
        self.transform:Transform=None
        self.renderer:Renderer=None
        self.collider:Collider=None
        self.script:str=None
    def __str__(self) -> str:
        return f"Transform: {self.transform}\n"\
            f"Renderer: {self.renderer}\n"\
            f"Collider: {self.collider}\n"\
            f"Screipt: {self.script}\n"
    
class Transform:
    def __init__(self,position:tuple,rotation:tuple,scale:tuple):
        self.position = position
        self.rotation = rotation
        self.scale = scale
    def __str__(self):
           return f"Postion: {self.position}\n"\
            f"Rotation: {self.rotation}\n"\
            f"Scale: {self.scale}\n" 
class Renderer:
    def __init__(self,mesh:str,material:str):
        self.mesh = mesh
        self.material = material
    def __str__(self):
        return f"Mesh: {self.mesh}, Material:{self.material}"
    
class Collider:
    def __init__(self,shape:str,is_trigger:str):
        self.shape = shape
        self.is_trigger = is_trigger
    def __str__(self):
        return f"Shape: {self.shape}, Trigger:{self.is_trigger}"
    
class GameBuilder:
    def __init__(self):
        self._game = GameObject()
    def add_transform(self,position,rotation,scale):
        self._game.transform = Transform(position,rotation,scale)
    def add_renderer(self,mesh,material):
        self._game.renderer = Renderer(mesh,material)
    def add_collider(self,shape,is_trigger):
        self._game.collider = Collider(shape,is_trigger)
    def add_script(self,script):
        self._game.script = (script)
    def get_game(self):
        return self._game 

print('===================== ENGINE 1 ===============================')

builder = GameBuilder()
builder.add_transform((1,2,4),(4,6,2),(5,6,2))
builder.add_renderer("cubeMesh","DefaultBlackShine")
builder.add_collider("Box",False)
builder.add_script("TurnScript.js")


game1 = builder.get_game()
print(game1)
