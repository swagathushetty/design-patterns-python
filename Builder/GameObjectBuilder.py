
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


#############################################################################################################
from typing import List
class QueryBuilder:
    def __init__(self):
        self._query=""
    
    def select(self,columns:List):
        self._query += f"SELECT {', '.join(columns)} "
        return self

    def from_(self,table):
        self._query += f"FROM {table}"
        return self
    
    def where(self,conditions:List):
        self._query += f"WHERE  {' AND '.join(conditions)}"
        return self
    
    def order_by(self,columns:List):
        self._query += f"ORDER BY {', '.join(columns)}"
        return self
    
    def group_by(self,columns:List):
        self._query += f"GROUP BY {', '.join(columns)}"
        return self

    def limit(self,limit):
        self._query += f"LIMIT {limit}"
        return self
    
    def get_query(self):
        return self._query
    

if __name__=='__main__':
    query_builder = QueryBuilder()

    query = query_builder.select(['name','age']).from("users")\
                            .where([
                                "age > 25",
                                "gender = 'male'"
                            ])