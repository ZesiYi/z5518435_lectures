import random

# Define the deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [{"rank": rank, "suit": suit} for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal two cards to each player
player1_hand = [deck.pop(), deck.pop(), deck.pop()]
player2_hand = [deck.pop(), deck.pop()]

# Function to display a player's hand
def display_hand(player_name, hand):
    print(f"{player_name}'s Hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

# Display both players' hands
display_hand("Player 1", player1_hand)
print("\n")
display_hand("Player 2", player2_hand)

# Determine the winner based on hand ranks (simplified for this example)
def determine_winner(hand1, hand2):
    # In a real poker game, you'd use a more complex algorithm to compare hands.
    # For simplicity, we'll just declare Player 1 as the winner if they have more cards.
    if len(hand1) > len(hand2):
        return "Player 1 wins!"
    elif len(hand2) > len(hand1):
        return "Player 2 wins!"
    else:
        return "It's a tie!"

# Determine and display the winner
winner = determine_winner(player1_hand, player2_hand)
print("\n")
print(winner)

lst = [1, True, None]
print(f"lst is originally {lst}" )
lst.insert(1, "string") # lst is now [1, "string", True, None]
print(f'After insertion, lst is now {lst}')

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove('bad')
sol.append('including')
sol.insert(2,'good')
sol.extend(list_b)
print(sol)
