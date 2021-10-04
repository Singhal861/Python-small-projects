import datetime


class Library:
    def __init__(self, list_of_book, library_name):
        self.list_of_book = list_of_book
        self.name = library_name
        self.lent_books = {}

    def display_book(self):
        for item in self.list_of_book:
            print(f"--{item}")
        return "-----------------------------------------------------------------"

    def add_of_book(self, new_book):
        self.list_of_book.append(new_book)

    def lend_of_book(self, book, user_name):
        if book in self.list_of_book:
            self.lent_books.update({book: user_name + "[" + str(datetime.datetime.now()) + "]"})
            self.list_of_book.remove(book)
            print(f"{book} is lent by {user_name} successfully")
        elif book in self.lent_books:
            print(f"Sorry {book} is already lent by {self.lent_books[book]} & Available books are {self.list_of_book}")
        else:
            print("The book not available in library please print book & choose from it ")

    def return_of_book(self, book):
        self.lent_books.pop(book)
        self.list_of_book.append(book)

    def display_of_lent_book(self):
        print(self.lent_books)


def Main_func():
    """                This Function is for Library Management               """
    print(Main_func.__doc__)
    try:
        n = 1
        Library1 = Library(["TOM", "SOM", "RAC", "FM", "HMT", "THERMODYNAMICS"], "Study")
        # print(Library1.list_of_book)
        while n != 0:
            user_name = input(f"Enter your  name = ")
            print(f"Welcome {user_name} to {Library1.name} Library")
            action = int(input(f"To print Available books press 1\n"
                               f"To Donate the book press 2\n"
                               f"To Lend the book press 3\n"
                               f"To Return the book press 4\n"
                               f"To Print lent book list press secrete code\n = "))
            if action == 1:
                Library1.display_book()

            elif action == 2:
                new_book = input("Enter the book name = ")
                new_book = new_book.upper()
                Library1.add_of_book(new_book)
                with open(Library1.name + ".txt", "a") as f:
                    f.write("Donated by" + user_name + "\n" + str(Library1.list_of_book) + "\n")
                print(f"Thanks for donating {new_book}")

            elif action == 3:
                book = input(f"Enter the name of book = ")
                Library1.lend_of_book(book, user_name)
                with open(Library1.name + ".txt", "a") as f:
                    f.write(str(Library1.lent_books) + "\n")

            elif action == 4:
                book = input(f"Enter the name of book = ")
                book = book.upper()
                # book = book.capitalize()
                Library1.return_of_book(book)
                with open(Library1.name + ".txt", "a") as f:
                    f.write(str(Library1.list_of_book) + "\n")
            elif action == 420:
                Library1.display_of_lent_book()

            else:
                print(f"Some kind of error occurs please try again")

    except Exception as m:
        print(m)


Main_func()
