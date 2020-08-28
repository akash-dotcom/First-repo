
print(
    "///////////////****************//////////////*****************/////////////////*****************///////////////////******************//////////")
print(
    "----------------------------------------------------- WELCOME TO AKGEC CENTRAL LIBRARY -----------------------------------------------------------------")
print(
    "//////////////****************///////////////*****************/////////////////*****************///////////////////******************//////////")

print("Welcome to the Online Library Portal")
print("Enter your Name")
name = input("Name:")
print("Enter your student number")
studentnumber = int(input("student number is:"))



class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.issueDict = {}
        

    def Availablebooks(self):
        print(f"The following books are available in the library: {self.name}")
        for book in self.booksList:
            print("-->", book)

    def issueBook(self, user, book):
        if book not in self.issueDict.keys():
            self.issueDict.update({book: user})
            print("The book is issued to you")
        else:
            print("Sorry! Someone else has already issued that book")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the list")

    


if __name__ == '__main__':
    akgec = Library(['NP Bali', 'Javascript', 'Harry Potter',
                     'Python', 'Naruto'], "AKGEC Central Library")
while(True):

    print("Enter your choice to continue")
    print("1)Display Books")
    print("2)Issue a Book")
    print("3)Add a Book")

    choice = int(input("Your choice here:"))

    if choice == 1:
        akgec.Availablebooks()
    elif choice == 2:
        book = input("Enter the name of the book you want to issue:")
        user = input("Enter your name:")
        akgec.issueBook(user, book)
    elif choice == 3:
        book = input("Enter the name of the book you want to add:")
        akgec.addBook(book)
    
    else:
        print("Please enter a valid choice")

    print("Press q to quit and c to continue")

    choice2 = " "
    while(choice2 != "c" and choice2 != "q"):
        choice2 = input()
        if choice2 == "q":
            exit()
        elif choice2 == "c":
            continue
