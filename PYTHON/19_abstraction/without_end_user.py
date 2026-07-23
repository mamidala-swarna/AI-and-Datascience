#Without Abstraction End User
from without_two import Dell,Lenovo

#End User Buying Dell Laptop
print("=" * 50)
print("     customer Buying Dell Laptop")
print("="  *50)

dellObject=Dell()
dellObject.should_have_processor()
dellObject.should_have_ram()