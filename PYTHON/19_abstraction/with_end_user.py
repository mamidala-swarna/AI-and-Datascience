# Without Abstraction End User

from with_two import Dell,Lenovo

# End User Buying Dell Laptop 
print("=" * 50)
print("     Customer Buying Dell Laptop")
print("=" * 50)

from  with_one import Laptop
dellObject = Dell()
dellObject.should_have_processor()
dellObject.should_have_ram()
dellObject.should_have_hard_disk()
dellObject.should_have_network()