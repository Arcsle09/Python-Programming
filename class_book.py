class book:
    def __init__(self):
        self.bookid = int(input('Enter the bookid: '))
        self.title = (input('Enter the book title: '))
        self.price = eval(input('Enter the price: '))   
        self.author = input('Enter the author name: ')
        self.publisher = input('Enter the publisher name: ')
        
# will add the new book details to book_list         
    def append_data(self):
         book_list.append(self.bookid)
         book_list.append(self.title)
         book_list.append(self.price)
         book_list.append(self.author)
         book_list.append(self.publisher)

#will show or update the book price 
    def book_price(show = True,price_change=False):
        t = list(chunks(book_list,5))
        if show == True:
            for i in range(n):
                print('Book Title:',t[i][1],'Price: ',t[i][2])
        elif price_change == True:
            book_search = input('Enter the title of book to change its price: ')
            for i in range(n):
                while book_search == t[i][1]:
                    t[i][2] = input('Enter the new price:')
                    break
            else:
                print('Sorry!, The book name did not match!')
        print('current book_list : ',t)

#will sort the books by Title or Price     
    #create chunks of sublists from original list. 
    def sort_book(byTitle = False, byPrice = False):
        if byTitle == True:
            print('The sorted book_list by title:')
            sorted_books_by_title = sorted(list(chunks(book_list,5)), key = lambda x: x[1])
            print(sorted_books_by_title)
        elif byPrice == True:
            print('The sorted book_list by price:')      
            sorted_books_by_price = sorted(list(chunks(book_list,5)),key = lambda x: x[2])
            print(sorted_books_by_price)       
        else:
            print('The sorted book_list by title:')
            sorted_books_by_title = sorted(list(chunks(book_list,5)), key = lambda x: x[1])
            print(sorted_books_by_title)
            print('The sorted book_list by price:')      
            sorted_books_by_price = sorted(list(chunks(book_list,5),reverse=True),key = lambda x: x[2])
            print(sorted_books_by_price) 
        

#entering the number of books records
n = int(input('how many employee data you would like to record?')) 

#initializing the list of books details
book_list = []        

#creating the list of variables to be assigned during instantiation of class
obj = ["obj_%d" % x for x in range(n)] 

#creates objects and produces the list of books data 
for i in range(n):
    print('Enter the details of a book - ',i+1)
    obj[i] = book()
    obj[i].append_data()

def chunks(l, n):
    # For item i in a range that is a length of l
    for i in range(0, len(l), n):
    # Create an index range for l of n items:
        yield l[i:i+n] 
                
book_by_title = book.sort_book(byTitle = True)
 
book_by_price = book.sort_book(byPrice = True)

show_price = book.book_price()

change_price = book.book_price(show = False,price_change=True)
