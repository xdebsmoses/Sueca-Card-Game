#!/usr/bin/env python3 Ace, Seven, King, Jack, Queen, Six, Five, Four, Three, Two
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:16:31 2022

@author: deborahmosesalabi
"""

#checking if the suit is valid 
def valid_suit(s):
    suit = ['D', 'H', 'C', 'S']
    if s in suit:
       return True 
    else:
       return False 
#checking if the rank is valid
def valid_rank(r):
    rank = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
    if r in rank:
       return True 
    else:
       return False 
#outputting the full name of a suit
def suit_full_name(s):
    if s == 'D':
        return "Diamonds"
    elif s == 'H':
        return "Hearts"
    elif s == 'C':
        return "Clubs"
    elif s == 'S':
        return "Spades"
    else :
        raise ValueError("Invalid suit symbol: %s " + s)
#ranking the suits 
def rank_points(r):
    others = ['2', '3', '4', '5', '6']
    if r in others:
        return 0
    elif r == 'A':
        return 11
    elif r == '7':
        return 10
    elif r == 'K':
        return 4
    elif r == 'J':
        return 3 
    elif r == 'Q':
        return 2
    else:
        raise ValueError ('Invalid rank symbol: %s' %r)
#comparing the ranks

def rank_higher_than(r1,r2):
    ranks = ['2', '3', '4', '5', '6', 'Q', 'J', 'K', '7', 'A']
    
    if not (valid_rank(r1)):
        raise ValueError ('Invalid rank symbol: %s' %r1)
    
    if not (valid_rank(r2)):
        raise ValueError ('Invalid rank symbol: %s' %r2)
    
    return ranks.index(r1) > ranks.index(r2)
        
 
