# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:22:34 2021


"""


n=int(input("Press of 1 for Addition, 2 for Multiplication, 3 for Substraction, 4 for Division: "))

if n==1:
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    sum=x+y
    print("The addition of",x,"and",y,"is", sum )


if n==2:
   a=int(input("Enter the first number: "))
   b=int(input("Enter the second number: "))
   multiply=a*b
   print("The multiplication of",a,"and",b,"is",multiply)
   
if n==3:
    z=int(input("Enter the first number: "))
    w=int(input("Enter the second number: "))
    sub=z-w
    print("The substraction of",z,"and",w,"is",sub)
    
    
if n==4:
   r=int(input("Enter the first number: "))
   s=int(input("Enter the second number: "))
   div=r/s
   print("The division of",r,"and",s,"is",div)
   
elif n>=5:
    print("Invalid Input")


    


    
          
