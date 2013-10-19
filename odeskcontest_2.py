#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def parse_square(raw):
    if raw in ["S", "R", "E"]:
        return raw
    else:
        return int(raw)

def append(counter):
    if counter == 0:
        return []
    else:
        return [parse_square(raw_input())] + append(counter-1)

# game_area = append(int(raw_input()))
game_area = ['S', 1, 'R', 4, 3, 4, 3, -5, 2, -4, 'E']
class Node(object):

    def __init__(self, id, parents_list):
        self.count = 1
        self.winner_way = False
        self.childrens_list = []
        self.id = id
        self.parents_list = parents_list

    def next_square(self, steps):
        if (self.id+steps)>=0 and (len(game_area) - (self.id+steps))>=0:
            # Если я ещё не возвращался на этой ветке в эту клетку,
            # то вернём номер следующего шага
            if (self.id+steps) in self.parents_list:
                return []
            else:
                return Node(self.id+steps, self.parents_list+[self.id])
        else:
            return []

    def get_steps(self):
        step_rule = game_area[self.id]
        if step_rule == "R":
            return xrange(1, 7)
        elif step_rule == "E":
            return []
        else:
            return [step_rule,]

    def __str__(self):
        return "%s %s %s" % (self.id, game_area[self.id], self.winner_way)

    def __repr__(self):
        return self.__str__()

    def get_childrens(self):
        if self.childrens_list == []:
            for step in self.get_steps():
                ns = self.next_square(step)
                if ns == []:
                    to_append = []
                elif game_area[ns.id] == "E":
                    to_append = ["E"]
                    self.winner_way = True
                    self.count += 1
                else:
                    self.winner_way, count, to_append = ns.get_childrens()
                    if self.winner_way:
                        self.count += count
                self.childrens_list.append([ns] + to_append)
        return self.winner_way, self.count, self.childrens_list


first_steps = []
for step in xrange(1, 7):
    node = Node(step, [0,])
    way = node.get_childrens()
    if way[0] == True:
        first_steps.append(node)

if first_steps == []:
    print("impossible")
else:
    print(min([x.count for x in first_steps]))
