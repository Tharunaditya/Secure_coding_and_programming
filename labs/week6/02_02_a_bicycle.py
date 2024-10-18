"""
create a simple bicylce class
"""
class Simplebicycle:
    def __init__(self,numtyres,tyretype,model,color,numgears,brakes,currentspeed):
        self.numtyres =numtyres
        self.tyretype =tyretype
        self.model = model
        self.color = color
        self.numgears = numgears
        self.brakes = brakes
        self.currentspeed = currentspeed
    def information(self):
        info = f"Model: {self.model}, Num of Tyres: {self.numtyres},Tyre type: {self.tyretype},Color: {self.color}, \n numgears: {self.numgears}, Brakes: {self.brakes}, Current speed : {self.currentspeed}"
        return info
    def jstbrake(self):
        self.currentspeed = 0
        print("Bicycle Stopped due to breaks applied . Current speed:",self.currentspeed)
    def jstpedal(self,acceleration):
        self.acceleration = acceleration
        self.currentspeed = self.currentspeed + acceleration
        print(f"Oh great you are moving with speed : {self.currentspeed}")
    
# # Attributes
    # number of tires
# type of of tires (road vs mountain bike)
# model
# color
# number of speeds
# brakes (front or back or both)
# current speed.

# # Methods
# brake
# pedal faster (should affect speed)
# """

My_bicycle = Simplebicycle(numtyres=2,tyretype='tubless',model='bmx',color='black',numgears=4,brakes="both",currentspeed=20)
print(My_bicycle.information())
speedincrement= 20
My_bicycle.jstpedal(speedincrement)
My_bicycle.jstbrake()