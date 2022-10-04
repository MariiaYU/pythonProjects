# from replit import clear
import random
from logo_instagramvs import logo, vs
from data_instagramvs import data

def person_info(person, letter):
    print(f"Compare {letter}: {person['name']}, a {person['description']}, from {person['country']}.")


person_A = random.choice(data)
person_B = random.choice(data)

print(logo)

play = True
scores = 0

while play:
    if person_A == person_B:
        person_B = random.choice(data)
    person_info(person_A, "A")
    print(vs)
    person_info(person_B, "B")
    followers_A = person_A['follower_count']
    followers_B = person_B['follower_count']
    who = input("Who has more followers? Type 'A' or 'B': ").lower()

    if who == "a" and followers_A >= followers_B:
        scores += 1
        # clear()
        print(logo)
        person_A = person_B
        person_B = random.choice(data)
    elif who == "b" and followers_B >= followers_A:
        scores += 1
        # clear()
        print(logo)
        person_A = person_B
        person_B = random.choice(data)
    else:
        # clear()
        print(logo)
        print("You lose!")
        play = False
    print(f"Your score: {scores}")
