# Smart Vehicle Classifier

An AI-based vehicle classifier demonstrating Object-Oriented Programming (OOP) concepts in Python.

## Overview

This project simulates a simple AI-based vehicle classifier using Object-Oriented Programming principles. It demonstrates:

- **Inheritance**: Car and Bike classes inherit from a base Vehicle class
- **Protected Members**: Using single underscore prefix (e.g., `_speed`, `_brand`)
- **Private Members**: Using double underscore prefix for name mangling (e.g., `__id`)
- **Method Overriding**: Subclasses override base class methods to provide specific behavior
- **Encapsulation**: Using getter and setter methods to control access to attributes
- **Polymorphism**: Same method names with different behaviors in different classes

The program manages two types of vehicles: **Car** and **Bike**, each inheriting from the base `Vehicle` class. A simple classifier method predicts the type of vehicle based on speed thresholds.

## Features

### OOP Concepts Demonstrated

1. **Inheritance**
   - Base class `Vehicle` provides common functionality
   - `Car` and `Bike` classes inherit from `Vehicle`
   - Reuse of code through inheritance

2. **Encapsulation**
   - Private member: `__id` (name-mangled for privacy)
   - Protected members: `_brand`, `_model`, `_speed`, `_type`
   - Getter methods: `get_id()`, `get_brand()`, `get_speed()`, etc.
   - Setter methods: `set_speed()` with validation

3. **Method Overriding**
   - `display_info()` - overridden in Car and Bike classes
   - `accelerate()` - overridden with vehicle-specific behavior

4. **Polymorphism**
   - Same method interface, different implementations
   - Runtime method resolution based on object type

### Vehicle Classification

- **Simple Classifier**: Predicts vehicle type based on speed threshold (50 km/h)
  - Speed < 50 km/h → Bike
  - Speed ≥ 50 km/h → Car

- **Advanced Classifier**: Uses multiple features and confidence levels

## Installation

No external dependencies required. Only Python 3.x is needed.

```bash
git clone https://github.com/riyazularfaat/Smart-Vehicle-Classifier.git
cd Smart-Vehicle-Classifier
```

## Usage

Run the main demonstration:

```bash
python3 main.py
```

### Example Output

```
============================================================
Smart Vehicle Classifier - OOP Demonstration
============================================================

Creating Car instances...

Creating Bike instances...

============================================================
VEHICLE INFORMATION (Method Overriding Demonstration)
============================================================

Car 1:
Vehicle ID: 1
Type: Car
Brand: Toyota
Model: Camry
Speed: 80 km/h
Number of Doors: 4
...
```

## Code Structure

```
Smart-Vehicle-Classifier/
├── vehicle.py          # Core vehicle classes and classifier functions
├── main.py             # Demonstration script
├── README.md           # This file
└── LICENSE             # License file
```

### Class Hierarchy

```
Vehicle (Base Class)
├── Car (Inherits from Vehicle)
└── Bike (Inherits from Vehicle)
```

## Class Documentation

### Vehicle (Base Class)

**Attributes:**
- `__id`: Private member - unique vehicle ID
- `_brand`: Protected member - vehicle brand
- `_model`: Protected member - vehicle model
- `_speed`: Protected member - vehicle speed in km/h
- `_type`: Protected member - vehicle type

**Methods:**
- `get_id()`: Returns unique vehicle ID
- `get_brand()`: Returns vehicle brand
- `get_model()`: Returns vehicle model
- `get_speed()`: Returns vehicle speed
- `get_type()`: Returns vehicle type
- `set_speed(speed)`: Sets vehicle speed with validation
- `display_info()`: Displays vehicle information
- `accelerate(increment)`: Increases vehicle speed
- `get_vehicle_count()`: Class method returning total vehicles created

### Car (Inherits from Vehicle)

**Additional Attributes:**
- `_num_doors`: Number of doors

**Overridden Methods:**
- `display_info()`: Displays car-specific information
- `accelerate(increment)`: Car-specific acceleration behavior

### Bike (Inherits from Vehicle)

**Additional Attributes:**
- `_bike_type`: Type of bike (Mountain, Road, etc.)

**Overridden Methods:**
- `display_info()`: Displays bike-specific information
- `accelerate(increment)`: Bike-specific acceleration behavior

## Classification Functions

### classify_vehicle(speed)

Simple classifier based on speed threshold.

**Parameters:**
- `speed` (float): Speed in km/h

**Returns:**
- `str`: "Car" or "Bike"

**Logic:**
- Speed < 50 km/h → Bike
- Speed ≥ 50 km/h → Car

### classify_vehicle_advanced(speed, num_wheels=None)

Advanced classifier with confidence levels.

**Parameters:**
- `speed` (float): Speed in km/h
- `num_wheels` (int, optional): Number of wheels

**Returns:**
- `str`: Predicted type with confidence level

## Example Usage in Code

```python
from vehicle import Vehicle, Car, Bike, classify_vehicle

# Create instances
car = Car("Toyota", "Camry", 80, num_doors=4)
bike = Bike("Giant", "TCR", 35, bike_type="Road")

# Use methods (polymorphism)
print(car.display_info())
print(bike.display_info())

# Encapsulation - using getters
print(f"Car speed: {car.get_speed()} km/h")

# Encapsulation - using setters
bike.set_speed(45)

# Method overriding
print(car.accelerate(20))  # Car-specific message
print(bike.accelerate(10))  # Bike-specific message

# Classification
predicted_type = classify_vehicle(35)  # Returns "Bike"
```

## Learning Objectives

This project helps understand:

1. How inheritance promotes code reuse
2. How encapsulation protects data integrity
3. How method overriding enables polymorphism
4. The difference between protected and private members in Python
5. How to design class hierarchies
6. Practical application of OOP in AI/ML contexts

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created as an educational demonstration of Object-Oriented Programming concepts in Python.