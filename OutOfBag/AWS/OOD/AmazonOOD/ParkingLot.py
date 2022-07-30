# https://github.com/nikuamit/ParkingLot/blob/f9359d453eaefacceb95ae13c717c679877da481/solution/parking_lot.py#L5
from enum import Enum
from abc import ABC, abstractclassmethod

class VehicleType(Enum):
    small = 1
    medium = 2
    large = 3
# print(VechileType.large)
# print(repr(VechileType.large))
# print(VechileType.large.name)

class Vehicle:
    def __init__(self, plate, companyName, vehicleType):
        self.plate = plate
        self.companyName = companyName
        self.vehicleType = vehicleType

    def getType(self):
        return self.vehicleType
    
    def __eq__(self, other):
        if other is None:
            return False
        if self.plate != other.plate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.vehicleType != other.vehicleType:
            return False
        return True
    
class Motobike(Vehicle):
    def __init__(self, name, plate, vehicleType = VehicleType.small):
        super().__init__(name, plate, vehicleType)
        
class Car(Vehicle):
    def __init__(self, name, plate, vehicleType = VehicleType.medium):
        super().__init__(name, plate, vehicleType)
    
class Bus(Vehicle):
    def __init__(self, name, plate, vehicleType = VehicleType.large):
        super().__init__(name, plate, vehicleType)


class ParkingSpotType(Enum):
    small = 1
    medium = 2
    large = 3
    Handicapped = 4

class ParkingSpot:
    def __init__(self, lane, spotNum, parkingType):
        self.lane = lane
        self.vehical = None
        self.parkingType = parkingType
        self.spotNum = spotNum
        
    def isAvailible(self):
        return self.vehical == None
    
    def park(self, vehical):
        if vehical.vehicleType == self.parkingType:
            self.vehical = vehical
            return True
        else:
            return False
    
    def removeVehicle(self):
        self.vehical = None
    
    def getVehicle(self):
        return self.vehical

class Level:
    def __init__(self, floorNumber, num_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = int(num_of_slots / self.spots_per_lane)
        # self.parkingSlots = set()
        self.availableSpots = []

        for lane in range(self.lanes):
            for i in range(self.spots_per_lane):
                import random 
                self.availableSpots.append(ParkingSpot(lane, i, random.choice(list(VehicleType))))
                                 
    def park(self, vehical):
        for slot in self.availableSpots:
            if slot.park(vehical):
                return True
        else:
            return False
    
    def remove(self, vehicle):
        for spot in self.availableSpots:
            if spot.getVehicle() == vehicle:
                spot.removeVehicle()
                return True
    
    def companyParked(self, companyName):
        all_vehicles = []
        for slot in self.availableSpots:
            vehicle = slot.getVehicle()
            if (vehicle is not None) and (vehicle.companyName == companyName):
                all_vehicles.append(vehicle)
                #print(all_vehicles)
        return all_vehicles
    
    
class ParkingLot:
    def __init__(self, no_of_floor, no_of_slot):
        self.levels = []
        for i in range(no_of_floor):
            self.levels.append(Level(i, no_of_slot))
        
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    # This operation exits a vehicle 'C' in a level 'm'.
    def leaveOperation(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True
        return False
    
    # This operation allows the user to view the list of vehicles parked for a particular company.
    def companyParked(self, companyName):
        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.companyParked(companyName))
        return all_vehicles
    

### testing 

import unittest
class TestParkingLot(unittest.TestCase):
    
    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car(10, "Amazon"))
        res3 = parkingLotObj.parkVehicle(Motobike(20, "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus(30, "Microsoft"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)


    def test_leave_operation(self):
        parkingLotObj = ParkingLot(6, 30)
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        #self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        self.assertTrue(parkingLotObj.leaveOperation(Car(20, "Google")))
        self.assertEqual(parkingLotObj.leaveOperation(Car(20, "Google")), None)


    def test_companyParked(self):
        parkingLotObj = ParkingLot(6, 30)
        # res1 = parkingLotObj.parkVehicle(Car(20, "Google"))
        # res2 = parkingLotObj.companyParked("Google")
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(20, "Google")])
        #self.assertEqual(parkingLotObj.companyParked("Google"), Car(10, "Google"))
        print(parkingLotObj.companyParked("Google"))

        
    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        # Atleast 1 parking spot for car.
        # First park a car, it should return True.
        self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))
        # Get the list of cars, it should give one car we parked.
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(10, "Google")])
        # Remove that car successfully.
        self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        # Now the list of cars should be empty.
        self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()