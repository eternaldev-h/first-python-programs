count: int
goodResponse:int
badResponse:int
neutralResponse:int
response:str
count=0
goodResponse=0
badResponse=0
neutralResponse=0
while count==0:
    response=str(input("How are you feeling?"))
    if response=="good":
        if goodResponse<3:
            print("Good to hear, hope your feel the same throughout the day.")
            goodResponse=goodResponse+1
        else:
            print("You keep saying that... Are you okay?")    
    elif response=="bad":
        if badResponse<3:
            print("No worries, your day will get better, good luck!")
            badResponse=badResponse+1
        else:
            print("Your day seriously can't be that bad if you can spam things here...")    
    elif response=="exit":
        count=count+1
    else:
        if neutralResponse<3:
            print("Thanks for visiting, have a good day!")
            neutralResponse=neutralResponse+1
        else:
            print("Stop typing random things here and write something meaningful!")    
print("The loop's over")
