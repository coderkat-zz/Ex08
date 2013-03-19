#!/usr/bin/env python

from sys import argv
#import twitter
import random
#api = twitter.Api(consumer_key='CYZGmsNeiOm47FrCLeZ3rA', consumer_secret='GGqsSqxdSDUdFqBfk3qRzzrv1Khk6Pkdmwrkb2oXo',access_token_key='1278908089-EqHKTzDyF5rtCnaeTiZs1c0LaqNoa80dNHOKpcQ', access_token_secret='oNhP6XbDpd7srl1AQnR9zRsVNu5Wnc83C31W0IU5GzQ')

def make_chains(text, text2):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    list_of_words = text.split() + text2.split()
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

   
def make_text(word_next_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    final_text = []
    # randomly select a tuple from the dictionary
    start = random.choice(word_next_dict.keys())
    # If 1st word in tuple isn't capitalized, choose a new pair until one is
    while not start[0].isupper():
        start = random.choice(word_next_dict.keys())
    # Begin the list of random text with tuple (separated to 2 strings)
    final_text.append(start[0])
    final_text.append(start[1])

    # create random text list: find a word associated with last 2 and append list
    while len(final_text) < 12:
        if '.' in final_text[-1]:
            while not start[0].isupper():
            #     start = random.choice(word_next_dict)
            # final_text.append(start)
        last_words = (final_text[-2], final_text[-1]) 
        next_guy = word_next_dict[last_words][random.randrange(len(word_next_dict[last_words]))] # finds length of wordlist, randomly picks 
        final_text.append(next_guy)

    to_tweet = ' '.join(final_text)
    print to_tweet
    return to_tweet

# def twitter(to_tweet):
#     status = api.PostUpdate(to_tweet)
#     print status.text    
   

def main():
    args = argv
    script, input_text_1, input_text_2 = args

    # Change this to read input_text from a file
    f = open(input_text_1)
    text = f.read()
    f.close

    f2 = open(input_text_2)
    text2 = f2.read()
    f2.close

    word_next_dict = make_chains(text, text2)
    to_tweet = make_text(word_next_dict)
    # tweet = twitter(to_tweet)




if __name__ == "__main__":
    main()