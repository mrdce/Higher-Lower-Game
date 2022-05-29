import random
import game_data
import art


def display(first, second):
    """Display the first comparison (with art)."""
    print(f'Compare 1: {first["name"]}, a {first["description"].lower()} from {first["country"]}')
    print(art.vs)
    print(f'Against 2: {second["name"]}, a {second["description"].lower()} from {second["country"]}')


def checker(first, second, firstf, secondf):
    """Display the question as an input var. Compare the comparison result with the user's answer. If correct, continue
    (the last becomes first!). Lose. """
    answer = input('Who has more followers? Type 1 or 2: ')
    if (firstf > secondf and answer == '1') or \
            (firstf < secondf and answer == '2'):
        first = second
        print(f'You are right!')
    else:
        print(f'Sorry, this is wrong. Final score: {score_counter}')
        return False
    return first


print(art.logo)
first_choice = random.choice(game_data.data)
score_counter = 0
while True:
    # Continue playing. Second becomes first. + Score counter
    second_choice = random.choice(game_data.data)
    first_f = first_choice['follower_count']
    second_f = second_choice['follower_count']
    display(first=first_choice, second=second_choice)
    first_choice = checker(first=first_choice, second=second_choice, firstf=first_f, secondf=second_f)
    if not first_choice:
        break
    score_counter += 1
