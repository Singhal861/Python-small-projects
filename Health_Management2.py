list1 = {1:"Harry", 2:"Rohan", 3:"Abhishek"}
list2 = {1:"Exercise", 2:"Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()

print(__name__)
if __name__ == '__main__':

    try:
        for key, value in list1.items():
            print("Press", key, "For", value, "\n", end="")
        Client = int(input("Your choise= "))
        print("Selected client: ", list1[Client], "\n")
        Action = int(input("For log press 1\n" + "For retrive press 2\n"))
        if Action == 1:
            for key, value in list2.items():
                print("Press", key, "For log", value, "\n", end="")
            tp = int(input())
            k = "y"
            while (k != "n"):
                with open(list1[Client] + list2[tp] + ".txt", "a") as H:
                    H1 = input(list2[tp] + "=")
                    H.write("[" + str(getdate()) + "]" + H1 + "\n")
                k = input("Add more ? y/n")
                continue
        elif Action == 2:
            for key, value in list2.items():
                print("Press", key, "For retrive", value, "\n", end="")
            tp = int(input())
            with open(list1[Client] + list2[tp] + ".txt") as H:
                print(H.read())
        else:
            print("invalid input")
    except Exception as e:
        print(e)