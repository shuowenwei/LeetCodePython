"""
https://www.youtube.com/watch?v=b7riKazRJkU&t=2939s

Amazon Locker Problem

To monoitor are process of how to put the package into a right locker. And one locker for one package. Your 
package and locker have different size, you need to make sure the locker size > package. 

Requirements:
1. The delivery guy should be able to find an "optimal" locker for a package/packages.
2. System should send code to the user
3. Users should be able to use a code to open a locker and pick up a package
4. Assign locker based on user location
5. Assume there is always a locker

"""
from enum import Enum
class Size(Enum):
    Small, Medium, Large = 1, 2, 3

class Status(Enum):
    Deliver, Transit, Not_picked, Picked = 1, 2, 3, 4
    
class Locker:
    def __init__(self, size, id):
        self.size = size
        self.id = id 
        self.isAvailable = True
        self.package = None
        
    def getSize(self):
        pass 
    
    def isAvailable(self):
        return self.isAvailable

    def addPackage(self, package: Package):
        self.isAvailable = False
        self.package = package
        
    def removePackage(self):
        self.isAvailable = True
        # self.package = None
        pass 
    
class Package:
    def __init__(self, id, packageSize, User):
        self.id = id 
        self.packageSize = packageSize
        self.user = User 
        self.status = Status.Transit
    
    def Assigned():
        pass 

class Code:
    def __init__(self):
        self.code = None 
        self.expired = None
    pass

class User:
    pass 

class DeliveryPerson:
    def __init__(self, lockerService):
        self.lockerService = lockerService 
        pass 

    def executeDelivery(self, packages):
        while packages:
            lockerSys = self.lockerService.getLockerSys(package)
            lockerSys.addPackage(package)
        
    
class LockerSystem:
    def __init__(self, id, locationId):
        self.smallLockers = [] # generate a list of small lockers
        self.mediumLockers = [] # generate a list of medium lockers 
        self.largeLockers = [] # generate a list of large lockers 
        self.assignLockerMap = {}
        self.lockerMap = {}
    
    def __code():
        pass 
    
    
    def __findLocker(package):
        if package.size == Size.small and True:
            for locker in self.smallLockers + self.mediumLockers + self.largeLockers:
                if locker.isAvailable:
                    locker.isAvailable = False
                    return locker
            # for locker in self.mediumLockers:
            #     if locker.isAvailable:
            #         locker.isAvailable = False
            #         return locker
            # for locker in self.largeLockers:
            #     if locker.isAvailable:
            #         locker.isAvailable = False
            #         return locker
                    
        # same thing for medium and large 
        return None    
        pass
    
    def pickUp(lockerCode):
        if lockerCode not in self.assignLockerMap:
            return 'Exception'
        codeObject = self.assignLockerMap[lockercode][0]
        if not codeObject.expired:
            locker = self.assignLockerMap[lockercode][1]
            package = locker.removePackage()
            del self.assignLockerMap[lockercode]
            return package
        # find locker 
        # open locker 
        # if code expire then return error, locker.isAvailable = False 
        pass
    
    def addPackage(self, package):
        locker = __findLocker(package)
        
        if not locker:
            return "Return package"
        
        locker.addPackage(package)
        codeObject = __code()
        self.assignLockerMap[codeObject.code] = [codeObject, locker]
        user = package.user
        
        notifyUser(code, user)
        # finding the locker 
        # gen the code and add to the locker 
        # notify user 
        # full return back to delivery 