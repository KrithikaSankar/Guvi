num1=int(input("Enter first number: "))
 
num2=int(input("Enter second number: "))
if num1 > num2:
 
     smaller = num2
 
else:
 
    smaller = num1
 
    for i in range(1, smaller+1):
 
         if((num1 % i == 0) and (num2 % i == 0)):
 
              hcf = i
print "The H.C.F. of", x,"and", y,"is",hcf
