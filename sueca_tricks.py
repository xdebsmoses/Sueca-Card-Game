#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:35:14 2022

@author: deborahmosesalabi
"""
from sueca_cards import parseCard, Card
class Trick:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
    #getting the points from the sueca_cards    
    def points(self):
        return self.c1.points() + self.c2.points() + self.c3.points() + self.c4.points()
    #getting the show from the sueca_cards      
    def show(self):
        return self.c1.show() + ' ' + self.c2.show () + ' ' + self.c3.show() + ' ' + self.c4.show()  
    
    def trick_winner(self, t):
        #comparing the first two cards with the same suit as the trump
        ls = self.c1.suit
        if self.c4.higher_than(self.c2, ls, t) and self.c4.higher_than(self.c3, ls, t) and self.c4.higher_than(self.c1, ls, t):
         return 4
        elif self.c3.higher_than(self.c2, ls, t) and self.c3.higher_than(self.c1, ls, t) and self.c3.higher_than(self.c4, ls, t):
         return 3
        elif self.c2.higher_than(self.c1, ls, t) and self.c2.higher_than(self.c3, ls, t) and self.c2.higher_than(self.c4, ls, t):
         return 2
        elif self.c1.higher_than(self.c2, ls, t) and self.c1.higher_than(self.c3, ls, t) and self.c1.higher_than(self.c4, ls, t):
         return 1
        
def parseTrick(ts):
    cards = ts.split(' ')
    if len(cards) != 4:
        raise ValueError (" A trick string must comprise four cards only; the given trick is: %s" %ts)
    #puts each of the split cards into the function  requierments of sueca_cards
    c1 = parseCard(cards[0])
    c2 = parseCard(cards[1])
    c3 = parseCard(cards[2])
    c4 = parseCard(cards[3])
    return Trick(c1, c2, c3, c4)

def parseGameFile(fname):
    tricks = []
    i = 1

    f = open (fname, 'r')
    for line in f:
        if (line[-1] == '\n'):
            data = line[:-1]
        else:
            data = line
        if i == 1:
            trump = parseCard(data)
        else:
            t = parseTrick(data)
            tricks.append(t)
        i+=1
    f.close()
    return trump,tricks

