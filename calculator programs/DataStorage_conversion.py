''' To input in mb and convert it into gb and kb'''
size = float(input("Enter the data size in mb: "))

#convert into kb
kb = size*1024
print("The size in kb is ",kb,"Kb")

#convert into gb
gb = size/1024
print("THe size in gb is ",gb,"Gb") 