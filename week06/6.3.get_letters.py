#----------------------------------------
# א אוהל, פ זה פייתון - 6.3
#----------------------------------------
from check_type_decorator import check_type


#======================================================
# get_letters function: 
# get a sentence.
# return a list of letters in the sentence - lower case 
#======================================================
""" 
 chr: returns a character from an ascii number.
 ord: returns an ascii number from a character.
"""
@check_type(str)
def get_letters(sentence):
    return [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) in sentence.lower()]

# main program
if __name__ == "__main__":
    print(get_letters("Eden Cohen is Awesome"))



