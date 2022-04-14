import random
import time
import os
import os.path

nono = random.randint(1000,9999) # 4-digit random number generation 
answer = (nono + 20000) -2

#storing the prediction in a file.
file_exists = os.path.exists('secret.txt') # checks whether file exists or not
#print(file_exists)
if file_exists == True:
  os.remove("secret.txt")
else:
  pass
f = open("secret.txt", "x")
f = open("secret.txt", "a")
f.write("I have predicted this even before starting the game.\nThe number is:")
f.write(str(answer))
f.close()

#function
def guess(): 
  num = int(input("Your Turn:\nPlease enter a four digit number:\n"))
  x = [int(a) for a in str(num)]
  number.append(x)

  ans = []
  no2 = []
  j = 0
  #guessno(num)
  while num >0:
    ans.insert(0,num%10)
    num = (num -num%10)//10
  
  j=0

  while True:
    s = random.randint(0,9)
    if(len(no2) == 4):
      break
    if(s +ans[j] == 9):
      no2.append(s);
      j+=1
  print("ummm...")
  time.sleep(1)
  print("okay I choose....\n",*no2)
  number.append(list(no2))

print("Hey There !!!")
name = input("Please enter your name:\n").lower()
time.sleep(0.5)
print("Hey", name,",I hope you are doing fine.")
time.sleep(1)
print("----------------------------")
time.sleep(1)
print("WELCOME TO MAGIC WITH NUMBERS")
time.sleep(1)
print("----------------------------")
time.sleep(0.5)
print("Without further ado")
print("Let's start the game")
time.sleep(1.5)
print("This game is very simple...")
time.sleep(1)
print("First I'll choose a number, then you do the same.")
time.sleep(1.5)
print("Let me start off by choosing a number... Um I choose :")
time.sleep(1.5)
print(nono)
number = []
g = [int(a) for a in str(nono)]
number.append(g)

for i in range(2):
  guess()
  
print()


time.sleep(1)
print("That's it !!!")
time.sleep(1.5)
print("Now I want you to calculate the numbers which You and I have randomly guessed")
print("Here are all the numbers that we have guessed...")
time.sleep(2)

for i in number:
  print(i)

resultt = input("Type Yes if you are done calculating.").lower()
if resultt == "yes":
  pass
time.sleep(1.5)
print("BRACE YOURSELF!!!!!")
time.sleep(1.5)
print("What if I told you...")
print("I have already predicted the sum and stored it in a file")
print("Search for a file on your machine ::: secret.txt ")
time.sleep(1.5)
print("You will find that the sum has already been predicted.")
print("And if you are a developer or a beginner, you can scan the entire code... I havent used addition in the entire code")

# NO ADD COMMAND IS USED ANYWHERE IN THE PROGRAM. YOU CAN APPRECIATE THIS MAGIC WITH A THUMBS UP .
