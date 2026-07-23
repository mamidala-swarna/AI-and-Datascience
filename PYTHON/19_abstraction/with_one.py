# With Abstraction
# There will Be Abstract Classes & Abstract Methods
# There will Be Contract Like Behaviors 
# Laptop Contract - Government said these are must features for building Laptops 
# Abstract Classes 
from abc import ABC,abstractmethod
class Laptop(ABC):
    #Abstract Methods
    @abstractmethod
    def should_have_processor(self):
        pass

    @abstractmethod
    def should_have_ram(self):
        pass

    @abstractmethod
    def should_have_hard_disk(self):
        pass

    @abstractmethod
    def should_have_network(self):
        pass
