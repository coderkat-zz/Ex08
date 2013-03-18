#!/usr/bin/env python

from sys import argv
import random

def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    text_lower = text.lower() 
    list_of_words = text_lower.split()
     # Build dictionary where key = tuple and value = following word
    word_next_dict = {}
    pos = 0

    for word in list_of_words[0:-2]:
        pair = (list_of_words[pos], list_of_words[pos+1])
        if pair not in word_next_dict:
            word_next_dict[pair] = [list_of_words[pos+2]]
            pos += 1
        else:
            word_next_dict[pair].append(list_of_words[pos+2])
            pos += 1
    print word_next_dict
    return word_next_dict

   
def make_text(word_next_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    final_text = []
    # for item in final_text:
    start = random.choice(word_next_dict.keys())
    final_text.append(start[0])
    final_text.append(start[1])

    a = 0
    while a < 10:
        last_words = (final_text[-2], final_text[-1]) 
        next_guy = word_next_dict[last_words][random.randrange(len(word_next_dict[last_words]))] # finds length of wordlist, randomly picks 
        final_text.append(next_guy)
        a += 1
    print ' '.join(final_text)

   

def main():
    args = argv
    script, input_text_1 = args

    # Change this to read input_text from a file
    f = open(input_text_1)
    text = f.read()
    f.close

    word_next_dict = make_chains(text)
    random_text = make_text(word_next_dict)
    #print random_text


   

if __name__ == "__main__":
    main()