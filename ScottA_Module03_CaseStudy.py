#ScottA_Module03_CaseStudy
#Created by Angela Scott for SDEV 220
#27 JUL 2025
#This is a vehicle report tool that allows the user to enter a type of vehicle
#and information about an automobile. (year, make, model, doors, and roof type)
#The tool will store and report back the information.

# Superclass for Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display(self):
        print(f"Vehicle Type: {self.vehicle_type}")

# Subclass for Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initialize superclass attributes
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Display the information and call the display method
    def display(self):
        super().display()
        print("----------",vehicle_type,"Information Report ----------")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Type of Roof: {self.roof}")
        print("----------End of Report----------")

# Collect user input for superclass and subclass
vehicle_type = input("Enter the type of vehicle: ")
year = int(input("Enter the year of manufacture: "))
make = input("Enter the make of your automobile:")
model = input("What is the model of your automobile:")
doors = int(input("How many doors does your automobile have: (enter 2 or 4):"))
if doors == 2:
    print("You have entered 2 doors.")
elif doors == 4:
    print("You have entered 4 doors.")
else:
    print("This is not a valid input, but will appear on your report.")       
roof = input("What type of roof does your automobile have: (solid or sunroof):")

# Create an instance of the subclass
automobile = Automobile(vehicle_type, year, make, model, doors, roof)

# Display the data
automobile.display()
