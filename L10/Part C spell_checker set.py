import time
class SpellChecker:
    def __init__(self):
        self.data_dict = set()



    # load the dictionary of words into the checker
    def load_dictionary(self, filename):
        in_file = open(filename, errors='ignore')
        while True:
            line = in_file.readline()
            if not line:
                break

            # perform some cleanup on the strings and the words.. you can add other filters
            line = line.strip()  # remove any trailing spaces and new line characters
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace("=", "")
            line = line.replace("+", "")
            line = line.lower()
            line_words = line.split(" ")

            for w in line_words:
                self.data_dict.add(w)

    # run a spell checker on the given filename.  Mode is as follows:
    # mode 1: display words not in dictionary
    # mode 2: display statistics about number of words processed, found and not found words
    # mode 1 is helpful when debugging small files.
    def spellcheck(self, filename, mode):
        mywords = []
        found_count = 0
        not_f_count = 0
        # the implementation will be very close to what we did in lab 2.
        in_file = open(filename, errors='ignore')
        while True:
            line = in_file.readline()
            if not line:
                break
            
            # perform some cleanup on the strings and the words.. you can add other filters
            line = line.strip()  # remove any trailing spaces and new line characters
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace("=", "")
            line = line.replace("+", "")
            line = line.lower()
            line_words = line.split(" ")
            
            
            for w in line_words:
                mywords.append(w)

        
        if mode == 1:
            for w in mywords:
                if w not in self.data_dict:
                        print(w)
        if mode == 2:
            print("Number of words processed",len(mywords))
            for w in mywords:
                if  w in self.data_dict:
                    found_count +=1

                else:
                    not_f_count +=1

            print("Number of words found",found_count)
            print("Number of words not found",not_f_count)




sc = SpellChecker()
print("Loading dictionary")
sc.load_dictionary("words_alpha.txt")
print("Processing file")
start = time.time()
sc.spellcheck("alice_wonderland.txt", 2)
stop = time.time()
print(stop-start)
print("done")



