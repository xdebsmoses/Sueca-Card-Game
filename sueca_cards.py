#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:17:39 2022

@author: deborahmosesalabi
"""
from sueca_suits_ranks import rank_points, rank_higher_than, valid_suit, valid_rank
#creating a custom exception
class CardInvalid(Exception):
    def __init__(self, cs, msg =""):
        self.card = cs
        self.message = ("Card '%s' invalid! \n %s"%(self.card, msg))
        super().__init__(self.message)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit        
        
    def points(self):           
        return rank_points(self.rank)
        
    def higher_than(self, other,s,t):
        #comparing them if they are the same suit
        if self.suit == other.suit:
            return rank_higher_than(self.rank, other.rank)
        #comparing them if first card has the same lead suit 
        if self.suit == s and other.suit != s and other.suit != t:
            return True
        #comparing them if first card has the same lead suit 
        elif self.suit == t and other.suit != t:
            return True
        else:
            return False
            
    def show(self):
        return self.rank + self.suit

        
def parseCard(cs):
    r = cs[0]
    s = cs[1]
    if len(cs)>2:
        raise CardInvalid(cs, msg="A card string representation must contain 2 characters only")
    elif not(valid_rank(r)):
        raise CardInvalid(cs, msg = "Invalid rank symbol: %s" %cs[0])
    elif not(valid_suit(s)):
        raise CardInvalid(cs, msg = "Invalid suit symbol: %s" %cs[1])
    else:
        return Card(cs[0],cs[1])

