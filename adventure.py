import random

class style:
   LOSE = "\033[1m" + "\033[41m"
   WIN =  "\033[1m" + "\033[42m"
   BOLD = "\033[1m"
   END = "\033[0m"


venues = [["Roses", "Olfe", "Südblock", "Silverfuture", "Rauschgold", "Woof", "Tipsy Bear"] ,["Schwuz","Chantal's", "SO36"]]
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
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
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
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
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
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
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
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
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
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
        # visits += 1
        venues[0].remove("Rauschgold")

    elif room == "Woof":
        print("""You plop down on a sofa in Silverfuture.\nA very nice comfy bar where you can have some cocktails without a worry about who you are, or what your drink choice is... Why not get that Raspberry Daiquiri?""")
        flirt = input("Omg, people are looking at you like they like you, maybe someone will buy you a drink!\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("OMG! Free drinks! YAY!\n")
            else:
                print("Oh well, maybe in the next place\n")
                cash -= 12
        elif flirt == "no" or flirt == "n":
            cash -= 12
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
        # visits += 1
        venues[0].remove("Woof")

    elif room == "Tipsy Bear":
        print("""You plop down on a sofa in Silverfuture.\nA very nice comfy bar where you can have some cocktails without a worry about who you are, or what your drink choice is... Why not get that Raspberry Daiquiri?""")
        flirt = input("Omg, people are looking at you like they like you, maybe someone will buy you a drink!\nFlirt? (Yes/No)\n").lower().strip()
        if flirt == "yes" or flirt == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("OMG! Free drinks! YAY!\n")
            else:
                print("Oh well, maybe in the next place\n")
                cash -= 12
        elif flirt == "no" or flirt == "n":
            cash -= 12
            print("Don't worry, maybe we can try in the next place after we loosen up a little")
        # visits += 1
        venues[0].remove("Tipsy Bear")

    elif room != bars:
        print("Uh, we can't go to that bar, one of my exes is there")

    if cash <= 0:
        print("OMG, we ran out of cash! I'm not even drunk and didn't get to make out with anyone!\nWhatever, lets get some beers at the Späti and go to the park\n" + style.LOSE + "You Lose!" + style.END)
        exit()

    print(f"You have {cash} left")
    
    visits += 1
    if visits < 4:
        room = input("Where do you want to go next?\nWe can go to " + style.BOLD + ", ".join(bars) + style.END + ", or whatever you suggest\n").strip()
    


print("\nI'm so lit and I want to dance! Are you ready for the club?\n")
input("press a key\n")

room = input("There's a bunch of parties we could go to tonight. I think the good ones are gonna be " + style.BOLD + ", ".join(clubs) + style.END + ", but I'm open to suggestions, it's your choice...\n").strip()

while room not in clubs:
    print("I'm blacklisted from that club, once I got very messy there")
    room = input("Lets just go to " + style.BOLD + ", ".join(clubs) + style.END + ", what do you think?\n").strip()

if room == "Schwuz":
    if cash >= 25:
        print("""The line was long, but we're finally inside SchwuZ!\nIt's the club! Somehow this intense industrial interior feels like home, right?.""")
    elif cash < 25:
        guest = input("LOL! We spent all our cash at the bars! Let's try to pretend we have guestlist. You're in?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("YAAAS! WE got in!\n")
            else:
                print("Damn, I thought I could get us in, it's worked before. I'm sorry, I guess we'll have to go home... no club for us\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("I get it, this bouncer looks very intimidating. I'm also very drunk, let's call it a night and go home.\n" + style.LOSE + "You Lose!" + style.END)
            exit()

elif room == "Chantal's":
    if cash >= 20:
        print("""A seasoned drag queen is slurring something into the mic that nobody seems to be paying attention to. It's a rowdy crowd that wants to party and make a mess.""")
    elif cash < 20:
        guest = input("LOL! We spent all our cash at the bars! Let's try to pretend we have guestlist. You're in?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("YAAAS! WE got in!\n")
            else:
                print("Damn, I thought I could get us in, it's worked before. I'm sorry, I guess we'll have to go home... no club for us\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("I get it, this bouncer looks very intimidating. I'm also very drunk, let's call it a night and go home.\n" + style.LOSE + "You Lose!" + style.END)
            exit()

elif room == "SO36":
    if cash >= 20:
        print("""The line was long, but you're finally inside SchwuZ!\nIt's the club! Somehow this intense industrial interior feels like home to you. ...""")
    elif cash < 20:
        guest = input("LOL! We spent all our cash at the bars! Let's try to pretend we have guestlist. You're in?\n").lower().strip()
        if guest == "yes" or guest == "y":
            chance = random.choice([True, False])
            if chance == True:
                print("YAAAS! WE got in!\n")
            else:
                print("Damn, I thought I could get us in, it's worked before. I'm sorry, I guess we'll have to go home... no club for us\n" + style.LOSE + "You Lose!" + style.END)
                exit()
        else:
            print("I get it, this bouncer looks very intimidating. I'm also very drunk, let's call it a night and go home.\n" + style.LOSE + "You Lose!" + style.END)
            exit()



print("What a night!! This was so much fun! Lets do it all over again next week, I'm definitely not too old and totally have the energy for this.\n" + style.WIN + "You Win!" + style.END)