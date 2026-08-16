# Input
distance1 = float(input("Enter distance of section 1 in km: "))
time1 = float(input("Enter time of section 1 in hours: "))

distance2 = float(input("Enter distance of section 2 in km: "))
time2 = float(input("Enter time of section 2 in hours: "))

# Speed of each section
speed1 = distance1 / time1
print("\n Speed of Section 1 is ", speed1, "km/hr")
speed2 = distance2 / time2
print("\n Speed of Section 2 is", speed2, "km/hr")

# Total distance and total time
total_distance = distance1 + distance2
print("\n Total distance is ",total_distance,"km")
total_time = time1 + time2
print("\n Total time taken is ",total_time,"hr")
# Average speed
average_speed = total_distance / total_time
print("\n  Average Speed:", average_speed, "km/hr")