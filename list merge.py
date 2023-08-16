list1=[]
list2=[]

num1 = int(input('enter list1 numbers'))
for i in range(1,num1+1):
      p=int(input("enter numbers"))
      list1.append(p)
      
num2 = int(input("enter list2 numbers"))
for i in range(1,num2+1):
      g = int(input("enter numbers"))
      list2.append(g)
    
list3 =list1+list2
print(list3)