

# BASIC QUIZ APP####
age = 50
message = "welcome to the game "
print(message)

choice = input("Do you want to play Squid game __?? ")
# player choice


if choice == "yes":
    print("Lets play...")

else:
    print("you can foooock off , order of the peaky blinders")
    quit()
score = 0

# game begins
# so an input method is called to take user's answer to the question
# and save this answer in variable answer
answer = input("what was ragnar's Lothbrok first job in vikings???  ").lower()
if answer == "farmer":
    print("SKOLLLL!")
    score += 1
else:
    print('You fucked up')

#question 3
answer = input('what language is spoken in kenya:').lower()
if answer == "swahili":
    print("correct")
    score += 1

else:
    print('incorrect')

#question 4
answer = input('what language is spoken in china:').lower()
if answer == "mandarin":
    print("correct")
    score += 1

else:
    print('incorrect')

print(f'your score is {score}')


