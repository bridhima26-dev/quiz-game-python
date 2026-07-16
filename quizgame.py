import random
import ques_python
import ques_maths 
import ques_harry

#Welcome screen
print("--------------QUIZ GAME--------------")

print("Welcome to the quiz!")

#Category selection
print("the categories you can take quiz in:\n1.Python\n2.Math\n3.Harry Potter Series")

while True:
    
    while True:
        x = int(input("Enter the serial number of any one of the categories:"))
        match x: 
            case 1: 
                quiz = ques_python.python_ques
                break
            case 2: 
                quiz = ques_maths.math_ques
                break
            case 3: 
                quiz = ques_harry.harry_ques 
                break
            case _: 
                print("Invalid serial number!try again.") 

            
    #Randomise question order            
    items = list(quiz)

    random.shuffle(items)

    count = 0 

    #Quiz questions
    for i in items:
         print(i) 
         answer = input("Enter answer:").lower()
         if answer == quiz[i]: 
            print("Correct") 
            count = count + 1 
         else: 
            print(f"Wrong answer! The correct answer is {quiz[i]}") 
            
    #Score calculation and feedback       
    score = count/len(quiz)*100 

    print(f"Your score is {score:.2f}%")
    
    if score>=80: 
        print("Well done!") 
    elif score>=60:
        print("Good!") 
    elif score>=40:
        print("Not bad, but you can do better") 
    else: 
        print("Needs more practice")
    
    #Replay option
    a = input("Do you want to play again?(y/n):").lower()

    if a=="n":
        break

 
