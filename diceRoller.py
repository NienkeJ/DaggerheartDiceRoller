# Daggerheart Dice Roller
# A dice roller for the game Daggerheart

import random, sys

print('A Daggerheart dice roller')
print('Good luck adventurer')

# These trackers keep track of a player's Hope and Fear.
hope = 0
fear = 0

while True: # The main game loop.
    print('%s Hope, %s Fear' % (hope, fear))
    while True: # The player input loop.
        print('Enter your move: (r)oll, (q)uit, use (h)ope or use (f)ear.')
        while True: # Player rolls the dice or uses their resources.
            playerMove = input()
            if playerMove == 'q':
                sys.exit() # Quit the program.
            if playerMove == 'r':
                break # Break out of the player input loop
            if playerMove == 'h':
                hope = hope - 1
                print('%s Hope, %s Fear' % (hope, fear))
            if playerMove == 'f':
                fear = fear - 1
                print('%s Hope, %s Fear' % (hope, fear))
            print('Choose adventurer, and (r)oll, (q)uit, use (h)ope or use (f)ear.')

        # Roll the dice
        if playerMove == 'r':
            hopeDice = int(random.randint(1, 12))
            fearDice = int(random.randint(1, 12))
            roll = int(hopeDice) + int(fearDice)
            print('You rolled {} with ...'.format(roll))
            if hopeDice > fearDice:
                print('... hope')
                hope = hope + 1
            if hopeDice < fearDice:
                print('... fear')
                fear = fear + 1
            if hopeDice == fearDice:
                print('Doubles! An extreme event')
        print('%s Hope, %s Fear' % (hope, fear))
