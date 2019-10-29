'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):

    the_string = [the_list[0], the_list[-1]]
    return the_string


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
#new_list = the_list[end:beginning:-1]  [start:stop:step]
    if int(end) > int(beginning) :
        the_list = the_list[end-1:beginning-1:-1]
    else:
        raise(ValueError)
    return the_list # hint this is incomplete
#ask about beginning -1

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    the_list.insert(index,index)
    the_list.insert(index,index)
    the_list.insert(index,index)
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    rev = word[::-1]
    if word.lower() == rev.lower():
        return True
    else:
        return False

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence = ''.join(sentence.split())
    rev = sentence[::-1]
    if rev.lower() == sentence.lower():
        return True
    else:
        return False

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
#capital + full stop/questionmark/exclamation
#white space + concatenated sentence in lowercase
def concatenate_sentences(sentence1, sentence2):
    if sentence1[0].islower() or sentence2[0].islower():
        print('capitalise')
        raise ValueError
    elif sentence1[-1] != '.' and sentence1[-1] != '?' and sentence1[-1] != '!':
        print('punctuation error in sentence 1')
        raise ValueError
    elif sentence2[-1] != '.' and sentence2[-1] != '?' and sentence2[-1] != '!':
        print('punctuation error in sentence 2')
        raise ValueError
    else:
        sentence = sentence1 + ' ' + sentence2
    return sentence


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary.keys():
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1
