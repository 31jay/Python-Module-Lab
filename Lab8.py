# Q1.
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age 

dog1=dog('Tom','10')
print(dog1.name,dog1.age)       

#Q2.
dog1=dog('Bruno',2)
dog2=dog('Sher',3)
print(f'Dog1={dog1.name, dog1.age}')
print(f'Dog2={dog2.name, dog2.age}')

#Q3.
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model    
        self.year=year  

    def describe_car(self):
        print(f'Model={self.model}, Make={self.make}, year={self.year}')

car1=car('Mustang','M2072',1990)
car1.describe_car()

#Q4. 
class car:
    def __init__(self,model,make,year):
        self.model=model  
        self.make=make
        self.year=year  
        self.fuelLevel=100

    def checkFuelLevel(self):
        print('Fuel Level=',self.fuelLevel)

car1=car('Mustang','M2072',1990)
car1.checkFuelLevel()

#Q5. 
class Car:
    def __init__(self,model,make,year):
        self.model=model  
        self.make=make
        self.year=year  
        self.fuelLevel=100    

    def updateFuelLevel(self,level):
        self.fuelLevel=level

    def checkFuelLevel(self):
        print('Fuel Level=',self.fuelLevel)

    def describe_car(self):
        print(f'Model={self.model}, Make={self.make}, year={self.year}')

car1=car('Mustang','M2072',1990)
car1.updateFuelLevel(50)
car1.checkFuelLevel()

#Q6, Q7, Q8, Q9
class ElectricalCar(Car):
    def __init__(self, model,make,year,battery_size):
        super().__init__(model,make,year)
        self.battery_size=battery_size

    def car_range(self):
        # print(f'Range of Car battery= {self.battery_size} is', self.battery_size*50)
        return self.battery_size*10

    def describe_car(self):
        print(f'Model={self.model}, Make={self.make}, year={self.year}, batterysize={self.battery_size}, range={self.car_range()}km')

car1=ElectricalCar('Mustang','M2072',1995,100)
car1.describe_car()

#Q10.
from car import Car

myCar=Car('ABC','ABC23',2000)
myCar.describe_car()

