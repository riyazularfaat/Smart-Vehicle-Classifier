"""
Smart Vehicle Classifier - Vehicle Module
Demonstrates OOP concepts: Inheritance, Encapsulation, Method Overriding, 
Protected and Private Members
"""

# Module-level constants for classification
SPEED_THRESHOLD = 50  # km/h - threshold for simple classification
LOW_SPEED_THRESHOLD = 40  # km/h - threshold for low-speed vehicles
HIGH_SPEED_THRESHOLD = 60  # km/h - threshold for high-speed vehicles


class Vehicle:
    """Base class for all vehicles"""
    
    # Class variable to track vehicle count
    _vehicle_count = 0
    
    def __init__(self, brand, model, speed):
        """
        Initialize a vehicle
        
        Args:
            brand (str): Brand of the vehicle
            model (str): Model of the vehicle
            speed (float): Speed of the vehicle in km/h
        """
        # Private member (name mangling with __)
        Vehicle._vehicle_count += 1
        self.__id = Vehicle._vehicle_count
        
        # Protected members (indicated by single _)
        self._brand = brand
        self._model = model
        self._speed = speed
        self._type = "Generic Vehicle"
    
    # Getter methods (encapsulation)
    def get_id(self):
        """Get the unique ID of the vehicle"""
        return self.__id
    
    def get_brand(self):
        """Get the brand of the vehicle"""
        return self._brand
    
    def get_model(self):
        """Get the model of the vehicle"""
        return self._model
    
    def get_speed(self):
        """Get the speed of the vehicle"""
        return self._speed
    
    def get_type(self):
        """Get the type of the vehicle"""
        return self._type
    
    # Setter methods (encapsulation)
    def set_speed(self, speed):
        """Set the speed of the vehicle"""
        if speed >= 0:
            self._speed = speed
        else:
            raise ValueError("Speed cannot be negative")
    
    def display_info(self):
        """Display vehicle information - can be overridden by subclasses"""
        return f"Vehicle ID: {self.__id}\nType: {self._type}\nBrand: {self._brand}\nModel: {self._model}\nSpeed: {self._speed} km/h"
    
    def accelerate(self, increment):
        """Accelerate the vehicle - can be overridden by subclasses"""
        self._speed += increment
        return f"{self._type} accelerated to {self._speed} km/h"
    
    @classmethod
    def get_vehicle_count(cls):
        """Get total number of vehicles created"""
        return cls._vehicle_count


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, speed, num_doors=4):
        """
        Initialize a car
        
        Args:
            brand (str): Brand of the car
            model (str): Model of the car
            speed (float): Speed of the car in km/h
            num_doors (int): Number of doors
        """
        # Call parent constructor
        super().__init__(brand, model, speed)
        
        # Car-specific attributes
        self._type = "Car"
        self._num_doors = num_doors
    
    def get_num_doors(self):
        """Get the number of doors"""
        return self._num_doors
    
    # Method overriding
    def display_info(self):
        """Override to display car-specific information"""
        base_info = super().display_info()
        return f"{base_info}\nNumber of Doors: {self._num_doors}"
    
    def accelerate(self, increment):
        """Override to provide car-specific acceleration behavior"""
        self._speed += increment
        return f"Car {self._brand} {self._model} smoothly accelerated to {self._speed} km/h"


class Bike(Vehicle):
    """Bike class inheriting from Vehicle"""
    
    def __init__(self, brand, model, speed, bike_type="Mountain"):
        """
        Initialize a bike
        
        Args:
            brand (str): Brand of the bike
            model (str): Model of the bike
            speed (float): Speed of the bike in km/h
            bike_type (str): Type of bike (Mountain, Road, etc.)
        """
        # Call parent constructor
        super().__init__(brand, model, speed)
        
        # Bike-specific attributes
        self._type = "Bike"
        self._bike_type = bike_type
    
    def get_bike_type(self):
        """Get the bike type"""
        return self._bike_type
    
    # Method overriding
    def display_info(self):
        """Override to display bike-specific information"""
        base_info = super().display_info()
        return f"{base_info}\nBike Type: {self._bike_type}"
    
    def accelerate(self, increment):
        """Override to provide bike-specific acceleration behavior"""
        self._speed += increment
        return f"Bike {self._brand} {self._model} swiftly accelerated to {self._speed} km/h"


def classify_vehicle(speed):
    """
    Simple AI classifier that predicts vehicle type based on speed threshold
    
    Speed thresholds:
    - Speed < 50 km/h: Likely a Bike
    - Speed >= 50 km/h: Likely a Car
    
    Args:
        speed (float): Speed in km/h
        
    Returns:
        str: Predicted vehicle type
    """
    if speed < SPEED_THRESHOLD:
        return "Bike"
    else:
        return "Car"


def classify_vehicle_advanced(speed, num_wheels=None):
    """
    Advanced classifier with multiple features
    
    Args:
        speed (float): Speed in km/h
        num_wheels (int, optional): Number of wheels
        
    Returns:
        str: Predicted vehicle type with confidence
    """
    confidence = "Medium"
    
    # Primary classification based on speed
    if speed < LOW_SPEED_THRESHOLD:
        predicted_type = "Bike"
        confidence = "High"
    elif speed < HIGH_SPEED_THRESHOLD:
        predicted_type = "Bike" if num_wheels == 2 else "Car"
        confidence = "Medium"
    else:
        predicted_type = "Car"
        confidence = "High"
    
    return f"{predicted_type} (Confidence: {confidence})"
