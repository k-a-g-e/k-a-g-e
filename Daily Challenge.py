import random

challenges_1 = ["Hit Someone", "Compliment Someone", "Have a conversation with someone",
              "Call Someone"]
reward = list(range(10, 51, 10))

# future note: change the user's name to (UsEr)upper.lower.continuously
user_name = input("Please Enter You Name ")
#user_gender = input("Are You A Male(m) or Female(f)")
#user_age = int(input("Please Enter You Age "))

rand_ch = random.choice(challenges_1)
rand_rew = random.choice(reward)

def decorate(task):
    def deco():
        print('_' * 70 + "\n" + "-" * 70)
        task()
        print("_" * 70 + "\n" + "-" * 70)
    return deco

@decorate
def out_put():
    print(f"Hello {user_name.upper()}, For Today's challenge you must to {rand_ch}.")
    print(f"{user_name}. If you complete the challenge you will get {rand_rew} points.")

out_put();
