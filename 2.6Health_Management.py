def getdate():
    import datetime
    return datetime.datetime.now()


def health1():
    """   This function is used to Read & Write Health Management of Entity's   """
    print(health1.__doc__)

    z = int(input("how many times you want read & write"))
    while z:
        c = int(input("What you want to do\nFor log type = 1\nFor read type = 0\n"))
        if c == 1:
            a = int(input("Which you want to choose\nHarry = 1\nRohan = 2\nHammad = 3\n"))
            if a == 1:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Harry's Exercise to log")
                    with open("HarryExe.txt", "a") as c:
                        d = str(input("Enter the exe "))
                        c.write("[" + str(getdate()) + "] " + d + "\n")
                elif b == 0:
                    print("You choose Harry's Food to lock")
                    with open("HarryFood.txt", "a") as e:
                        d = str(input("Enter the food"))
                        e.write("[" + str(getdate()) + "] " + d + "\n")
            elif a == 2:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Rohan's Exercise to lock")
                    with open("RohanExe.txt", "a") as c:
                        d = str(input("Enter the exe"))
                        c.write("[" + str(getdate()) + "] " + d + "\n")
                elif b == 0:
                    print("You choose Rohan's Food to lock")
                    with open("RohanFood.txt", "a") as e:
                        d = str(input("Enter the food"))
                        e.write("[" + str(getdate()) + "] " + d + "\n")
            elif a == 3:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Hammad's Exercise to lock")
                    with open("HammadExe.txt", "a") as c:
                        d = str(input("Enter the exe"))
                        c.write("[" + str(getdate()) + "] " + d + "\n")
                elif b == 0:
                    print("You choose Hammad's Food to lock")
                    with open("HammadFood.txt", "a") as e:
                        d = str(input("Enter the food"))
                        e.write("[" + str(getdate()) + "] " + d + "\n")
        elif c == 0:
            a = int(input("Which you want to choose\nHarry = 1\nRohan = 2\nHammad = 3\n"))
            if a == 1:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Harry's Exercise to read")
                    with open("HarryExe.txt") as c:
                        print(c.read())
                elif b == 0:
                    print("You choose Harry's Food to lock")
                    with open("HarryFood.txt") as e:
                        print(e.read())
            elif a == 2:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Rohan's Exercise to read")
                    with open("RohanExe.txt") as c:
                        print(c.read())
                elif b == 0:
                    print("You choose Rohan's Food to lock")
                    with open("RohanFood.txt", "a") as e:
                        print(e.read())
            elif a == 3:
                b = int(input("Exercise = 1\nFood = 0\n"))
                if b == 1:
                    print("You choose Hammad's Exercise to lock")
                    with open("HammadExe.txt", "a") as c:
                        print(c.read())
                elif b == 0:
                    print("You choose Hammad's Food to lock")
                    with open("HammadFood.txt", "a") as e:
                        print(e.read())


try:
    health1()
except Exception as y:
    print(y)
