#!/usr/bin/env python2
# -*- coding: utf-8 -*-

a_pr=e_pr=o_pr=i_pr=n_pr=r_pr=t_pr=l_pr=s_pr=u_pr = 1
d_pr=g_pr = 2
b_pr=c_pr=m_pr=p_pr = 3
f_pr=h_pr=v_pr=w_pr=y_pr = 4
k_pr = 5
j_pr=x_pr = 8
q_pr=z_pr = 10

def word_volume(word, counter):

    def summator(word):
        if word == "":
            return 0
        else:
            return int(globals()["%s_pr" % word[0]]) + summator(word[1:])

    return [word, summator(word), counter]

n = int(raw_input())
def append(counter):
    if counter == 0:
        return []
    else:
        return [word_volume(raw_input(), counter)] + append(counter-1)

dictionary = append(n)
word7, max_volume, _ = word_volume(raw_input(), 0)

def range_words():
    """sort words' list by the volume"""
    # if word has volume greater than max_volume it means that word
    # has letters not from word7
    return filter(lambda x: x[1] <= max_volume,
                  sorted(dictionary, key = lambda k: k[1], reverse=True))

def dword_in_word7(dict_word):
    """is dictionary word in the 7-letters word"""

    minus_char = lambda char, string: string.replace(char, "", 1)
    temp_word = word7
    for char in dict_word:
        if char not in word7:
            return False
        else:
            temp_word = minus_char(char, temp_word)
    return True

def win_word():
    winner_volume = 0
    winner = None
    for word_type in range_words():
        if dword_in_word7(word_type[0]):
            # we have had no prev. winner
            if winner_volume == 0:
                winner_volume = word_type[1]
                winner = word_type
            # winners' volume finished
            elif winner_volume > word_type[1]:
                return winner[0]
            else:
                # if current word is older than prev. winner
                if word_type[2] > winner[2]:
                    winner = word_type
    return winner[0] if winner is not None else None

print win_word()
