#EXCEPTION HANDLIMG
number1= 20
number2= 0
try:
    y=number1/number2
    print(y)
except:
    print("Error")

number3=20
number4=0
try:
    x=number3/number4
except Exception as r:
    print("not ok:",r)
else:
    print(x)
    print("its ok")


