def start():
    print('Welcome!,young traveller')
    tiny_field()

def tiny_field():
    print('I am an ancient mgical orb,I want you to save this forest by touching the sword of enlighntenment.')
    move = input('\nnow Where would you like to go? Say one of these choices:\n\tdeep_roots\n\tpot_stop\n\tgivingup\n\tgraveyard\n:')
    if move.lower() == 'deep_roots':
        deep_roots()
    elif move.lower() == 'pot_stop':
        pot_stop()
    elif move.lower() == 'givingup':
        givingup()
    elif move.lower() == 'graveyard':
        graveyard()

def deep_roots():
    print('You are in deeproots.The place that holds the sword, the key to your mission or the end goal.But it is not so easy, a thick hoard of trees block your way.You can either go through the trees and die due to injury but still win, or you could burn the tress with a fire orb and cause a forest fire killing everything and you would still win.')
    move = input('\nWhere would you like to go? Say one of these choices:\n\ttiny_field\n\tsword\n:')
    if move.lower() == 'tiny_field':
        tiny_field()
    elif move.lower() == 'sword':
        sword()

def sword():
    go_through = input('Would you like to go through,please say yes,no or use orb:')
    if go_through == 'yes':
        print('You go through,ducking and dodging your body to avoid the branches of the sturdy trees')
        print('while dodging, you dont notice a sharp branch and it pierces you.......')
        print('but being fueled by justice and the need to help others just like an anime protagonist you power through...')
        print('You reach the area, seeing the sword made your knees weak, was it the sword or the amout of blood you lost....\nyou sart to get dizzy and lose your vision....\nyou fall on your knees')
        print('You try to stand up but you lost all strength,and crawl towards the sword.... you reach your hand out and before you could see or feel the swordhlit, your vision gives out and you see the darkness, the cold and alone darkness.....')
        print('Looks like you managed to touch it, so you won congragulations, the orb dances around you')
        print('ending 1 out of 5, Touch of enlightenment, you are dead tho')
        input('press enter to go back')
        tiny_field()
    elif go_through == 'no':
        print('you should try finding the orb,')
        input('press enter to go back')
        deep_roots()

    global haveorb
    if go_through == 'use orb':
        if not haveorb :
            print('seems like you dont have the orb, please go through or go get the orb')
            input('press enter to go back')
            deep_roots()

        elif haveorb == True :
            print('Ah! traveller it seems like you do have the orb. You can chose to use it or you can die while saving us.')
            print('you use the orb and see as the fire rages through burning the trees in your way opening a path but everything else burns')
            print('you feel guilty but it quickly washes away as you have work to do')
            print('you enter and see the sword,you touch it.........')
            print('light glows around you and you wake up in your bed, You won....but at what cost ')
            print('ending 2 out of 5, Touch of fire')
            input('press enter to go back')
            tiny_field()

def pot_stop():
    print('You are in pot_stop. This is where travellers like you come and rest. You see a big pot with a raging fire, You stare in the fire and you get kinda hungry. You look at the orb and it looks like a flying chicken and you get the urge to eat it.')
    move = input('\nWhere would you like to go back? Say :\n\ttiny_field\nyou remember your thought from earlier, would you like to grab the flying chick.. I mean orb,say yes or no :')
    if move.lower() == 'tiny_field':
        tiny_field()
    elif move == 'yes':
        print('you grab the orb with force, and it struggles in your arm, you grow closer to the pot and hear the fire crackle, you throw the orb and and watch as it cooks \nor so you thought, it disapears before your eyes and you start to feel sad')
        print('Congragulations dummy, you lost your guide, ending 4 of 5, Disintegration')
        input('press enter to go back')
        tiny_field()
    if move == 'no':
        print('You contain your urges and go on your journey')
        input('press enter to go back')
        pot_stop()

def givingup():
    print('You are in the backwoods, this place is quiet and peacefull you see an ominous door, you try to ask the orb but the orb wont float to this area')
    move = input('\nWhere would you like to go? Say:\n\ttiny_field\nYou get closer to the door, you feel strange weird,as if you are awake. The feeling only gets stronger as you go closer. Would you like to go through? say yes or no:')
    if move.lower() == 'tiny_field':
        tiny_field()
    elif move == 'yes':
        print('You go through the door.........')
        print('you slowly open you eyes, you look around you and you see your room. The same room you always had.\nYou get up slowly and start recalling your weird dream, you chuckle quietly at how weird it was. No matter time to go to school.')
        print('ending 3 of 5...... Giving up')
        input('press enter to go back')
        tiny_field()
    elif move == 'no':
        print('okay')
        input('press enter to go back')
        tiny_field()
        
   

def graveyard():
    print('This is the graveyard, what no the people buried are not travellers, well not the recent one atleast.')
    move = input('\nWhere would you like to go back? Say tiny_field\nYou see an animal lying on the groud,injured probably. You get a feeling you should help. But you also see the orb. What do you want to do? animal or orb:')
    if move.lower() == 'tiny_field':
        tiny_field()
    elif move == 'animal':
        print('You approch the animal, it looks at you.You notice something is not right, its not injured at all')
        print('But before you could back out two big shadowy figures jump out of the bushes and pin you to the ground.')
        print('You try to fight, but those are animals you cant overpower them. You look at the original animal on the ground, relaxing and you could almost make out the smirk of the animal,but before you could you lose your vision.')
        print('You have died,dont worry this is also an ending. 5 of 5. Eaten by animals')
        input('press enter to go back')
        tiny_field()
    elif move == 'orb':
        global haveorb
        haveorb = True
        print('You have acquired the orb, you feel a surge of power. No time to waste a forest needs saving')
        input('press enter to go back')
        tiny_field()


########
#main
#######
#TODO: Add some global variables
haveorb = False

start()