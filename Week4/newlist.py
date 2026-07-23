#write a prgram to create a new list containing all the lements based on even positions from the original list
a = [43,23,21,56,78,90,12,34,67,89]
newlist = []

i = 0
while i < len(a):
    newlist.append(a[i])   # pick element at even index
    i += 2                 # jump to the next even index
       # print the new list after each addition

print(newlist)
