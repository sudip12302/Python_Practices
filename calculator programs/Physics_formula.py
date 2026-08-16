''' Take initial velocity, final velocity and time as input and calculate acceleration using
 formula a=(v-u)/t and distance using formula s=ut+1/2at^2'''
initial_velocity = float(input("Enter the initial velocity (u) in m/s: "))
final_velocity = float(input("Enter the final velocity (v) in m/s: "))
time = float(input("Enter the time (t) in s: "))
#calculating acceleration
acceleration = (final_velocity - initial_velocity) / time
print("The acceleration of the object is ",acceleration,"m/s^2")    
#calculating distance
distance = initial_velocity * time + 0.5 * acceleration * time**2   
print("The distance traveled by the object is ",distance,"m")

