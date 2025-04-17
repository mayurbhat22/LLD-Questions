from abc import ABC, abstractmethod
class Home:
    def __init__(self):
        self.has_garage = False
        self.has_swimming_pool = False
        self.has_garden = False
    
    def get_results(self):
        print(f"Home with Has Garage: {self.has_garage}, Has_Garden: {self.has_garden}, Has_Swimming_Pool: {self.has_swimming_pool}")
    
class Builder(ABC):
    @abstractmethod
    def build_garage(self):
        pass
    @abstractmethod
    def build_swimming_pool(self):
        pass
    @abstractmethod
    def build_garden(self):
        pass
    @abstractmethod
    def get_home(self):
        pass

class NormalHome(Builder):
    def __init__(self):
        self.home = Home()
    
    def build_garage(self):
        self.home.has_garage = True
    
    def build_garden(self):
        self.home.has_garden = True
    
    def build_swimming_pool(self):
        self.home.has_swimming_pool = False

    def get_home(self):
        return self.home

class LuxuryHome(Builder):
    def __init__(self):
        self.home = Home()
    
    def build_garage(self):
        self.home.has_garage = True
    
    def build_garden(self):
        self.home.has_garden = True
    
    def build_swimming_pool(self):
        self.home.has_swimming_pool = True

    def get_home(self):
        return self.home

class Director:
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
    
    def build_normalhome(self):
        self._builder.build_garage()
        self._builder.build_garden()
        self._builder.build_swimming_pool()
    
    def build_luxuryhome(self):
        self._builder.build_garage()
        self._builder.build_garden()
        self._builder.build_swimming_pool()
    
    def get_home(self):
        self._builder.get_home().get_results()


if __name__ == "__main__":
    normal_home = NormalHome()
    director = Director()
    director.builder = normal_home

    director.build_normalhome()
    director.get_home()  

    luxury_home = LuxuryHome()
    director.builder = luxury_home
    director.build_luxuryhome()
    director.get_home()  
