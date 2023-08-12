#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:07:29 2022

@author: deborahmosesalabi
"""

class CardAlreadyPlayed(Exception):
    def __init__(self, cs, msg =""):
        self.card = cs
        self.message = ('Card is already played \n %s'%(self.card + msg))
        super().__init__(self.message)
 
class DealerDoesNotHoldTrumpCard(Exception):
    def __init__(self, cs, msg =""):
        self.card = cs
        self.message = ("Dealer does not hold the trump card \n %s"%(self.card + msg))
        super().__init__(self.message)

class IllegalCardPlayed(Exception):
    def __init__(self, cs, msg =""):
        self.card = cs
        self.message = ("An illegal card was played \n %s"%(self.card + msg))
        super().__init__(self.message)

from sueca_tricks import Trick, parseGameFile, parseTrick
from sueca_cards import Card
#from sueca_cards import Card
class Game:
    def __init__(self, tc):
        self.tc = tc
        self.trick = []
        
    def gameTrump(self):
        return self.tc
    
    def playTrick(self, trick):
        if len(self.trick) == 4:
            raise ValueError("Trick already played. Cannot play another trick.")
        
        if trick.current_player not in [1, 2, 3, 4]:
            raise ValueError("Invalid player number. Valid player numbers are 1, 2, 3, or 4.")
        
        if trick.current_card in self.trick:
            raise CardAlreadyPlayed(trick.current_card)
        
        if self.tc and self.tc.suit != trick.current_card.suit:
            raise DealerDoesNotHoldTrumpCard(self.tc, " - It is not the dealer's turn.")
        
        if not self.trick:
            self.trick.append(trick.current_card)
            return "Trick started. Current player: Player {}".format(trick.current_player)
        
        if trick.current_card.suit != self.trick[0].suit:
            for card in trick.player_cards:
                if card.suit == self.trick[0].suit:
                    raise IllegalCardPlayed(card, " - You should follow the suit.")
        
        self.trick.append(trick.current_card)
        return "Card played by Player {}: {}".format(trick.current_player, trick.current_card)

    def get_current_trick(self):
        return self.trick

    def score(self):
        # Implementation of scoring rules
        score = (0, 0)
        return score
