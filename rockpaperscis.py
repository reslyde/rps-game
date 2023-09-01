
import random
p2_list = ["R", "P", "S"]
pc_score = 0
score = 0

i = 0

while i < 5:
  p2 = random.choice(p2_list)

  a3 = input(" Select R, P or S ").upper()
  if a3 not in ["R", "P", "S"]:
    print("Invalid Input!")
    continue
      
  if a3 == p2:
      print("Tie !")
  elif a3 == "P" and p2 == "R":
      print("You Win !!") 
      score += 1
      i += 1
  elif a3 == "S" and p2 == "R":
      print("You Lose !!") 
      pc_score += 1
      i += 1
  elif a3 == "P" and p2 == "S":
      print("You Lose !!") 
      pc_score += 1
      i += 1
  elif a3 == "S" and p2 == "P":
      print("You Win !!") 
      score += 1
      i += 1
  elif a3 == "R" and p2 == "P":
      print("You Win !!") 
      score += 1
      i += 1
  elif a3 == "R" and p2 == "S":
      print("You Lose !!") 
      pc_score += 1
      i += 1

  if score == 3:
    print(f"Bob scored {pc_score} points and you scored {score} points")
    print("You Won against Bob!")
    break
    

  
  if pc_score == 3:
    print(f"Bob scored {pc_score} points and you scored {score} points")
    print("You Lost against Bob!")
    break

  


  
  print(f"Bob picked {p2}")
  print(f"Bob has {pc_score} points, Player has {score} points")


  



    
