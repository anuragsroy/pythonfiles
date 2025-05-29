#finding the even numbers of a list using for loop
list=[]
even=[]
limit=input("Enter the number of elements in the list: ")
for i in range(0,int(limit)):
    element=input("Enter the element")
    list.append(element)

print("The list is:", list)

for i in range(0,int(limit)):
    if int(list[i])%2==0:
        even.append(list[i])
    else:
        continue
print("even numbers in the list are:", even)