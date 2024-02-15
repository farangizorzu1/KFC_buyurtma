url=input()
i=0
point_count=0
count_point1=0
count_point2=0
if url[:8]=="https://":
  if url[0]!="." and url[-1]!="." and url[0]!="/" and url[-1]!="/":
    while i<len(url):
      if url[i]==".":
        if url[i-1]!="." and url[i+1]!="." and url[i-1]!="/" and url[i+1]!="/":
           point_count+=1
      i+=1
    if point_count==3 or point_count==2 or point_count==1:
      print("url 1")
    else:
      print(False)
  else:
    print(False)
else:
   if url[0]!="h" and url[1]!="t" and url[2]!="t" and url[3]!="p" and url[4]!="s" and url[5]!=":" and url[6]!="/" and url[7]!="/":
     if url[-1]!="." and url[0]!="." and url[-1]!="/" and url[0]!="/":
         while i<len(url):
              if url[i]==".":
                  if url[i-1]!="." and url[i+1]!="." and url[i-1]!="/" and url[i+1]!="/":
                      count_point1+=1
              i+=1
         if count_point1==3 or count_point1==2 or count_point1==1:
              print("url 2")
         else:
            print(False)
     else:
        print(False)
   else:
       if url[0]=="h" and url[1]=="t" and url[2]=="t" and url[3]=="p" and url[4]==":" and url[5]=="/" and url[6]=="/":
         if url[-1]!="." and url[0]!="." and url[-1]!="/" and url[0]!="/":
            while 7<len(url):
                if url[i]==".":
                  if url[i-1]!="." and url[i+1]!="." and url[i-1]!="/" and url[i+1]!="/":
                      count_point2+=1
                i+=1
            if count_point2==3 or count_point2==2 or count_point2==1:
                 print("url3")
            else:
                   print(False)
         else:
            print(False)
       else:
              print(False)

