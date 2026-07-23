# Implementations -> Companies who wants to manufacture laptops 
# Dell Wants To Build Laptops

from  with_one import Laptop

class Dell(Laptop):
    def should_have_processor(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("Processor")
        print("Functionality")
        print("Present")
        
    def should_have_ram(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("RAM")
        print("Functionality")
        print("Present")
    
    # NOTE: Dell doesn't have Hard Disk and Wi-fi Network, 
    # but still able to sell the Laptops
    
    # TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 
    # 'should_have_hard_disk', 'should_have_network'

        
    def should_have_hard_disk(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("Hard Disk")
        print("Functionality")
        print("Present")
        
    def should_have_network(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("Wi-Fi Network")
        print("Functionality")
        print("Present")
        
    # NOTE: Dell now has Hard Disk and Wi-fi Network, 
    # then only able to sell the Laptops
    
    
class Lenovo(Laptop):
    def should_have_hard_disk(self):
        print("=" * 30)
        print("Lenovo")
        print("=" * 30)
        
        print("Laptop")
        print("Hard Disk")
        print("Functionality")
        print("Present")
        
    def should_have_network(self):
        print("=" * 30)
        print("Lenovo")
        print("=" * 30)
        
        print("Laptop")
        print("Wi-Fi Network")
        print("Functionality")
        print("Present")
    
    # NOTE: Lenovo doesn't have Processor and RAM, 
    # but still able to sell the Laptops
    
    