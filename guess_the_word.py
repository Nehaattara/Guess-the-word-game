import random
name=raw_input(("What is your name?"))
print("Good Luck!",name)
words=['apple','banana','mango','kiwi']
word=random.choice(words)
#print(word)
print("Guess the characters:")
guesses=''
turns=3
while turns>0:
	failed=0
	for char in word:
		if char in guesses:
			print(char)
		else:	
			#print("_")	
			failed+=1

	if failed==0:
		print("You Win")

		print("The word is",word)
		break
	guess=raw_input("guess the characters")
	guesses+=guess
	if guess not in word:
		turns-=1
		print("Wrong")
		print("You have",+turns,"more guesses")

		if turns==0:
			print("You loose..")