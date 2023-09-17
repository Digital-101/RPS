import random

userpts = 0        
pcpts=0

print("TO STOP THE GAME TYPE 'stop'")
while True:
    
    #Enumerated List type 
    choice = ["rock", "paper", "scissor"]
    
    #Randomize
    randomNum = random.randint(0,2)

    print("---rock---\n---paper---\n---scissor---")
    userchoice = str(input("Select choice: ")) 
    
    print("\n+++++++++++++++++++++")
    print("Your Choice: ", userchoice)
    print("PC Choice: ", choice[randomNum])
    print("+++++++++++++++++++++\n")
    
    #compare selection
    if userchoice == "rock" and choice[randomNum] == "paper" :
        print("PC Win")
        pcpts+=1
        print("Your Score: ", userpts)
        print("PC Score: ",pcpts)
        print("---------------------")
    
    elif userchoice == "paper" and choice[randomNum] == "scissor" :
        print("PC Win")
        pcpts+=1
        print("Your Score: ", userpts)
        print("PC Score: ",pcpts)
        print("---------------------")
    
    elif userchoice == "scissor" and choice[randomNum] == "rock" :
        print("PC Win")
        pcpts+=1   
        print("Your Score: ", userpts)
        print("PC Score: ",pcpts)
        print("---------------------")
    
    elif userchoice == choice[randomNum]:
        print("Its a Tie!")
        pcpts+=1  
        userpts+=1
        print("Your Score: ", userpts)
        print("PC Score: ",pcpts)
        print("---------------------")
    
    elif userchoice == "stop":
        print("Total points \nYou:",userpts,"\nPC:",pcpts)
        break
    
    #input validation
    elif userchoice != choice[0] and userchoice != choice[1] and userchoice != choice[2] :
        print("Invalid input :(")
        
    else:
        print("You Win")
        userpts+=1
        print("Your Points: ", userpts)
        print("PC Points: ", pcpts)

print("##############")
#Display Winner
if userpts > pcpts:
    print("---You won---")

elif pcpts > userpts:
    print("---PC Won---")
else:
     print("---Draw---")
        
