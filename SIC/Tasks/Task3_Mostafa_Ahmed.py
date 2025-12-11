import string



class library_book():
    def __init__(self,id,name,field,num_papers,writer,publisher, publish_year,is_borrowed,borrowed_price
                 ,rate):
        self.id = id
        self.name = name
        self.field = field
        self.num_papers = num_papers
        self.writer = writer
        self.publisher = publisher
        self.publish_year = publish_year
        self.is_borrowed = is_borrowed
        self.borrowed_price = borrowed_price
        self.rate = rate
        self.review=[]
        self.type_of_review=[]
    def update(self,id,name,field,num_papers,writer,publisher, publish_year,is_borrowed,borrowed_price
                 ,rate):
        self.id = id
        self.name = name
        self.field = field
        self.num_papers = num_papers
        self.writer = writer
        self.publisher = publisher
        self.publish_year = publish_year
        self.is_borrowed = is_borrowed
        self.borrowed_price = borrowed_price
        self.rate = rate
    def show_details(self):
        print(self.id)
        print(self.name)
        print(self.field)
        print(self.num_papers)
        print(self.writer)
        print(self.publisher)
        print(self.publish_year)
        print(self.is_borrowed)
        print(self.borrowed_price)
        print(self.rate)

    def calc_age(self):
        return 2025-self.publish_year
    def add_review(self,review: string,type_of_review:bool):
        self.review.append(review)
        self.type_of_review.append(type_of_review)
    def show_review_details(self):
        print(self.review)
        print(self.type_of_review)


def interface(database:dict):
    choice= input("What do you want to do? choose one of 5 options: \n"
          "1.Add a new Book"
          "\n2.Search about book info"
          "\n3.Show Book Reviews"
          "\n4.Add a review for any book"
          "\n5.Update book info")
    if(choice.isnumeric()):
        if(int(choice)>0 and int(choice)<=5):
            choice_int = int(choice)
            if (choice_int == 1):

                book_id = input("Enter book ID: ")
                name = input("Enter book title: ")
                field = input("Enter field: ")
                num_papers = int(input("Enter number of papers: "))
                writer = input("Enter writer: ")
                publisher = input("Enter publisher: ")
                publish_year = input("Enter publish year: ")
                is_borrowed = int(input("Enter borrowed: "))
                borrowed_price = float(input("Enter borrowed price: "))
                rating = input("Enter rating: ")




                database[book_id] = library_book(book_id,name,field,num_papers,writer,
                                                 publisher,publish_year,is_borrowed,borrowed_price,
                                                 rating)
            elif(choice_int==2):
                book_id = input("Enter book ID: ")
                database[book_id].show_details()

            elif(choice_int==3):
                book_id = input("Enter book ID: ")

                database[book_id].show_review_details()

            elif(choice_int==4):
                book_id = input("Enter book ID: ")
                review = input("Enter review: ")
                type_of_review = input("Enter review type(good or bad): ")
                if (type_of_review == "good"):
                    type_of_review_bool = True
                    database[book_id].add_review(review, type_of_review)
                elif (type_of_review == "bad"):
                    type_of_review_bool = False
                    database[book_id].add_review(review, type_of_review)
                else:
                    print("Please enter a valid review type")
            else:

                book_id = input("Enter book ID: ")
                name = input("Enter book title: ")
                field = input("Enter field: ")
                num_papers = int(input("Enter number of papers: "))
                writer = input("Enter writer: ")
                publisher = input("Enter publisher: ")
                publish_year = input("Enter publish year: ")
                is_borrowed = int(input("Enter borrowed: "))
                borrowed_price = float(input("Enter borrowed price: "))
                rating = input("Enter rating: ")

                database[book_id].update(book_id, name, field, num_papers, writer,
                                                 publisher, publish_year, is_borrowed, borrowed_price,
                                                 rating)

        else:
            print("Sorry not a valid choice")
    else:
        print("Sorry not a valid choice")

