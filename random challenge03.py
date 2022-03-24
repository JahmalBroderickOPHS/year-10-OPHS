import random
ht = ["Heads", "Tails"]
coin = random.choice(ht)
guess = str(input("Heads or Tails"))
if coin == guess:
    print("you win")
else:
    print("bad luck")
    print("it was" + coin)
