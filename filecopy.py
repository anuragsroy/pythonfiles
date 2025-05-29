lines=[]
with open("C:/Users/hp/Desktop/text3.txt","r") as file1:
    for i in file1.readlines():
        lines.append(i)


with open("C:/Users/hp/Desktop/text4.txt","w") as file2:
    for j in lines:
        file2.write(j)




