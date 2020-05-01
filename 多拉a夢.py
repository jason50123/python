Chinese_zodiac_sign = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon",
                       "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

n = int(input())
if (n>0 and n<37):
    n+=8
    n%=12
    print(Chinese_zodiac_sign[n])
