import sys


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return user1, "wins!"
        else:
            return user2, "wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return user1, "wins!"
        else:
            return user2, "wins!"
    elif u1 == 'paper':
        if u2 == 'rock':
            return user1, "wins!"
        else:
            return user2, "wins!"
    else:
        return "Invalid input! You have entered rock, paper or scissors, try again."
        sys.exit()



user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do you want to choose rock, paper or scissor? " % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissor? " % user2)
print(compare(user1_answer.lower(), user2_answer.lower()))