#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Rock Paper Scissors that allows 1 person to play against computer, or a second person to also play

TODO: Add player 2
"""


# In[ ]:


import random
import os
from distutils.util import strtobool
from end import end_ as end


p1_wins=0
p2_wins=0
ties=0
class Game:
    def __init__(self,p_2_enabled=False):
        self.p_2_enabled=p_2_enabled
        self.rps_dict={
            1:"rock",
            2:"paper",
            3:"scissors"
        }
        self.plays=0
        while True:
            if self.plays == 0:
                self.grab_user()
            try:
                again_=input("Play again?").lower()
                i=strtobool(again_)
                if i:
                    self.grab_user()
                elif not i:
                    end(5)
                    break
            except ValueError:
                print("Wrong input, please use yes or no")
    def roll(self):
        self.p_2_guess=self.rps_dict[random.randint(1,3)]
    def grab_user(self):
        while True:
            self.p_1_guess=input("Rock, Paper, or Scissors?{p1}".format(p1=" Player One" if self.p_2_enabled==True else "")).lower()
            #self.p_1_guess=self.p_1_guess.lower()
            if self.p_1_guess in self.rps_dict.values():
                break
            else:
                print("Wrong input, please enter Rock, Paper, or Scissors")
                continue
        #print("P1:",self.p_1_guess)
        if not self.p_2_enabled:
            self.roll()
            print("CPU:",self.p_2_guess)
        else:
            #code for player two
            ##ToDo: find way to clear console
            #print("\n"*100)
            os.system('cls')
            while True:
                self.p_2_guess=input("Rock, Paper, or Scissors? Player Two").lower()
                if self.p_2_guess in self.rps_dict.values():
                    break
                else:
                    print("Wrong input, please enter Rock, Paper, or Scissors")
                    continue
        self.logic()
    def logic(self):
        global p1_wins,p2_wins,ties
        p1=self.p_1_guess
        p2=self.p_2_guess
        """
        win 0 = tie
        win 1 = p1 win
        win 2 = p2 win
        """
        if p1 == p2:
            win = 0
            ties +=1
        elif p1 == "rock":
            if p2 == "paper":
                win=2
                p2_wins+=1
            elif p2 == "scissors":
                win=1
                p1_wins+=1
        elif p1 == "paper":
            if p2 == "scissors":
                win=2
                p2_wins+=1
            elif p2 == "rock":
                win=1
                p1_wins+=1
        elif p1 == "paper":
            if p2 == "scissors":
                win=2
                p2_wins+=1
            elif p2 == "rock":
                win=1
                p1_wins+=1
        print("{winner}".format(winner="Tie" if  win == 0 else "Player One Wins!" if win == 1 else "CPU Wins!" if self.p_2_enabled==False else "Player Two Wins!"))
        self.plays+=1
        print("{game} Played: {num} ".format(game="Game" if self.plays < 2 else "Games", num=self.plays))
        print("Score: Player One:{p1}, {p2_}:{p2}, Ties:{tie}".format(p1=p1_wins,p2_="CPU" if self.p_2_enabled == False else "Player Two",p2=p2_wins,tie=ties))
              
while True:
    try:
        start_=input("Would you like to play Rock Paper Scissors?").lower()
        i=strtobool(start_)
        if i:
            while True:
                p2_quest=input("Would you like to play 1 player or 2 player? Input 1 or 2").lower()
                if p2_quest.isdigit():
                    if p2_quest == "1":
                        mem=Game()
                        break
                    elif p2_quest == "2":
                        mem=Game(True)
                        break
                else:
                    continue
            break
        elif not i:
            end(5)
            break
    except ValueError:
        print("Pleasse input yes or no")


# In[ ]:




