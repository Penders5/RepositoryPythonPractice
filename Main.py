def highLow(x):

    if x > 10:
        return "High!"
    elif x == 10:
        return "Good ammount"
    else: 
        return "Low..."


def equalsTen(x):
    if x == 10:
        return "x equals 10!"

    elif x < 10:
        return "x is less than 10..."

    else:
        return "x is greater than 10!"

def define(word):
    word = word.lower()
    if word == "bat":
        return "Bat: A stick used in baseball that hits a ball"
    elif word == "desert":
        return "Desert: To abandon someone or something"
    elif word == "fair":
        return "Fair: Someone who has light skin or hair"
    elif word == "lie":
        return "Lie: Lay down"
    elif word == "lead":
        return "Lead: A very dense metal"
    elif word == "minute":
        return "Minute: Something small"
    elif word == "refuse":
        return "Refuse: Garbage"
    elif word == "project":
        return "Project: To plan something"
    elif word == "fine":
        return "Fine: Payment for a vialation"
    elif word == "entrance":
        return "Entrance: to bewitch or delight"
    else:
        return "Cannot define"

print(define("bat"))