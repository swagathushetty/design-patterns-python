from abc import ABC,abstractmethod

class Product(ABC):

    @abstractmethod
    def operation(self):
        pass 

class ConcreteProductA(Product):

    def operation(self):
        return "concrete product A operation"
    
class ConcreteProductB(Product):

    def operation(self):
        return "concrete product B operation"


class Creator(ABC):

    @abstractmethod
    def factory_method(self) -> Product:
        pass 

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteCreatorB()

creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()