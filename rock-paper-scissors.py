import random


count = 0
compScore = 0

print('Want to play Rock, Paper, Scissors?')
print('')
print('Best out of 5!!')
print('')
print('Can You Beat the computer?')
print('')

while count < 3 and compScore < 3:
    while count < 3 and compScore < 3:
        compStorage = ['Rock','Paper','Scissors']    
    #    Sto = ['paper', 'scissors', 'rock']
        i = random.randint(0, 2)

        x = input('Rock,Paper or Scissors?: ')

        if x == "":
            break
        

        
        if ((x == "Rock" or x == "rock" )and (compStorage[i] == 'Rock' and i == 0)):
            print(i)
            print(compStorage[i])
            print('You Tied')
            print(compStorage[i])
            print('Computer Pick: ' + compStorage[i])
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "Rock" or x == "rock" and compStorage[i] == 'Paper'):
            print('You Lost')
            print('Computer Pick: ' + compStorage[i])
            compScore = compScore + 1
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "Rock" or x == "rock" and compStorage[i] == 'Scissors'):
            print('You Won')
            print('Computer Pick:' + compStorage[i])
            compScore = compScore
            count = count + 1
            print('Your Score:' + str(count))
            print('Hi')
            print('Computer Score:' + str(compScore))
            
        elif (x == "Paper" or x == "paper" and compStorage[i] == 'Rock'):
            print('You Won!')
            print('Computer Pick:' + compStorage[i])
            count = count + 1
            
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "Paper" or x == "paper" and compStorage[i] == 'Paper'):
            print('You Tied')
            print('Computer Pick:' + compStorage[i])
            print('Your Score:' +  str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "Paper" or x == "paper" and compStorage[i] == 'Scissors'):
            print('You Lost')
            print('Computer Pick:' + compStorage[i])
            compScore = compScore + 1
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))

        elif (x == "Scissors" or x == "scissors" and compStorage[i] == 'Rock'):
            print('You Lost')
            print('Computer Pick:' + compStorage[i])
            compScore = compScore + 1
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "Scissors" or x == "scissors" and compStorage[i] == 'Paper'):
            print('You Won!')
            print('Computer Pick:' + compStorage[i])
            count = count + 1
            print('Your Score:' +  str(count))
            print('Computer Score:' + str(compScore))
            
        elif (x == "scissors" or x == "Scissors" and compStorage[i] == 'Scissors'):
            print('You Tied')
            print('Computer Pick:' + compStorage[i])
            compScore = compScore
            print('Your Score:' + str(count))
            print('Computer Score:' + str(compScore))
        print("")




    if count == 3:
        print("Thanks For Playing! You Won!")
    else:   
        print("Thanks For Playing! You nearly won!")
        y = input('Do you want to play again? ')
        if y == 'yes' or y == 'Yes':
            count = 0
            compScore = 0
            print('Ok!!')
            print('')
        elif y == 'no' or y == 'No':
          print('Ok!')
          print('Have a nice day!')
          break
          
          
          
z = int(input('How good on a scale of 1 to 5, would you rate this game? '))
print('')
if z == 5:
  print('Awesome!')
elif z == 4:
  print('Thanks for your feedback!')
elif z == 3:
  print('Okay have a nice day!')
elif z == 2:
  print('I hope you enjoy it next time!')
elif z == 1:
  print('Okay!')
    
