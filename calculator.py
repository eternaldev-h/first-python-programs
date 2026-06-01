num1:int
num2:int
finalResult:int
operator:str
error:int
loopCounter:int
loopLogic:str

error=0
loopCounter=1

while loopCounter==1:
    num1=int(input("Enter number 1: "))
    operator=str(input("Enter operation: "))
    num2=int(input("Enter number 2: "))
    finalResult=0
    if operator=="/":
        finalResult=num1/num2
    elif operator=="*":
        finalResult=num1*num2
    elif operator=="+":
        finalResult=num1+num2
    elif operator=="-":
        finalResult=num1-num2
    else:
        error=error+1   #Code for error, debugged multiple times
    if error>0:
        print("Error, write a logical operation")
    else:       
        print(num1, operator, num2, "=", finalResult)
    loopLogic=str(input("Do you want to end the loop? Enter Y or N  "))
    if loopLogic=="Y" or "y":  
        loopCounter=0
    else:
        loopCounter=1    

#Can add a while loop to loop entire calculations. Can also add more operations like floor division and modulus
