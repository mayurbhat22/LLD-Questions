from abc import ABC, abstractmethod

#Product Interface
class AbstractSofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

#Concrete Products
class ModernSofa(AbstractSofa):
    def lie_on(self):
        return "Lying on Modern Sofa"

class VintageSofa(AbstractSofa):
    def lie_on(self):
        return "Lying on Vintage Sofa"


class AbstractChair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

#Concrete Products
class ModernChair(AbstractChair):
    def lie_on(self):
        return "Lying on Modern Chair"

class VintageChair(AbstractChair):
    def lie_on(self):
        return "Lying on Vintage Chair"

#AbstractFactory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass
    
    def create_sofa(self) -> AbstractSofa:
        pass

#Concrete Factories
class ModernFactory(FurnitureFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()
    
    def create_sofa(self) -> AbstractSofa:
        return ModernSofa()

class VintageFactory(FurnitureFactory):
    def create_chair(self) -> AbstractChair:
        return VintageChair()
    
    def create_sofa(self) -> AbstractSofa:
        return VintageFactory()

def abstact_client(self, factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    