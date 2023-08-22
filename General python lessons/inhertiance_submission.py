#general vehicle information
class vehicle:
    seats = 4
    color = "red"
    price = 600,000.00
    power = "100 hp"
    controller = "steering wheel"
    fuel = "diesel"
# this class inherits two additional items not typical of other vehicles
class plane(vehicle):
    wings = 4
    engines = 1
    
    
# this one has capabilities other vehicles don't have
class submarine(vehicle):
    pressure_capabilities = " 9,000 ft' "
    power_line = "60 ft"
    

sub = submarine()
fly = plane()
veh = vehicle()

print (sub.power_line)
print (fly.engines)
print (veh.color)


print (sub.seats)
print (fly.price)
print (veh.fuel)
