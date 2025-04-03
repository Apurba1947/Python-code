print("Apurba Mallick.", "My age is 20")
print(23+63)
name ="Apurba"
age =20
price =25.99
print("my name is :",name)
print("my age is:",age)
print("price is :", price)
print(type(name))
print(type(age))
print(type(price))
old=False
old=True
a=None
print(type(old))
print(type(a))
a=24
b=34
sum=a+b
print(sum)
#string & number values can operator together with *
A,B=2,34
Txt="@"
print(2*Txt*3)
# string & string can operate with +
A,B='2',3
Txt="@"
print((A+Txt)*B)
# numeric values can operate with all arithmetic operators
A,B=2,3 
c=4
print(A+B*c)
# Arithmetic expression with Integer and  float will result in float
A,B=10,5.0 
c=A*B
print(c)
# Result of division operator with two integers will be float
A,B=1,2
c=A/B
print(c)
# Integers division with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C,A/B)
#floor gives colsest integer , which is lesser than or equal to the float value result of (A//B) is same as floor(A/B)
A,B=12,5
C=A//B
print(C)

A,B=-12,5
C=A//B
print(C)

A,B=12,-5
C=A//B
print(C)
# reminder is negative when demoinator is negative(This symbol we called:-(%)modulo)
A,B=-5,2
C=A%B
print(C)

A,B=5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)
