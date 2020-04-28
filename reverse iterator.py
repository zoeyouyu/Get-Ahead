##class Reverse:
##
##  def __init__(self, data):
##    self.data = data
##    self.index = len(data)
##
##  def __iter__(self):
##    return self
##
##  def __next__(self):
##    if self.index == 0:
##      raise StopIteration
##    
##    self.index -= 1
##    return self.data[self.index]

# Generator function
##def Reverse(data):
##  for index in range(len(data)-1, -1, -1):
##    yield data[index]

# Generator expression
##def Main():
##  rev = Reverse('Drapsicle')
##  for char in rev:
##    print(char)
##  data = "Drapsicle"
##  print(list(data[i] for i in range(len(data)-1, -1, -1)))
##


# When python runs a file, it creates several special variables,
# __name__ is one of them.
# If it is being directly, it names it as __main__.
# If it is being imported, the __name__ variable becomes the 'filename'.

# Check if this file is being directly run by python,
# or being imported.
# Make sure these code only run when its directly run, not when imported.
##if __name__ == '__main__':
##  Main()


import random

class RandomIter:

    """ This Iterator picks random items in the
    container and goes until it randomly hits the end."""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index = random.randint(0, len(self.data))
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

def main():
    rnd = RandomIter('Drapsicle')
    for char in rnd:
        print(char)

if __name__ == '__main__':
  main()


