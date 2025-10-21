date = input("Enter today's date: ")
rating = input("How do you rate your mood today from 1 to 10 ? ")
thought = input("Let your thought flow: \n")

with open(f"./journal/{date}.txt",'w') as file : 
  file.write(rating + "\n")
  file.write(thought)