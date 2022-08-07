list = [] 
print(list)

list.append(1)
list.append(2)
list.append(4)

print(list)

for i in range(1,4):
    list.append(4)
print(list)


list2 = ['for','Geeks']
list.append(list2)
print(list)    


list = [1,2,3,4,5,'Geek','python']
list.reverse()
print(list)

 
# Creating a List
list4 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(list4)
  
# Removing elements from List
# using Remove() method
list4.remove(5)
list4.remove(6)
print("\nList after Removal of two elements: ")
print(list4)



# Creating a List
List5 = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List5.remove(i)
print("\nList after Removing a range of elements: ")
print(List5)

