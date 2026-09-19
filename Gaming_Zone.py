import random
game = int(input("1.Guess the Number \n2.Rock Paper Scissors \nselect a game you want to play: "))

if game == 1:
    guess = random.randint(1, 10)
    while True:
        number = int(input("Select  a number: ").lower().strip())
        if number == guess:
            print("You got it!")
            break
        elif number > guess:
            print("Your guess is too high.")
        elif number < guess:
            print("Your guess is too low.")
elif game == 2:
    count_p1 =0
    count_p2 =0
    count = 0
    for i in range(5):
        player1 = input("Enter your move : ").lower().strip()
        player2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
        print(player2)
        if player1 == player2:
            print("draw")
        elif player1 == "rock" and player2 == "paper":
            count_p2 += 1
        elif player1 == "paper" and player2 == "rock":
            count_p1 += 1
        elif player1 == "paper" and player2 == "scissors":
            count_p2 += 1
        elif player1 == "scissors" and player2 == "paper":
            count_p1 += 1
        elif player1 == "scissors" and player2 == "rock":
            count_p2 += 1
        elif player1 == "rock" and player2 == "scissors":
            count_p1 += 1
        print(f'Player 1: {count_p1}')
        print(f'Player 2: {count_p2}')

    if count_p1 > count_p2:
        print("player 1 wins")
    else:
        print("player 2 wins")