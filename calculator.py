num1:int
num2:int
finalResult:int
operator:str
error:int
num1=int(input("Enter number 1: "))
operator=str(input("Enter operation: "))
num2=int(input("Enter number 2: "))
finalResult=0
error=0
if operator=="/":
    finalResult=num1/num2
elif operator=="*":
    finalResult=num1*num2
elif operator=="+":
    finalResult=num1+num2
elif operator=="-":
    finalResult=num1-num2
else:
    error=error+1
if error>0:
    print("Error, write a logical operation")
else:       
    print(num1, operator, num2, "=", finalResult)


#Can add a while loop to loop entire calculations. Can also add more operations like floor division and modulus
