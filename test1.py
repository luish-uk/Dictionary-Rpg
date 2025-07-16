import random
import time
import webbrowser

animals_dict = {
    1 : 'pigeon',
    2 : 'ferret',
    3 : 'rabbit',
    4 : 'duck',
    5 : 'chicken',
    6 : 'lamb',
    7 : 'pig',
    8 : 'cow',
    9 : 'deer',
    10: 'lion'
}
success_rate = 10
n_of_hunts = 0
inventory = {}
def hunt():
    global success_rate
    global inventory
    global n_of_hunts
    sleep = random.randint(1, 5)
    time.sleep(sleep)
    print('\n\n\n\n3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    sleep = random.random()
    time.sleep(sleep)
    print('\nBANG!')
    sleep = random.randint(1, 5)
    time.sleep(sleep)
    animal = random.randint(1, 10)
    success = random.randint(1, 100)
    if success > success_rate:
        animal_caught = animals_dict[animal]
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDUUUNNNNNN!')
        sleep = random.random()
        time.sleep(sleep)
        time.sleep(2)
        print(f'\n\nCongrats, you caught a {animal_caught}')
        success_rate+=5
        n_of_hunts+=1
        inventory[n_of_hunts] = animal_caught  
        try_again()

    else:
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDun!')
        sleep = random.random()
        time.sleep(sleep)
        print('\n\n\nDUUUNNNNNN!')
        sleep = random.random()
        time.sleep(sleep)
        time.sleep(2)
        print(f'\n\nOh no you just missed you shot at catching a {animals_dict[animal]}')
        n_of_hunts+=1
        try_again()
def try_again():
    global inventory
    try_again = input("\n\nWould ya like to continue huntin'?\n(y/n?) : ")
    if try_again == 'n':
        play()
    elif try_again == 'y':
        hunt()
    elif try_again == 'russianroulette':
        webbrowser.open('https://youtu.be/9zqsc7mad24?si=doA53ottaxvAuA8a&t=15')
        time.sleep(15)
        gun = random.randint(1, 6)
        print("\n\n\nROULETTE TIME!!!!\n\n\n\n")
        print("Gun")
        time.sleep(1)
        print('\nLocked and loaded')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        if gun == 6:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBANG')
            del inventory
            inventory = {}
            time.sleep(2)
            print('del inventory')
            time.sleep(3)
            print('Toushe partner, I jusy wiped your whole collection like that purple hulk')
            play()
        else:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nclick')
            time.sleep(2)
            print('\n\nOh well you got lucky this time huh partner?')
            play()
    else:
        print("\n\nWell im afraid that aint an answer I was lookin for")
        quit()
    
def play():
    play = input("\n\n\n\nHello sir, would you like to go huntin'?\n(y/n?) : ")
    if play == 'n':
        collection = input("\n\nWell then sir, would ya like to see your collection?\n(y/n?) : ")
        if collection == 'n':
            quit()
        elif collection == 'y':
            print(f'\n\ninventory:\n{inventory}\n\nNumber of hunts done: {n_of_hunts}')
            try_again()
        else:
            print("\n\nWell im afraid that aint an answer I was lookin for")
            quit()

    elif play == 'y':
        hunt() 
    else:
        print("\n\nWell im afraid that aint an answer I was lookin for")
        quit()

success_rate = 10
n_of_hunts = 0
inventory = {}

play()