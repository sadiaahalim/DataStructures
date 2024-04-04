from linked_list import LinkedList


class BookGenre:
    def __init__(self):
        self.all = LinkedList()
        self.fiction = LinkedList()
        self.book_itr = None
        self.genretemp = []
        self.genreList = []
        self.rm_fic = []
    
    def add_book(self,title,author,genre):

        self.all.insert_back({"Title":title, "Author":author, "Genre":genre})
        if genre == "fiction":
            self.fiction.insert_back({"Title":title, "Author":author, "Genre":genre})
        self.book_itr = self.all.get_iterator()


    def current_book(self):
        return self.book_itr.current_value()["Title"]

    def next_book(self):
        if not self.book_itr.has_next():
            self.book_itr = self.all.get_iterator()
            return self.book_itr.current_value()["Title"]
        self.book_itr.next()

    def all_books(self):
        self.itr = self.all.get_iterator()
        ptr = self.itr
        while self.itr.has_next():
            self.genretemp.append(ptr.current_value()['Genre'])
            ptr.next()
        self.genretemp.append(ptr.current_value()['Genre'])
        
        for x in self.genretemp:
            if x not in self.genreList:
                self.genreList.append(x)
        
        return self.genretemp
        
    def remove_fiction_books(self):
        self.itr = self.all.get_iterator()
        ptr = self.itr
        
        while self.itr.has_next():
            if ptr.current_value()['Genre'] != "fiction":
                self.genretemp.append(ptr.current_value()['Genre'])
            else:
                self.rm_fic.append(ptr.current_value()['Genre'])
            ptr.next()
        self.genretemp.append(ptr.current_value()['Genre'])
        return self.genretemp
    
    def fiction_books(self):
        temp = []
        self.itr = self.all.get_iterator()
        ptr = self.itr
        while self.itr.has_next():
            temp.append(ptr.current_value()['Title'])
            ptr.next()

        
        temp.append(ptr.current_value()['Title'])
        return temp

    ##Count no. of book each genre has
    def count_gen_books(self,genre):
        counter = 0
        self.itr = self.all.get_iterator()
        while self.itr.has_next():
            if self.itr.current_value()['Genre'] == genre:
                counter += 1
            self.itr.next()
        if self.itr.current_value()['Genre'] == genre:
            counter += 1
        return counter


    #Change null to unknowns
    def modify_author(self):
        self.itr = self.all.get_iterator()
        counter = 0
        while self.itr.has_next():
            if self.itr.current_value()['Author'] == "":
                self.itr.current_value()['Author'] = "Unknown"
                counter += 1
            self.itr.next()
        if self.itr.current_value()['Author'] == "":
            self.itr.current_value()['Author'] = "Unknown"
            counter += 1
        return counter , str("Unkowns Modified")
        
    def debug(self):
        pass
        
            
    
bk = BookGenre()
f = open("book.csv")
for x in f:
    line = x.strip("\n")
    line = line.split(",")
    bk.add_book(line[0],line[1],line[2])
    
bk.all_books()
for x in bk.genreList:
    print(bk.count_gen_books(x), x)
##print(bk.genre)
##print(bk.current_book())
##bk.next_book()
##print(bk.current_book())
##print(bk.fiction_books())
##bk.debug()
##print(bk.modify_author())

##bk.debug()

