"""
Created on Mon Nov  4 10:27:38 2019

@author: Carlos Villa
"""

from itertools import permutations
import sys

def build_list():
    """ Builds a list of words from a text file.
    
        Assumption: Text file line format is <word>\r\n
        
        fin: text file
        
        returns: list    
    """
    fin = open('words.txt')
    list_of_words = []
    
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    return list_of_words

def in_bisect(words, target):
    """ Determines if element is present in sorted list using
        a binary search. Uses recursion.
        
        words: list
        
        returns: boolean
    """
    if len(words) == 0:
        return False
    
    middle = len(words)//2
    
    if words[middle] == target:
        return True
    
    if target < words[middle]:
        return in_bisect(words[:middle], target)
    else:
        return in_bisect(words[middle+1:], target)
    
def generate_words(dictionary, in_bisect):
    """ Generates a list of possible words of a
        specific size given a string of letters.
        Permutations are compared with elements in
        a dictionary. Throws ValueError exception
        if size is not an integer.
        
        dictionary: list
        
        returns: list
    """
    print('\nHello cheater!')
    letters = input('Enter the 7 letters: ')    
    
    try:
        size = int(input('Enter the length of word (max 7): '))
        print('\n')
        
    except ValueError:
        print('\nYou must enter an iteger!\n')
        sys.exit()
        
    possible_words = []
    for word in permutations(letters, size):
        delimeter = ""
        new_word = delimeter.join(word)
        if in_bisect(dictionary, new_word) and new_word not in possible_words:
            possible_words.append(new_word)  
        
    return possible_words
    
def display(word_list):
    """ Displays the list of possible words
    
        word_list: list
    """
    if not word_list:
        print(f'There are no possible words.')
    else:
        for word in word_list:
            print(word)


def main():
    dictionary = build_list()

    while True:
        
        display(generate_words(dictionary, in_bisect))
        print('\n')
        if input('Try again? (y/n): ') == 'y':
            continue
        else:
            print('\nGoodbye cheater!\n')
            break

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
