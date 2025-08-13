class Library:
    name = 'granth'
    books = {'python':5,'java':7,'science':8}
    tbooks = {'python':5,'java':7,'science':8}

    def __init__(self,na,sid):
        self.na = na
        self.sid = sid
        self.bks = {}

    def details(self):
        print(f"total books are {self.books}\nstudent name{self.na}\nstudent id{self.sid}\nstudent has books{self.bks}")

    def borrow(self):
        c = sum(self.bks.values())
        if c<5:
            bn = input(f"Enter the book to borrow for {self.na}:")
            if bn in self.books:
                if bn in self.bks:
                    self.bks[bn]+=1
                else:
                    self.bks[bn]=1
                if self.books[bn]>1:
                    self.books[bn]-=1
                else:
                    self.books.pop(bn)
            else:
                print("library doesn't have the book")
        else:
            print("max book borrowed")

    def ret(self):
        bn = input(f"Enter the book to return {self.na}:")
        if bn in self.bks:
            if bn in self.books:
                self.books[bn]+=1
            else:
                self.books[bn]=1
            if self.bks[bn]>1:
                self.bks[bn]-=1
            else:
                self.bks.pop(bn)
        else:
            print("you don't have the book")

    @classmethod
    def new_book(cls):
        bn=input("Enter the new book to add in library:")
        count=int(input("Enter the no of books to add:"))
        if bn in cls.tbooks:
            cls.tbooks[bn]+=count
        else:
            cls.tbooks[bn]=count
        if bn in cls.books:
            cls.books[bn]+=count
        else:
            cls.books[bn]=count
        print(f'book {bn} of {count} nos is added to library.\ntotal books in library are {cls.tbooks}')

    @classmethod
    def given_books(cls):
        diff = {}
        for i in cls.tbooks:
            if i in cls.books:
                if cls.tbooks[i]>cls.books[i]:
                    diff[i]=cls.tbooks[i]-cls.books[i]
            else:
                diff[i]=cls.tbooks[i]
        print(f"The books given are {diff} ")

mvr=Library('murali',352)
jag=Library('jagadish',346)
mvr.details()
mvr.borrow()
mvr.borrow()
mvr.borrow()
mvr.borrow()
mvr.borrow()
mvr.borrow()
mvr.details()
Library.new_book()
Library.given_books()
jag.borrow()
jag.borrow()
jag.borrow()
jag.borrow()
jag.borrow()
jag.borrow()
jag.details()
Library.given_books()
mvr.ret()
mvr.ret()
mvr.ret()
mvr.ret()
mvr.ret()
mvr.ret()
mvr.details()
Library.given_books()
jag.ret()
jag.ret()
jag.ret()
jag.ret()
Library.given_books()