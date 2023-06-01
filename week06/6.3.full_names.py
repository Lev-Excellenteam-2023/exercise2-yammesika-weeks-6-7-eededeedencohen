#------------------
# ואלה שמות - 6.3
#------------------

#================================================================
# full_names function:
# get two lists: list of First names and list of Last names.
# get a minimum length of full name.
# return a list of full names that are longer than the minimum length.
#================================================================
def full_names(first_names, last_names,min_length=-1):
    return [f'{first_name.title()} {last_name.title()}'
             for first_name in first_names for last_name in last_names 
             if len(first_name+last_name)+1 >= min_length or min_length == -1] 


# main program
if __name__ == "__main__":
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    min_length = 10
    print(full_names(first_names, last_names,min_length))
    print(f"There are {len(full_names(first_names, last_names,min_length))} full names \n")

    print (full_names(['avi', 'moshe', 'yaakov'], ['cohen', 'levi', 'mizrahi']))
    print(f"There are {len((full_names(first_names, last_names)))} full names")


    








