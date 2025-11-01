"""
Smart Vehicle Classifier - Main Demonstration
Demonstrates OOP concepts and vehicle classification
"""

from vehicle import Vehicle, Car, Bike, classify_vehicle, classify_vehicle_advanced


def main():
    print("=" * 60)
    print("Smart Vehicle Classifier - OOP Demonstration")
    print("=" * 60)
    print()
    
    # Create Car instances
    print("Creating Car instances...")
    car1 = Car("Toyota", "Camry", 80, num_doors=4)
    car2 = Car("Tesla", "Model 3", 120, num_doors=4)
    print()
    
    # Create Bike instances
    print("Creating Bike instances...")
    bike1 = Bike("Giant", "TCR", 35, bike_type="Road")
    bike2 = Bike("Trek", "X-Caliber", 25, bike_type="Mountain")
    print()
    
    # Display vehicle information (demonstrating method overriding)
    print("=" * 60)
    print("VEHICLE INFORMATION (Method Overriding Demonstration)")
    print("=" * 60)
    print()
    
    print("Car 1:")
    print(car1.display_info())
    print()
    
    print("Car 2:")
    print(car2.display_info())
    print()
    
    print("Bike 1:")
    print(bike1.display_info())
    print()
    
    print("Bike 2:")
    print(bike2.display_info())
    print()
    
    # Demonstrate encapsulation with getters
    print("=" * 60)
    print("ENCAPSULATION DEMONSTRATION (Using Getters)")
    print("=" * 60)
    print()
    
    print(f"Car 1 - ID: {car1.get_id()}, Brand: {car1.get_brand()}, Model: {car1.get_model()}")
    print(f"Car 1 - Type: {car1.get_type()}, Speed: {car1.get_speed()} km/h")
    print(f"Car 1 - Doors: {car1.get_num_doors()}")
    print()
    
    print(f"Bike 1 - ID: {bike1.get_id()}, Brand: {bike1.get_brand()}, Model: {bike1.get_model()}")
    print(f"Bike 1 - Type: {bike1.get_type()}, Speed: {bike1.get_speed()} km/h")
    print(f"Bike 1 - Bike Type: {bike1.get_bike_type()}")
    print()
    
    # Demonstrate encapsulation with setters
    print("=" * 60)
    print("ENCAPSULATION DEMONSTRATION (Using Setters)")
    print("=" * 60)
    print()
    
    print(f"Bike 2 current speed: {bike2.get_speed()} km/h")
    bike2.set_speed(45)
    print(f"Bike 2 new speed after setter: {bike2.get_speed()} km/h")
    print()
    
    # Demonstrate polymorphism with accelerate method
    print("=" * 60)
    print("POLYMORPHISM DEMONSTRATION (Method Overriding)")
    print("=" * 60)
    print()
    
    print(car1.accelerate(20))
    print(car2.accelerate(30))
    print(bike1.accelerate(10))
    print(bike2.accelerate(15))
    print()
    
    # Vehicle Classification
    print("=" * 60)
    print("AI VEHICLE CLASSIFIER (Speed-based)")
    print("=" * 60)
    print()
    
    test_speeds = [25, 35, 45, 55, 70, 90, 120]
    
    print("Simple Classification:")
    for speed in test_speeds:
        predicted = classify_vehicle(speed)
        print(f"Speed: {speed:3d} km/h -> Predicted Type: {predicted}")
    print()
    
    print("Advanced Classification:")
    for speed in test_speeds:
        predicted = classify_vehicle_advanced(speed)
        print(f"Speed: {speed:3d} km/h -> Predicted: {predicted}")
    print()
    
    # Demonstrate class method
    print("=" * 60)
    print("CLASS METHOD DEMONSTRATION")
    print("=" * 60)
    print()
    print(f"Total vehicles created: {Vehicle.get_vehicle_count()}")
    print()
    
    # Demonstrate protected and private members
    print("=" * 60)
    print("PROTECTED AND PRIVATE MEMBERS")
    print("=" * 60)
    print()
    
    print("Protected members (accessible but conventionally internal):")
    print(f"  car1._brand = {car1._brand}")
    print(f"  car1._speed = {car1._speed}")
    print(f"  car1._type = {car1._type}")
    print()
    
    print("Private members (name-mangled, accessed through getters):")
    print(f"  car1.get_id() = {car1.get_id()}")
    print(f"  bike1.get_id() = {bike1.get_id()}")
    print()
    
    # Try to demonstrate that private members are name-mangled
    print("Private members are name-mangled:")
    try:
        print(f"  car1.__id would raise AttributeError")
        _ = car1.__id
    except AttributeError as e:
        print(f"  AttributeError: {e}")
    
    print(f"  But accessible via _Vehicle__id: {car1._Vehicle__id}")
    print()
    
    print("=" * 60)
    print("Demonstration Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
