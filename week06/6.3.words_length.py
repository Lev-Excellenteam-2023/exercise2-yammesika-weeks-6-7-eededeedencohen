#====================
# הֲיִי שלום - 6.3
#====================
from check_type_decorator import check_type

#--------------------------
# words_length function:
# get a sentence.
# return a list of words length
#--------------------------
@check_type(str)
def words_length(sentence):
    return [len(word) for word in sentence.split()]

# main program
if __name__ == "__main__":
    print(words_length("Eden Cohen is Awesome"))




