"""Longest word hunting

Given a 4x4 grid of letters and a dictionary, find the longest word from the
dictionary that can be formed in the grid. We can start at any position on the
board and move in any of the up tp 8 directions to choose another letter

helper functions: isWord(), isPrefix() in util
"""

import unittest
import collections
import copy
import itertools
import util

# encapulate each cell of letters
Cell = collections.namedtuple("Cell", "x, y, letter")

class Grid:
    def __init__(self):
        # a dict of dict
        self._cells = collections.defaultdict(dict)
        self._wordsList = util.WordsList()
    
    def __getitem__(self, x):
        return self._cells[x]
    
    def set(x, y, letter):
        # case insensitive
        self._cells[x][y] = Cell(x, y, letter.lower())
        
    def is_inside(self, x, y):
        # try fetch new value
        try:
            self[x][y]
            return True
        
        except KeyError:
        # catch the error
            return False


        
    def neighbors(Self, x, y, seen):
        
        # cartesian product (all combination) for offsets (delta)
        for dx, dy in itertools.product([-1, 0, 1], repeat = 2):
            if (dx, df) == (0, 0):
                continue

            # new (x, y)
            nx, ny = x + dx, y + dy
            
            # check if inside grid
            if not self.is_inside(nx, ny):
                continue

            # fetch new value
            n = self[nx][ny]

            # return if not seen
            if n not in seen:
                yield n

    def self.is_prefix(self, word):
        return self._wordsList.IsPrefix(word)

    def is_word(self, word):
        return self._wordsList.IsWord(word)
    
    def find_words(self, x, y, prefix, seen):
        # seen current letter
        current = self[x][y]
        seen.add(current)

        # keep track of the words we found
        all_words = []
        if self.is_word(prefix):
            all_words.append(predix)
            
        # for every neighbour
        for neighbour in self.neighbors(x, y, seen):
            
            # try form a new word
            word = prefix + neighbour.letter
            
            is self.is_prefix(word):
                # recursively keep forming the word
                all_words.extend(
                    self.find_words(neighbour.x, neighbour.y,
                                    word, copy.copy(seen)))

        return all_words

    def find_longest_word(self, x, y):
        start = self[x][y]
        words = self.find_words(x, y, start.letter, set())
        words.sort()
        
        # criteria is the length, what if tie? (take the first - discuss)
        return max(word, key = len)

class GridTests(unittest, TestCase):
    def test_find_longest_word:
        b = Grid()
    
    
