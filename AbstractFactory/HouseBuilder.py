from abc import ABC,abstractmethod

# product 1
class Furniture(ABC):
    def __init__(self,quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass


class Chair(Furniture):
      def display(self):
        return f"{self.quantity} Chair"
      
class Sofa(Furniture):
      def display(self):
        return f"{self.quantity} Sofa"

# product 2
##############################################################################
class Electronic(ABC):
    def __init__(self,quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass

class Radio(Electronic):
      def display(self):
        return f"{self.quantity} Radio(s)"


class Television(Electronic):
      def display(self):
        return f"{self.quantity} Television(s)"

# product 3
##################################################################################
class Decoration(ABC):
    def __init__(self,quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass

class Flowervase(Decoration):
      def display(self):
        return f"{self.quantity} Flowervase(s)"
      


class Chandalier(Decoration):
      def display(self):
        return f"{self.quantity} Chandalier(s)"
      

#################### product factories ##############################


class HouseFactory(ABC):

    @abstractmethod
    def furniture(self):
        pass 


    @abstractmethod
    def electronic(self):
        pass 


    @abstractmethod
    def decoration(self):
        pass 


class SmallHouse(HouseFactory):

    def furniture(self):
        return Chair(4)
    
    def electronic(self):
        return Radio(2)
    
    def decoration(self):
        return Flowervase(1)
        
class BigHouse(HouseFactory):

    def furniture(self):
        return Sofa(10)
    
    def electronic(self):
        return Television(7)
    
    def decoration(self):
        return Chandalier(6)
    

def client(factory:HouseFactory):
    print("Furniture: ",factory.furniture().display())
    print("Electronic: ",factory.electronic().display())
    print("Decoration: ",factory.decoration().display())

client(SmallHouse())

print('*****')

client(BigHouse())