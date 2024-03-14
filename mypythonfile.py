#varibles
boy_name = "henok"
boy_age = "70"
boy_marks = "60.455"
male = "true"

print(boy_age)
print(boy_name)
print(male)
print(boy_marks)



u= y = z = 10
p, b, c = 30, 40, 70
r = 3
t, s, j = 3, 4, 5
a= int(2)

price =10
qaty =5
total = price*qaty
print("the total is:"+str(total)+"kenya shillings")

frstname="dan"
secndname="moko"
thrdname=frstname + " " + secndname
print("my third name is:", thrdname)
print(25//5)
print(5**6)

x=5
print(x)
x+=5 #x=x+5
print(x)
x-=4 #x=x-5
print(x)
x*=3 #x=x*3
print(x)
x//=2 #x=x/2
print(x)

#comparison ops
q=20
z=21
print(q==z)
#logical ops
age=50
nationality= "kenyan"

if nationality == "kenyan" and age>=35:
    print ( "can be preso")
else:
    print("cannot be preso")


location="ruiru"
location="juja"
location="keno"

if location =="ruiru" or "juja" or "kenol":
    print("can be governor")
else:
    print("cannot be governor")

pen=50.8
book="70"
total=pen+ float(book)
result="my total is:"+str(total)+" ksh"
print(result)

d=50
q=5
total==d%q
print(total)
if total==0:
    print("t is even")
else:
    print("t is odd")


  #loops----BREAK
x=1
while x<5:
    if x==3:
        break
    print(x)
    x+=1

r = 0
while r<=10:

    if r == 3:
       r+=1
       continue
    if r == 5:
       r+=1
       continue
    print("the ans is", r)
    r += 1



p=51
g=5
ans=p%g
print(ans)
if ans==0:
    print("p is even")
else:
    print("p is odd")


x=1
if x>3:
    print("x is greater than 3")
elif x==3:
     print("x is equal to 3")
else:
    print("x is less than 3")

""" 
country= input("enter the country:")
if country=="Rwanda":
    print("East African")
elif country=="Kenya":
    print("East African")
elif country=="Tanzania":
    print("East african")
elif country=="Congo":
    print("East African")
elif country=="Uganda":
    print("East African")
else:
    print("unknown country")

x=1
while x<=10:
    print("the no is",x )
    x += 1
else:
    print("the loop has ended here")
 """
x=1
while x<10:

    x+=2
    print(x)


