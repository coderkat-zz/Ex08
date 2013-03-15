#!/usr/bin/env python

from sys import argv
import random

def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    list_of_words = text.split()
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

    return word_next_dict

   
def make_text(markov_words):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    final_text = []

    start = random.choice(markov_words.keys())
    final_text.append(start)
    next_guy = markov_words[start][random.randrange(len(markov_words[start]))] # finds length of wordlist, randomly picks 
    final_text.append(next_guy)

    a = 0
    while a < 6:
        next_guy_1 = markov_words[final_text[-2:]][random.randrange(len(markov_words[next_guy]))]
        final_text.append(next_guy_1)
        a += 1
    print final_text

# .join turns list into string

 #   return "Here's some random text."
    

def main():
    args = argv
    script, input_text = args

    # Change this to read input_text from a file
    f = open(input_text)
    text = f.read()
    f.close

    markov_words = make_chains(text)
    random_text = make_text(markov_words)
    #print random_text


   

if __name__ == "__main__":
    main()