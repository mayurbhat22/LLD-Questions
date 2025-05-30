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

    

#Products
class Button:
    def render(self):
        pass
class Alert:
    def show(self):
        pass

#Concrete Products
class AndroidButton(Button):
    def render(self):
        print("Android style Button")

class IOSButton(Button):
    def render(self):
        print("IOS Style Button")

class AndroidAlert(Alert):
    def show(self):
        print("Android-style Alert")

class IOSAlert(Alert):
    def show(self):
        print("IOS-style Alert")

#Abstract Factory
class UIFactory(ABC):
    def create_button(self): pass
    def create_alert(self): pass

#Android Factory
class AndroidFactory(UIFactory):
    def create_button(self):
        return AndroidButton()
    
    def create_alert(self):
        return AndroidAlert()

#IOS Factory
class IOSFactory(UIFactory):
    def create_button(self):
        return IOSButton()

    def create_alert(self):
        return IOSAlert

def render_ui(factory: UIFactory):
    alert = factory.create_alert()
    button = factory.create_button()
    alert.show()
    button.show()

render_ui(AndroidFactory())



























