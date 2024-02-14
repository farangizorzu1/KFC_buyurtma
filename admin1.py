# # endi kiritga qiymatni uchirish
a_menyu = ["lavash", "hotdog", "burger", "pizza", "sandwich"]
a_dreenk = ["pepsi", "fanta", "cola"] 
a_price = [40, 45, 46, 89, 99, 90, 90, 9]
menu = a_menyu + a_dreenk 
s = []
k = [] 
d=0 
a=[] 
a1=[] 
q=[] 
total_price = 0 
n=1 
l=[] 
sum1=0 
sum=0 
sum2=0 
count=0 
m=0 
 
for i,items in  enumerate(menu, start=1):
    print(f"{i}.{items}")
while n!=0:
    n=input("NIma hohlaysiz?")
    if n.isdigit():
        n=int(n)
        if n==0:
           break
        else:
            if len(menu)>=n:
                s.append(menu[n-1])
                z=int(input("nechita olasiz"))
                total_price+=z*a_price[n-1]
                print(f"{z} ta {menu[n-1]}, {total_price}")
                k.append(z)
            else:
                print("BUNDAY QIYMAT MENYUDA YOQ")
    if n=="-":
        # print("uchirmoqchi bulgan elementizni sonnini kiriting")
        z=int(input("uchirmoqchi bulgan elementingizni kiriting"))
        menu.remove(menu[z-1])
        a_price.remove(a_price[z-1])
        print(menu)
        print("yangi menu")
        for i , items in enumerate(menu, start=1):
            print(f"{i}.{items}")
    print(a_price)
    # print(s)
print("Buyurtma")  
for i in range(len(s)):
    if s[i] not in a:
        qiymat=0
        for j in range(len(s)):
           if s[i]==s[j]:
              qiymat+=k[j]
        a.append(s[i])
        print(f"{qiymat} ta {s[i]}")
            # q.append(qiymat)
    
print(f"jami summa:{total_price}")
            
            
            
        
        
                
        
                
        
           


    
    
    