lines=["this is line 1\n","this is line 2\n","this is line 3\n","this is line 4\n"]
with open("C:/Users/hp/Desktop/text3.txt","w") as file1:
    for i in lines:

     file1.write(i)

#with open("C:/Users/hp/Desktop/text2.txt","a") as file2:
 #   file2.write("\nThis is line 3")




with open("C:/Users/hp/Desktop/text3.txt","r") as file2:
   for j in file2.readlines():
       print(j)
    #stuff=file2.readlines()
    #print(stuff)
   print(len(file2.readlines()))
