import json
import os
data_file='library.txt'
def lode_library():
    if os.path.exists(data_file):
        with open(data_file,'r')as file:
            return.json.load(file)
            return[]
 def save_library(library)
            with _open(data_file,'w')as file:
                jeson.dump(library,file):
 def _add_book (library)
            title= input('Enter the title of the book:')
            author=input('Enter the author of the book:')
            year=input('Enter the year of the book:')
            gener=input('Enter the gener of the book:')
            read=input('have you read the book(yes/no)')lower()==yes
            new_book={
              'title': title,
             ' author':author
             ' year': year,
             ' gener': gener,
              'read': read,
            }
            library.append(new_book)
            save_library(library)
            print(f'book {title}added successfully.')
 def remove_book(library)
            title= input('Enter the title book to remove from the library:')
            initail_length=len(library)
            library=[book for book in library if book['title'].lower()!=title]
            if len (library)<initail_length:
              save_library(library) 
               print(f'book {title}remove successfully.')
             else :
                print(f'book {title}not found in the library'.) 

def search_library (library)
            search_by=input('search by the title or by author').lower()
             search_trem=input(f'Enter the {search_by} ').lower()
            result=[book for book in library if search_trem in book{earch_by}]
            if result:
                for book in result
                status="Read"if book['read'] else "unread"
                print(f"{book['title']}by{ book['author']}"-{book['year']}-{book['gener']})-{'status'}
            else:
                   print("library is empty")

def dispaly_statistics(library)
             total_books=len(library)
             read_books=len(book for book in library if book read['read'])
             percentage_read=(read_books/total_books)*100 if total_books>0 else 0
             print(f"total books:{total_books}")
             print(f"percentage read:{percentage_read:.2f}%")
def main():
              library:lode_library()
              while true:
                print("manu")
                print("1.Add a book")
                print("2.Remove a book")
                print("3.serch the library")
                print("4.Display all books")
                print("5.Disply statistics")
                print("6.Exit")
                choice= input("Enter your choice")
                if choice =='1':
                  add_book =(library)
                elif choice =='2':
                         remove_book=(library)
                  elif    choice =='3':
                         serch_book=(library)
                    elif choice =='4':
                          Display_all books =(library)
                    elif choice =='5':
                          Disply_statistics =(library)
                    elif choice =='6':
                          print   =("Good by !")
                          Break
                      else:
                       print ("invalid choice,please try again")
         if __name__=='__main__ ' 
         main():          


                       
                    



                  





                








