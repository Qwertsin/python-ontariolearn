"""Black Jack Assignment 5

Game Initialization:

Welcome the player.
Ask if they wish to start a new game.
Player's Turn:

Deal two cards to the player.
Display the total.
Deal two cards to the dealer (with one hidden).
Ask the player if they wish to "hit" or "stand".
Implement the logic for the player's decisions.
Dealer's Turn:
Implement the dealer's logic for drawing cards based on the game's rules.
Result Evaluation:

Compare the totals.
Announce the winner.
Replay:

Ask the player if they wish to play again.

"""

import random


def deal_card():  # function to deal a card that is between 1 and 10
    return random.randint(1, 10)


def hit_or_stay(total):  # function to prompt the user to hit or stay on their hand
    while total < 21:
        turn = input('Hit or stand? (h/s):').lower()

        # while hit_or_stay != 'h' and hit_or_stay != 's':
        if turn == 'h':
            add_card = deal_card()
            total += add_card
            print(f'Hit! You draw a {add_card}. Your total is {total}.', end=' ')

        elif turn == 's':
            print('You Stand.')
            break
        else:
            print("Invalid choice. Please input 'h' or 's'")

    return total


def dealer_turn(d_total):  # function to make the dealer hit if total is 16 or below
    while d_total <= 16:
        add_card = deal_card()
        d_total += add_card
        print(f"Hit! The dealer draws {add_card}. The dealer's total is {d_total}.")

    return d_total


def main():
    # welcome the player
    print('Welcome to Blackjack.')
    print('-' * 50)

    while True:     # new game loop
        # Ask if they wish to start the game?
        new_game = input('Do you wish to start a new game? (y/n):').lower()
        if new_game != 'y':
            print('Ok, Goodbye!')
            break

        # establish variables
        player_card_1 = deal_card()
        player_card_2 = deal_card()
        player_total = player_card_1 + player_card_2
        dealer_card_1 = deal_card()
        dealer_card_2 = deal_card()
        dealer_total = dealer_card_1 + dealer_card_2

        # present cards to users with one hidden
        print(f'You draw a {player_card_1} and a {player_card_2}. Your total is {player_total}.')
        print(f'The dealer draws a {dealer_card_1} and a hidden card.')

        player_total = hit_or_stay(player_total)

        if player_total > 21:   # bust scenario for user
            print('You bust!\n\nDealer wins!')
            continue

        # dealer's turn
        print(f"The dealer's hidden card is a {dealer_card_2} and has a total of {dealer_total}.")

        dealer_total = dealer_turn(dealer_total)

        # dealer bust scenario
        if dealer_total > 21:
            print(f'Dealer busts with {dealer_total}!\nYou Win ')
            continue

        # compare final hands
        if dealer_total >= player_total:
            print(f"Your total is {player_total} and the dealer's total is {dealer_total}.\n The dealer wins!")
        else:
            print(f"Your total is {player_total} and the dealer's total is {dealer_total}.\n You wins!")


if __name__ == "__main__":
    main()
