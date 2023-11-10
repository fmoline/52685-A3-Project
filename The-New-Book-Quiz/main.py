import os
import sys
import time

a = 0
b = 0
c = 0
d = 0
e = 0

def typingeffect(chat):
  for character in chat:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def clearscreen():
  os.system("clear")

typingeffect("Welcome to The New Book Quiz!\n")
time.sleep(1)
typingeffect("Answer the questions and I'll tell you which one of my favourite books you should read!\n")
typingeffect("To answer, type the letter in lowercase and press enter.")
print("\n")

time.sleep(1)
#Question 1:
print("Q1: Which genre do you like the most?")
print("a: Dystopian")
print("b: Psychological Thriller")
print("c: Romance")
print("d: Fantasy")
print("e: Mystery")

while True:
  answer = input("Answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2
    break
  elif answer == 'c':
    c += 2
    break
  elif answer == 'd':
    d += 2
    break
  elif answer == 'e':
    e += 2
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 2
print("Q2: Which bird is your favouite...")
print("a: Pheonix")
print("b: Canary")
print("c: Dove")
print("d: Peacock")
print("e: Kookaburra")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 3
print("Q3: Which superpower would you most like to have?")
print("a: Invisibility")
print("b: Mind-reading")
print("c: Time travel")
print("d: Element control")
print("e: Teleportation")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 4
print("Q4: What kind of kid were you?")
print("a: The Bookworm")
print("b: The Scooby Doo Kid (loved solving mysteries)")
print("c: The \"Lets play family!\" Kid")
print("d: The 'Horse Girl' Kid (Don't be embarrassed - I was one!")
print("e: The Sporty Kid")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 5
print("Q5: Who is your favourite 'New Girl' character?")
print("a: Schmidt")
print("b: Nick Miller")
print("c: Cece Parikh")
print("d: Jessica Day")
print("e: I don't know what New Girl is...?")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    print("\n")
    typingeffect("You don't know 'New Girl'?! It's only the greatest show on Earth.\n")
    typingeffect("You're not allowed to continue until you've seen the show.\n")
    typingeffect("Goodbye!")
    time.sleep(3)
    clearscreen()
    sys.exit()
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 6
print("Q6: Which Barbie character do you relate to most?")
print("a: Ken")
print("b: Weird Barbie")
print("c: Barbie")
print("d: Allan")
print("e: Mermaid Barbie")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 7
print("Q7: Which Harry Styles song is your favourite?")
print("a: Sign of the Times")
print("b: Medicine")
print("c: Love of My Life")
print("d: Lights Up")
print("e: I don't listen to Harry Styles")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    print("\n")
    typingeffect("Ha Ha! That must be a joke.\n")
    typingeffect("I'll give you another try. Answer properly this time...")
    time.sleep(1)
    print("\n")
    #Question 7.2
    print("Q7: Which Harry Styles song is your favourite?")
    print("a: Sign of the Times")
    print("b: Medicine")
    print("c: Love of My Life")
    print("d: Lights Up")
      
    while True: 
      answer = input("Answer: ")
      if answer == "a":
        a += 1
        break
      elif answer == 'b':
        b += 1
        break
      elif answer == 'c':
        c += 1
        break
      elif answer == 'd':
        d += 1
        break
    break
      
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 8
print("Q8: Which deli meat are you buying?")
print("a: Ham off the bone")
print("b: Proscuitto")
print("c: None! I don't eat meat")
print("d: Spicy Salami")
print("e: Panchetta")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 9
print("Q9: If you could travel to any of these countries, where would you go:")
print("a: The United Stated")
print("b: Antarctica")
print("c: South America")
print("d: Greece")
print("e: New Zealand")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 10
print("Q10: Which Christmas movie are you watching:")
print("a: The Nightmare Before Christmas")
print("b: The Polar Express")
print("c: The Holiday")
print("d: How the Grinch Stole Christmas")
print("e: Home Alone")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

print("\n")
#Question 11
print("Q11: Pick a pastry")
print("a: A croissant")
print("b: A pain aux raisans")
print("c: An eclair")
print("d: A danish")
print("e: A pain au chocolat")

while True:
  answer = input("Answer: ")
  if answer == "a":
    a += 1
    break
  elif answer == 'b':
    b += 1
    break
  elif answer == 'c':
    c += 1
    break
  elif answer == 'd':
    d += 1
    break
  elif answer == 'e':
    e += 1
    break
  else:
    print(input("That's not an answer! Try again: "))
    break

while True:
  print("\n")
  typingeffect("Anaylsing answers...\n")
  typingeffect("Choosing best book match...")
  typingeffect("Aha! I know the one...")
  time.sleep(1)
  clearscreen()
  break

#outcomes
print("\n")
while True:
  if a > b and a > c and a > d and a > e:
    typingeffect("Your new book: Farenheit 451 by Ray Bradbury\n")
    time.sleep(1)
    print("\n")
    print("Synopsis: In a future society where books are forbidden, Guy Montag, a 'fireman' whose job is the burning of books, takes a book and is seduced by reading. He begins to question his duty to the state and ultimately has to choose between his personal beliefs and his loyalty to the government.")
    break
  if b > a and b > c and b > d and b > e:
    typingeffect("Your new book: The Silent Patient by Alex Michaelides\n")
    time.sleep(1)
    print("\n")
    print("Synopisis: Alicia Bereson shot her husband five times in the face and never spoke another word. Theo Faber is a criminal psychotherapist who is obsessed with uncovering her motives, taking him down a twisting path into his own motivations.")
    break
  if c > a and c > b and c > d and c > e:
    typingeffect("Your new book: Everything I Know About Love by Dolly Alderton\n")
    time.sleep(1)
    print("\n")
    print("Synopisis: A wildly funny, occasionally heartbreaking internationally bestselling memoir about growing up, growing older, and learning to navigate friendships, jobs, loss, and love along the ride.")
    break
  if d > a and d > b and d > c and d > e:
    typingeffect("Your new book: The Red Queen by Victoria Aveyard\n")
    time.sleep(1)
    print("\n")
    print("Synopsis: Mare Barrow's world is divided by blood - those with common, Red blood serve the Silver-blooded elite, who are gifted with superhuman abilities. Mare is a Red, scraping by as a thief in a poor, rural village, until a twist of fate throws her in front of the Silver court.")
    break
  if e > a and e > b and e > c and e > d:
    typingeffect("Your new book: The Dry by Jane Harper\n")
    time.sleep(1)
    print("\n")
    print("Synopsis: Amid the worst drought in a century, Falk and the local detective question what really happened to Luke. As Falk reluctantly investigates to see if there's more to Luke's death than there seems to be, long-buried mysteries resurface, as do the lies that have haunted them.")
    break

time.sleep(3)
print("\n")
typingeffect("If you've already read this book, or want a new one, retake the quiz!\n")
typingeffect("Hint: giving the opposite answers will give you a book that's out of your comfort zone :D\n")