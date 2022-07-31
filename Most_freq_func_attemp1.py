def most_frequent():
 x=input("Please enter a string : ")
 print("string =",x)
 d=dict()
 for key in x:
     if key not in d:
         d[key]=1
     else:
        d[key]+=1
 for key in sorted(d , key=d.get ,  reverse=True):
    print(key , d[key])
most_frequent()