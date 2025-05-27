class Library:
    def _init_(self,book_list):
        self.books=book_list

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")

    def borrow_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\nYou have borrowed '{book_name}'")
        else:
            print(f"\n Sorry, '{book_name}' is not available.")

    def return_book(self,book_name):
        self.books.append(book_name)
        print(f"\n Thanks for returning '{book_name}'")


class User:
    def request_book(self):
        return input("Enter the book name you want to borrow")
    
    def return_book(self):
        return input("Enter the book name you want to return:")
    
library = Library(["1984","To Kill a Mocking Bird"," The Great Gatsby","Harry Potter"])
user=User()

while True:
    print("\n ----Library Menu----")
    print("1.Display available Books")
    print("2.Borrow a Book")
    print("3.Return a Book")
    print("4.Exit")

choice=input("Enter you choice(1-4):")

if choice =="1":
    library.display_books()

elif choice=="2":
    book=user.request_book()
    library.borrow_book(book)

elif choice=="3":
    book=user.return_book()
    library.return_book(book)

elif choice=="4":
    print("\n Thanks for using the library.Goodbye!")


else:
print("Invalid Choice. Try Again")