# You are building a Food Delivery Billing System. Create a class Order with a method
# calculate_total(*items) that uses *args to sum item prices regardless of how many items
# are passed (simulated method overloading). Then create a base class DeliveryService
# with a method deliver(), and derived classes BikeDelivery, CarDelivery, and
# DroneDelivery that each override deliver() to print a different delivery message (method
# overriding). Demonstrate runtime polymorphism by looping through a list of mixed
# delivery objects and calling deliver() on each.

class order:
    def total(self,*args):
        return sum(args)
class DeliveryService:
    def deliver(self):
        print("Delivery in progress...")
class BikeDelivery(DeliveryService):
    def deliver(self):
        print("Bike delivery in progress...")
class CarDelivery(DeliveryService):
    def deliver(self):
        print("Car delivery in progress...")
class DroneDelivery(DeliveryService):
    def deliver(self):
        print("Drone delivery in progress...")

o1=order()
print ("Menu:\n1. Pizza = 1000\n2. Burger = 500\n3. Pasta = 900\n4. Biryani = 400")
print("Enter menu items by there number (1-4) and type 0 when finished.")
total=[0]
while True:
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        item1=1000
        total.append(item1)
    elif choice == 2:
        item2=500
        total.append(item2)
    elif choice == 3:
        item3=900
        total.append(item3)
    elif choice == 4:
        item4=400
        total.append(item4)
print("Pick a delivery method:\n1. Bike Delivery: Rs 100\n2. Car Delivery: Rs 200\n3. Drone Delivery: Rs 300")
method=input("Enter your choice (1/2/3): ")
if method=='1':
    d1=BikeDelivery()
    total.append(100)
    t1=o1.total(*total)
    print("Total amount:",t1)
    d1.deliver()
elif method=='2':
    d1=CarDelivery() 
    total.append(200)
    t1=o1.total(*total)
    print("Total amount:",t1)
    d1.deliver()
elif method=='3':
    d1=DroneDelivery()
    total.append(300)
    t1=o1.total(*total)
    print("Total amount:",t1)
    d1.deliver()