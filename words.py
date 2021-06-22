#Turn that into a function, print_upper_words. 
#Test it out. (Don’t forget to add a docstring to your function!)

#Change that function so that it only prints words that start with
 #the letter ‘e’ (either upper or lowercase).

#Make your function more general: you should be able to pass in a set of letters,
 #and it only prints words that start with one of those letters.

def print_upper_words(string):
    """turns string arg into uppercase word output"""
    words = string.split(' ')
    for word in words:
        print(word.upper())

def print_upper_e_words(string):
    """turns string arg into uppercase word output for letters starting with 'e' on new line"""
    words = string.split(' ')
    
    for word in words:
        upper_words = word.upper()
        e_words = upper_words.startswith("E")
        if e_words == True:
            print(upper_words)

def print_upper_begins_with(string, letters):
    """prints only words that start with designated letter"""
    words = string.split(' ')
    letters = letters.upper()
    letter = list(letters)
    for word in words:
        upper_word = word.upper()
        for char in letter:
            if upper_word.startswith(char) == True:
                print(upper_word)
