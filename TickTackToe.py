
def board(user,key,li):
   if user == 0:
       li[key-1]="O"
   if user == 1:
       li[key-1]="X"
   for i in range(0,7,3):
      print(" ",li[i]," "+"|"+" ",li[i+1]," "+"|"+" ",li[i+2]," ")
   #print(" _    _    ")   
      print(" ","_"," "+" "+" ","_" +" " ,"_"," " )
  
   #winner(user, li)
    
   return li
   

user1 =0 
user2 =1
key = 0
li =[1,2,3,4,5,6,7,8,9,10]
print("welcome to tik tack toe")
board(user1,key,li)
for i in range (1,10):
    if i%2==0:
        print("\n user2 turm: choose any number")
        key=int(input())
        li=board(user2,key,li)
    else:
       print("\n user1 turm: choose any number")
       key=int(input())
       li=board(user1,key,li)