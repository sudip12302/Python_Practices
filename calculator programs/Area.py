''' Calculate area of different shapes '''
#giving value of pi
pi=3.14
#Area of circle
radius=float(input("Enter the radius of circle: "))
area_circle= pi*radius**2
print("The area of circle is",area_circle)

#Area of rectangle
length=float(input("Enter the length of rectangle: "))
width=float(input("Enter the width of rectangle: "))
area_rectangle=length*width
print("The area of rectangle is",area_rectangle)

#Total area of circle and rectangle
total_area=area_circle+area_rectangle
print("The total area of circle and rectangle is",total_area)
