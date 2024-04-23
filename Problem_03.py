def order(): 
    stack=[] 
a=int(input("enter the number of item")) 
stack=[] 

for i in range(1,a+1):
    b=input("enter the order") 
    stack.append(b) 
    
             
for i in range(a):
            print("The following order have been prepared",stack[i]) 


for j in range(a):
            print("The following order have been despatched",stack[j]) 
