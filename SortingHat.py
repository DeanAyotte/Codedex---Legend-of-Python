#Codedex
#Sorting Hat

#Houses

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#Header

print ("The Sorting Hat")

print ("\nWhich house will you join?")

#Question 1

print ("\nQ1) Do you like Dawn or Dusk?")

print ("\n1) Dawn")
print ('2) Dusk')

answer = int(input("\nEnter your answer (1-2): "))

if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print ("\nWrong input.")

#Question 2

print ("\nQ2) When I'm dead, I want people to remember me as:")

print ("\n1) The Good")
print ("2) The Great")
print ("3) The Wise")
print ("4) The Bold")

answer = int(input("\nEnter your answer (1-4): "))

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print ("\nWrong input.")

#Question 3

print ("\nQ3) Which kind of instrument most pleases your ear?")

print ("\n1) The violin")
print ("2) The trumpet")
print ("3) The piano")
print ("4) The drum")

answer = int(input("\nEnter your answer (1-4): "))

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer ==3:
  Ravenclaw += 4
elif answer ==4:
  Gryffindor += 4

else:
  print ("\nWrong input.")

#Results

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print("\n🦁 Gryffindor!")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print("\n🦅 Ravenclaw!")
elif Hufflepuff >= Slytherin:
  print("\n🦡 Hufflepuff!")
else:
  print("\n🐍 Slytherin!")
