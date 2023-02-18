num = int(input("Enter the number "))

for i in range(num):
    for j in range(num-i):    # ***   if input = 3
            print("*",end="") # **
    print()                   # *


'''for i in range(0 , a ):
    print("*",i=i+1);
    for i in range(0 , a ):
       print("*",i=1-i);'''
"""for i in range(num):
    i=i+1
    for j in range(num):
            j=j-1
            print("*",end="")
    print()
    
    for i in range(num):
    i=i+1
    for j in range(i):
            j=j-1
            print("*",end="")
    print()
    
   
    
for i in range(num):
    for j in range(num-i):
            print("*",end="")
    print()  
    
row= int(input())
row= int(input())
for i in range(row):
        for j in range(column):
            print("*",end="") 
        print()
    
for i in range(num):
        for j in range(num-i):
            print(" ",end="")   #   *
        for k in range(i):      #  **
             print("*",end="")  # ***    
        for j in range(num-i):
            print(" ",end="")   #   *
        for k in range(i):      
             print("*",end="")         
        print() 

count=1
for i in range(num+1):
        for j in range(i):
              print(count,end=" ")
              count=count+1        
        print() 
"""
