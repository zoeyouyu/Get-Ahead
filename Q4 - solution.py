# Histograms and Areas
import math
import unittest

def find_minimum(values, start, end):
  
  index = None
  minimum = math.inf
  for i in range(start, end + 1):
    if values[i] < minimum:
      index = i
      minimum = values[i]
  return index

def maximum_rectangle(histogram, start = None, end = None):
  
  if start is None:
    start = 0

  if end is None:
    end = len(histogram) - 1
    
  # base case (height = area)
  if start == end:
    return start, end, histogram[start]

  # invalid case
  if start > end:
    return start, end, -math.inf

  # find the lowest bar
  index = find_minimum(histogram, start, end)
  # If use the lowest bar
  a = histogram[index] * (end - start + 1)

  # store in a dict
  areas = dict()
  areas[a] = (start, end) # area a is given by this (start, end)

  # recursive case to its(min_bar) left
  i, j, a = maximum_rectangle(histogram, start = start, end = index - 1)
  areas[a] = (i, j)

  # recursive case to its(min_bar) RIGHT
  i, j, a = maximum_rectangle(histogram, start = index + 1, end = end)
  areas[a] = (i, j)
  
  maximum = max(areas)
  return areas[maximum] + (maximum,) # return (i, j, max_area)


# Testing
class HistogramTests(unittest.TestCase):

  def test_maximum_rectangle(self):
    self.assertEqual(maximum_rectangle([6, 2, 5, 4, 5, 1, 6]), (2, 4, 12))
    self.assertEqual(maximum_rectangle([2, 4, 2, 1]), (0, 2, 6))
    self.assertEqual(maximum_rectangle([2, 4, 2, 1, 10, 6, 10]), (4, 6, 18))
    self.assertEqual(maximum_rectangle([5, 3, 4, 1, 2, 3]), (0, 2, 9))


if __name__ == "__main__":
  print(maximum_rectangle([6, 2, 5, 4, 5, 1, 6]))
