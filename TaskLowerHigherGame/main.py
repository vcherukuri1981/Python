import random
from game_data import data
from art import logo, vs

print(logo)

def get_random_account():
    return random.choice(data)

def format_account(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

score = 0
should_continue = True
account_a = get_random_account()
account_b = get_random_account()
while account_a == account_b:
    account_b = get_random_account()

while should_continue:
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']

    is_correct = (follower_a > follower_b and user_guess == 'A') or (follower_b > follower_a and user_guess == 'B')
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

