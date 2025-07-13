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
                break # Break out of the player input loop and to 'roll the dice'.
            if playerMove == 'h':
                if hope > 0:
                    hope = hope - 1 # Allows player to use a Hope resource if available, lowering the tracker by one.
                    print('%s Hope, %s Fear' % (hope, fear))
                else:
                    print('No hope available.')
            if playerMove == 'f':
                if fear > 0:
                    fear = fear - 1 # Allows solo player / GM to use a Fear resource if available, lowering tracker by one.
                    print('%s Hope, %s Fear' % (hope, fear))
                else:
                    print('No fear available.')
            print('Choose adventurer, and (r)oll, (q)uit, use (h)ope or use (f)ear.')

        # Roll the dice
        if playerMove == 'r':
            hopeDice = random.randint(1, 12)
            fearDice = random.randint(1, 12)
            roll = int(hopeDice) + int(fearDice)
            print('You rolled {} with ...'.format(roll))
            if hopeDice > fearDice:
                print('... hope')
                if hope < 6: # The TTRPG rules allow you to have up to but not exeeding 6 Hope at any time.
                    hope += 1
            if hopeDice < fearDice:
                print('... fear')
                if fear < 6: # The TTRPG rules allow you to have up to but not exeeding 6 Fear at any time.
                    fear += 1
            if hopeDice == fearDice:
                print('Critical succes! You may clear one stress and possibly increase the Damage calculation (if applicable).')
                if hope < 6:
                    hope += 1
        print('%s Hope, %s Fear' % (hope, fear))
