import random
def deal(deck,hand, count):
    card_1 = random.choice(list(deck.keys()))
    hand[card_1] = deck[card_1]
    deck.pop(card_1)
    card_2 = random.choice(list(deck.keys()))
    hand[card_2] = deck[card_2]
    deck.pop(card_2)

    count = sum(hand.values())

    while count > 21 and 11 in hand.values():
        for c, v in hand.items():
            if v == 11:
                hand[c] = 1
                break
    count = sum(hand.values())

    return hand, count


def hit(deck,hand, count):
    card = random.choice(list(deck.keys()))
    count = sum(hand.values())
    hand[card] = deck[card]
    deck.pop(card)

    while count > 21 and 11 in hand.values():
        for c, v in hand.items():
            if v == 11:
                hand[c] = 1
                break
    count = sum(hand.values())

    return hand, count


#after basic funtions work add a memory counter so it keeps track of your wins and losses aswell as profit or debt
wins = 0
losses = 0
profit = 0
while True:
    answer =  input("Play? (y/n)")
    if answer.lower() != 'y':
        break
    ranks = ["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    suits = ["♠","♥","♦","♣"]
    deck = {}
    #update functions to work with new deck,
    # additionally add the removal option
    # and memory and ur done
    for rank in ranks:
        for suit in suits:
            if rank in ['J', 'K', 'Q']:
                value = 10
            elif rank == 'A':
                value = 11
            else:
                value = int(rank)
            deck[(rank,suit)] = value


    bet = int(input("Place a bet: "))

    dealer_count = 0
    dealer_hand = {}

    player_count = 0
    player_hand = {}

    print(f"The bet is ${bet}")

    dealer_hand, dealer_count = deal(deck, dealer_hand, dealer_count)
    player_hand, player_count = deal(deck, player_hand, player_count)

    print(f'Dealer: {dealer_hand},Total: {dealer_count}')
    print(f'Player: {player_hand}, Total: {player_count}')

    stand = input("Hit or Stand?")

    #dealer doesnt hit anymore if their hand is more than 17
    # player can keep hitting if they want

    while dealer_count < 17:
        dealer_hand, dealer_count = hit(deck, dealer_hand, dealer_count)


    while stand.lower() != "stand":
        player_hand, player_count = hit(deck, player_hand, player_count)
        print(f"\nPlayer hits!\n")
        print(f"Dealer:{dealer_hand} Total: {dealer_count} \nPlayer:{player_hand} Total: {player_count}")
        stand = input("Hit or Stand?")


    if (dealer_count > 21 and player_count > 21) or (player_count == dealer_count):
        print("Stalemate")
    elif dealer_count > 21:
        print("Player wins!")
        profit += bet
        wins += 1
    elif player_count > 21:
        print("Player Loses")
        profit -= bet
        losses -= 1
    elif dealer_count > player_count:
        print("Dealer Wins!")
        profit -= bet
        losses -= 1
    elif dealer_count < player_count:
        print("Player Wins!!")
        profit += bet
        wins += 1


    print("$ " + str(profit))
    print("Wins:" , wins, "| Losses:", losses, "| Profit:", profit)
