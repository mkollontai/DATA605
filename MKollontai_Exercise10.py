# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:35:40 2020

Exercise 8 on page 452 of Introduction to Probability

Write a program to play the game in Exerise 7.

---

**Exercise 7**. Here is a trick to try on your friends. Shuffle a deck of cards
and deal them out one at a time. Count the face cards each as ten. Ask your 
friend to look at one of the first ten cards; if this card is a six, she is to
look at the card that turns up six cards later; if this card is a three, she is
to look at the card that turns up three cards later, and so forth. Eventually
she will reach a point where she is to look at a card that turns up x cards
later but there are not x cards left. You then tell her the last card that
she looked at even though you did not know her starting point. You tell her
you do this by watching her, and she cannot disguise the times that she looks
at the cards. In fact you just do the same procedure and, even though you do
not start at the same point as she does, you will most likely end at the same
point. Why?

@author: Misha Kollontai
"""
import random, collections, itertools

#----------------------------------------------------------------------------
class Card:
#Taken almost verbatim from Think Python: How to Think Like a 
#Computer Scientist 2nd Edition
    
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
        #Added the value of each rank. Face cards are 10
        self.rank_val = self.rank_value[rank]
        
    suit_names = ['Spades','Hearts','Clubs','Diamonds']
    rank_names = [None, 'Ace', '2', '3', '4' ,'5' ,'6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    rank_value = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], 
                             Card.suit_names[self.suit])
#----------------------------------------------------------------------------        
class Deck:
#Baseline code taken from Think Python: How to Think Like a 
#Computer Scientist 2nd Edition
        
#Adjusted to shuffle on initiation, added the method for playing our game
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit,rank)
                self.cards.append(card)
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def play_game(self):
        #shuffle deck again to ensure a proper mix
        self.shuffle()
        results = []  #instantiate an empty list
        for i in range(1,11):   
            #loop to account for each of the possible starting cards
            n = i #the number of cards to be pulled
            counter = i #total cards pulled
            
            while (counter <= len(self.cards)):
                #loop to keep pulling until we don't have enough cards
                card_now = self.cards[-counter]
                n = card_now.rank_val
                counter = counter + n
            #The 'card_now' owuld be the last card chosen before the deck
            #had fewer cards than the value of the rank of the pulled card
            results.append(card_now)
        return results
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

def Single_check():
    deck = Deck() #generate a Deck() object
    results = deck.play_game()
    
    #For this particular shuffle, print the rusult for starting at 
    #each of the first 10 cards
    
    for i in range(0,10):
        print("If I start at card ",i+1," I would end up at the ",results[i])

#----------------------------------------------------------------------------
#Repeat thecheck abve 1
def Overall_frequency(n):
    random.seed(123)
    deck = Deck()
    breakdown=[]
    for _ in itertools.repeat(None, n):
        freq = collections.Counter(deck.play_game())
        a=[*freq.values()]
        breakdown.append(str(sorted(a)))
    
    freq={}
    for i in breakdown:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True):
        print("{} : {:.2%}".format(key, value/n))
    
    #print(breakdown)
    #print("\nThe set is:\n")
    #summary = collections.Counter(breakdown)
    #print((set(breakdown))
    

Single_check()
print ("\nAs we can see, most paths lead to the same final card. \n\nLet's repeat this exercise multiple times and see how \nreproducible it is\n")
print("\nThe list below shows how often each breakdown of final locations happened in our simulation.")
print("\n[10] signifies that all 10 starting cards led to the same card. \n[1, 9] signifies that 9 of the first 10 cards led to the same result and one of them yielded something different.\n\nAnd so forth.\n")
Overall_frequency(10000)
print("\nHaving seeded this particular simulation, we can see that \nin around 28% of cases any path you follow leads to the same card.")
print("\nThis may not seem all that high until you realize that \nin 28+13+12+12+11 = 76% of cases there are only 2 options, \nwith at least 6 of them being the same result.")