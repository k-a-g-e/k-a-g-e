''' Made by k-a-g-e
    March 2021
    
'''

import random

challenges = ["Hit Someone", "Compliment Someone", "Have a conversation with someone",
              "Call Someone"]
weak_ch = ["1","2","3","4"]
reward = list(range(10, 51, 10))

# future note: change the user's name to (UsEr)upper.lower.continuously
user_name = input("Please Enter You Name ")
#user_gender = input("Are You A Male(m) or Female(f)")
user_age = int(input("Please Enter You Age "))

rand_ch = random.choice(challenges)
rand_wk = random.choice(weak_ch)
rand_rew = random.choice(reward)
chall = ""
#future note to keep count of score for the user


def decorate(task):
    def deco():
        print('_' * 70 + "\n" + "-" * 70)
        task()
        print("_" * 70 + "\n" + "-" * 70)
    return deco

@decorate
def out_put():
    score = 0
    if (user_age >= 0) and (user_age < 18) :
        print("Since your age is below 18 you will have restricted access")
        chall = rand_wk
        score += rand_rew
    elif (user_age >= 18 ) and (user_age < 41 ):
        print("You age is optimum for the challenge")
        chall = rand_ch
        score += rand_rew
    elif (user_age >= 41 ) and (user_age < 120 ):
        score = "0"
        return print("Sorry but You are too old to participate")
    elif user_age >= 120 :
        score = "0"
        return print("Are you sure your age is correct")
    else:
        print("please enter valid numbers")
        score = "0"
    print(f"Hello {user_name.upper()}, For Today's challenge you must to {chall}.")
    print(f"{user_name}. If you complete the challenge you will get {rand_rew} points.")
    return score


out_put()
