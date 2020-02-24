on = true
Books["Eregon","dawn of man","a game of gods"]
while on = true:
    #start of code
    print("select wanted function")
    print("1 for invertry  2 to search the list  3 to add to the list  4 to remove from the list  5 to close peogam")
    number choice=int(input())
    word=(input())
    if number choice=(1):
        print(Books)
    if number choice=(2):
        print("enter name of book")
        if word in Books:
            print("the book is in the invertory") 
    if number choice=(3):
        add = (input())
        Books.append(add)
        print(Books) 
    if number choice=(4):
        
    if number choice=(5):
        set on = false
    