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
