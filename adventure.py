import random
import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

class style:
   LOSE = "\033[1m" + "\033[41m"
   WIN =  "\033[1m" + "\033[42m"
   BOLD = "\033[1m"
   END = "\033[0m"


venues = [["Roses", "Olfe", "Südblock", "Silverfuture", "Rauschgold", "Woof"] ,["Schwuz","Chantal's", "SO36"]]
bars = venues[0]
clubs = venues[1]
cash = 0
visits = 0

print("""
Hi friend!!! Are you ready for a night out? I'm so excited, let's get wild!
I'm gonna take you to some of my favorite bars and once we've done the rounds we'll go to the club.

""")
cash = int(input("Most places are still cash only, how much do you have?\n"))

while cash < 30 or cash > 75:
    if cash < 0:
        print("How can you have negative cash? are you trying to trick me?")
        cash = int(input("For real though, how much do you have?\n"))

    elif cash < 30:
        print("are you broke? here you can borrow 20 from me\n")
        cash += 20
        break

    elif cash > 75:
        print("WOW! that's a bit too much! take 75 and leave the rest\n")
        cash = 75

print("Fantastic, then lets get going. I think you're gonna really enjoy this first place.\nLove your outfit by the way! I think you'll manage to flirt your way into some free drinks, but watch out, people might convince you to buy drinks for them")

input("press a key\n")
clearscreen()

room = random.choice(bars)

while cash > 0 and visits < 4:
    
    if room == "Roses":
        print("""This is Roses.\nIt's a small bar and the furry red walls make it feel even smaller. It's packed though, let's try to make it to the bar\n""")
        flirt = input("Omg, people are looking at you like they like you, maybe someone will buy you a drink!\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("I Love making new friends that buy you drinks! YAY!\n")
            else:
                print("LOL you ended up paying for their drinks yourself!\n")
                cash -= 12
        elif flirt == "no" or flirt == "n":
            cash -= 8
            print("Don't worry, maybe we can try in the next place after we loosen up a little.")
        venues[0].remove("Roses")

    elif room == "Olfe":
        print("""This is a bar called Möbel Olfe after the furniture store that used to be here.\nIt's big and roomy with some very interesting lamps and decorations. The staff is a bit surly but after you manage to elbow your way to the bar, that just adds to the charm.""")
        flirt = input("Look at all these cuties! I think if you chat someone up you can a free drink\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("OMG! Free drinks! YAY!\n")
            else:
                print("Wow, that was a smooth talker, they got a free drink out of you instead!\n")
                cash -= 18
        elif flirt == "no" or flirt == "n":
            cash -= 12
            print("It's fine, we can try at the next place.")
        # visits += 1
        venues[0].remove("Olfe")

    elif room == "Südblock":
        print("""This is Südblock.\nThe atmosphere here is relaxed and welcoming. Even though it's at a busy intersection, you find the terrace to be a very pleasant break from the bustle all around""")

        flirt = input("That table looks friendly, maybe we can sit with them and see if they'll buy us some drinks!\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("Yaas! What a fun time! Made more fun by the free beer!\n")
            else:
                print("These people were even more broke than us! You ended up paying for them!\n")
                cash -= 18
        elif flirt == "no" or flirt == "n":
            cash -= 12
            print("Yeah, it's a bit too hectic here, we can be more bold at a more intimate setting.")
        # visits += 1
        venues[0].remove("Südblock")

    elif room == "Silverfuture":
        print("""We made it to Silverfuture, lets plop down on that sofa over there.\nThis bar is very nice and comfy where you can have some cocktails without a worry about who you are, or what your drink choice is...""")
        flirt = input("These people next to us seem friendly, try to get that Strawberry Daiquiri from them\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("Tourists are always so open and ready to spend money. Good call on asking them for drinks!\n")
            else:
                print("Backpackers are always so broke! But I guess we helped them extend their vacation\n")
                cash -= 26
        elif flirt == "no" or flirt == "n":
            cash -= 18
            print("Yeah, I'm not feeling the flirty vibe here, but we can think about it somewhere else.")
        # visits += 1
        venues[0].remove("Silverfuture")

    elif room == "Rauschgold":
        print("""Wow, Rauschgold is busy today, and they've put up so many decorations everywhere!\nIt looks like the drag show just started, perfect time to make our way to the bar and get something""")
        flirt = input("This group by the bar seems to be about to get some drinks, lets see if we can get in on their order\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("Oh, they were friends with the performers and had drink tickets! Amazing!\n")
            else:
                print("What are the chances, they're the next performers and told us to tip them ahead of time!\n")
                cash -= 15
        elif flirt == "no" or flirt == "n":
            cash -= 10
            print("So many people makes it intimidating, lets try our luck at another bar.")
        # visits += 1
        venues[0].remove("Rauschgold")

    elif room == "Woof":
        print("""This place seems seedy but it's not that bad. People get much more friendly towards the back, if you know what I mean.""")
        flirt = input("Oh you already made some friends over there? See if you can get them to buy us some drinks.\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("Gulp, that daddy was generous!\n")
            else:
                print("What's with the broke daddies here!\n")
                cash -= 12
        elif flirt == "no" or flirt == "n":
            cash -= 8
            print("Yeah, people here seem kinda shy and not like they'd be open to banter.")
        # visits += 1
        venues[0].remove("Woof")

    elif room != bars:
        print("Uh, we can't go to that bar, one of my exes is a bartender there")

    if cash <= 0:
        print("OMG, we ran out of cash! I'm not even drunk and didn't get to make out with anyone!\nWhatever, lets get some beers at the Späti and go hang out at the park\n" + style.LOSE + "You Lose!" + style.END)
        exit()

    print(f"You have {cash} left")
    
    visits += 1
    if visits < 4:
        room = input("Where do you want to go next?\nWe can go to " + style.BOLD + ", ".join(bars) + style.END + ", or whatever you suggest\n").strip()
    

print("\nI'm so lit and I want to dance! Are you ready for the club?\n")
input("press a key\n")

clearscreen()

room = input("There's a bunch of parties we could go to tonight. I think the good ones are gonna be " + style.BOLD + ", ".join(clubs) + style.END + ", but I'm open to suggestions, it's your choice...\n").strip()

while room not in clubs:
    print("I'm blacklisted from that club... lets just say things got very messy there once...")
    room = input("Lets just go to " + style.BOLD + ", ".join(clubs) + style.END + ", what do you think?\n").strip()

if room == "Schwuz":
    if cash >= 25:
        print("""It's good we had enough to get in. That line was long, but we're finally inside SchwuZ!\nIt's the club! Somehow this intense industrial interior feels like home, right?.""")
    elif cash < 25:
        guest = input("LOL! We spent all our cash at the bars! Let's try to pretend we have guestlist. You're in?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("YAAAS! WE got in! Let's PARTY!!\n")
            else:
                print("Damn, I thought I could get us in, it's worked before. I'm sorry, I guess we'll have to go home... no club for us\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("I get it, this bouncer looks very intimidating. I'm also very drunk, let's call it a night and go home.\n" + style.LOSE + "You Lose!" + style.END)
            exit()

elif room == "Chantal's":
    if cash >= 20:
        print("""It's good we still had some money left. We made it just in time for the show! I mean, the show is mostly Chantal herself slurring on the mic, but that's part of the charm... that, and the debauchery!""")
    elif cash < 20:
        guest = input("Gurl, we're out of money! I think I know a back entrance where we can sneak in. You wanna try?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("See? Pretending you know what you're doing is all you need. Time to party!!\n")
            else:
                print("Oh no! The secret entrance was closed! They must have realized people were sneaking in.\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("Yeah, climbing that rusty fence and jumping over those bushes doesn't seem like the safest. Let's just go.\n" + style.LOSE + "You Lose!" + style.END)
            exit()

elif room == "SO36":
    if cash >= 20:
        print("""Great, we had enough for the cover and some drinks. There's a Drag Queen Pageant tonight! This is gonna be fun! Wooo!!!""")
    elif cash < 20:
        guest = input("Oh No! We don't have enough money, hold on, I think I know that Drag Queen by the door. You want me to try to get us in?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("She's the best! She even gave me a drink ticket! Let's go have fun!\n")
            else:
                print("Oh no! She pretended she doesn't know me!! I'm heartbroken!\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("Yeah this drag queen looks very tall in her heels and huge wig! I'm scared to even approach her.\n" + style.LOSE + "You Lose!" + style.END)
            exit()


print("What a night!! This was so much fun! Lets do it all over again next week, I'm definitely not too old and totally have the energy for this.\n" + style.WIN + "You Win!" + style.END)