#-----------------------------
#  חתול ארוך הוא ארוך - 6.3
#-----------------------------

import string

TEXT = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
#===============================================
# count_words function:
# get a text.
# return a dictionary of words and their count.
#===============================================
from check_type_decorator import check_type

@check_type(str)
def count_words(text):
    clean_text = (word.strip(string.punctuation).lower() for word in text.split()) # generator of clean words
    return {word: len(word) for word in clean_text}


# main program
if __name__ == "__main__":
    print(count_words(TEXT))
    




