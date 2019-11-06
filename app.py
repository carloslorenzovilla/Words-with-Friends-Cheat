"""
Created on Mon Nov  4 10:27:38 2019

@author: Carlos Villa
"""

from itertools import permutations
import sys

def build_dict():
    """ Builds a list of words in a text file.
    
        Assumption: Text file line format is <word>\r\n
        
        fin: text file
        
        returns: list    
    """
    fin = open('words.txt')
    dict_of_words = {}
    
    for line in fin:
        word = line.strip()
        dict_of_words[word] = 1
    return dict_of_words
    
def generate_words(dictionary):
    """ Generates a list of possible words of a
        specific size given a string of letters.
        Permutations are compared with elements in
        a dictionary. Throws ValueError exception
        if size is not an integer.
        
        dictionary: dict
        
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
        if new_word in dictionary:
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
    dictionary = build_dict()

    while True:
        
        display(generate_words(dictionary))
        print('\n')
        if input('Try again? (y/n): ') == 'y':
            continue
        else:
            print('\nGoodbye cheater!\n')
            break

if __name__ == "__main__":

    main()
