# Simple class
class Simpleclass:
    def __init__(self,name):
        self.name = name 
       

        
# Create an instance and print the attribute
Namevar= Simpleclass('Tharunaditya')
print(Namevar)
print(Namevar.name)


# Less simple class
class pc:
    def __init__(self,processor,ram,memory):
        self.processor = processor
        self.ram = ram
        self.memory = memory 
        
    def w_p(self):
        return f"Processor : {self.processor}"
    def raam(self):
        return f"Ram : {self.ram}"
    def memo(self):
        return f"Memory : {self.memory}"



tharunpc=pc('i7','16gb','1tb')

# Instance method Example of an instance method
print(tharunpc.raam())


# Access class attribute from class and instance
pc('i3','8gb','512gb')
print(pc('i3','8gb','512gb').w_p())
print(pc('i3','8gb','512gb').raam())

print(tharunpc.w_p())