mass = float(input("Enter Mass in kg"))
height = float(input("Enter Height in M"))
time = float(input("Enter time in s"))
motor_power = float(input("Enter Motor Power in W"))
gravity = 9.81

force = mass * gravity
work_done = force * height
power_required = work_done / time

if motor_power >=  power_required:
                    print("motor has sufficient power")
else:
    print("motor has insuccifient power")
                    
               
