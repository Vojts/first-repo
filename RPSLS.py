# Rock Paper Scissors Lizard Spock
# This is a simple game of Rock Paper Scissors Lizard Spock

import random
end_check = False
player = 0
cpu = 0
emoji = ["✊", "✋", "✌️", "🦎", "🖖", "to resign 😔"]


while not end_check:

  #Menu block
  print("================================")
  print("Rock Paper Scissors Lizard Spock")
  print("================================")
  print("1) ✊")
  print("2) ✋")
  print("3) ✌️")
  print("4) 🦎")
  print("5) 🖖")
  print("6) Close 😔")
  player = int(input("Pick a number: "))
  cpu = random.randint(1,5)
  print("")

  #Emoji print
  if player in range(1, len(emoji)+1):
    print("You chose: " + emoji[player-1])
    print("CPU chose: " + emoji[cpu-1])
    if player == 6:
      break

  #Logic block
  if cpu == player:
    print("It's a tie!")
  elif player > 6:
    print("Wrong number! Try again.")

    #Rock wins
  elif cpu == 1 and player == 3:
    print("CPU won!")
  elif cpu == 1 and player == 4:
    print("CPU won!")

    #Paper wins
  elif cpu == 2 and player == 1:
    print("CPU won!")
  elif cpu == 2 and player == 5:
    print("CPU won!")

    #Scissors wins
  elif cpu == 3 and player == 2:
    print("CPU won!")
  elif cpu == 3 and player == 4:
    print("CPU won!")
  
      #Lizard wins
  elif cpu == 4 and player == 5:
    print("CPU won!")
  elif cpu == 4 and player == 2:
    print("CPU won!")

    #Spock wins
  elif cpu == 5 and player == 3:
    print("CPU won!")
  elif cpu == 5 and player == 1:
    print("CPU won!")
    
    #Player wins
  else:
    print("You won!")


  print("")