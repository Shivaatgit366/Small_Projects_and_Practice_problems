# Project: To create an “Online Library Management System”.
# For this, you have to create a library class which includes the following methods:

# Displaybook() : To display the available books
# Lendbook(): To lend a book to a user
# Addbook(): To add a book in the library
# Returnbook(): To return the book in the library.

# After creating a library class, create an object and pass the following parameters in the constructor.
# HarryLibrary=Library(listofbooks, library_name)

# create a main function and run an infinite while loop which asks the users for their input.

# Optional:-
# Maintain a dictionary for the users who own a book.
# Dictionary should take book name as a key and name of the person as a value.
# Whenever you lend a book to a user, you should maintain a dictionary.

# -------------*----------------------*--------------------*-------------------------*-------------------------*------

# Solution for the project
class Library:
    def __init__(self, booklist, personname):
        self.booklist = booklist
        self.personname = personname
        self.lentbooks = {}  # this is a dictionary which has details of lent books and persons.

    def displaybooks(self):
        print(f"The available books in the library are")
        for book in self.booklist:
            if book in self.lentbooks:
                continue
            else:
                print(book)  # this command prints all the books in the object's booklist.


    def lendbook(self, bookname, username): # this function is about to lend the books to users.
# If the book is not present in "self.lentbooks" dictionary, then only book will be lend/given to someone.

        if bookname not in self.lentbooks.keys():
            self.lentbooks.update({bookname: username}) # update function updates key value pair in lentbooks.
            print("OK, Book and the Lender database has been updated, "
                  "now the book will be lend to you by librarian")
        else:  # if the same book is present in lentbooks dictionary, then person name should be displayed.
            print(f"sorry, this book has been already lent/given to {self.lentbooks[bookname]}")

    def addbook(self, book): # if any book is donated to the library, it should be added to original book list.
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lentbooks.pop(book)
        print(f"{book} has been returned")

if __name__ == '__main__': # the above class can be used anywhere, so, below code is written in main function.
    shivalibrary = Library(["Python", "Rich Daddy Poor Daddy", "Javascript", "R language", "Basic algorithms",
                            "How to cook healthy dishes"], "shivahegde")
    while(True):  # this means an infinite while loop, until the process becomes true, iterations will be done.
        print(f"Hello {shivalibrary.personname} welcome to the library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend/Give a Book from the library to the person")
        print("3. Add a Book")
        print("4. Return the Book")
        choice_of_user = int(input())

        if choice_of_user not in [1, 2, 3, 4]:
            print("Please enter a valid input")
            continue
        else:
            choice_of_user = int(choice_of_user)

        if choice_of_user == 1:
            shivalibrary.displaybooks()
        elif choice_of_user == 2:
            book = input("Enter the name of the book you want to take from the library\n")
            user = input("Enter your name\n")
            shivalibrary.lendbook(book, user)
        elif choice_of_user == 3:
            book = input("Enter the name of the book you want to donate to the library\n")
            shivalibrary.addbook(book)
        elif choice_of_user == 4:
            book = input("Enter the name of the book you want to return back to the library\n")
            shivalibrary.returnbook(book)
        else:
            print("Not a valid option")

        choice_of_user2 = input("Press q to quit and c to continue\n")

        while (choice_of_user2 != "q" and choice_of_user2 != "c"):
            if choice_of_user2 == "q":
                exit()
            if choice_of_user2 == "c":
                continue


# --------------*------------------------*--------------------------------*----------------------------------*-------
