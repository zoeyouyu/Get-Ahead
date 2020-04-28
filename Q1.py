
class FlattenedIterator:
  
  """Iterator that iterates in an interleaved fashion."""
  
  def __init__(self, data):
    self.data = data
    self.current = 0 # current iterator
    self.index = 0
    self.maxcycle = max(len(it) for it in data)
    self.cycle = 0
    
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.current < len(self.data):
        it = self.data[self.current]
        self.current += 1
        if self.index < len(it):
          return it[self.index]
        else:
          return next(self)

    else:
        self.current = 0
        self.cycle += 1
        self.index += 1
        
        if self.cycle >= self.maxcycle:
            raise StopIteration
            
        return next(self)
    
Iterators = [[1, 2, 3], [4, 5], [6, 7, 8]]
    
FlattenedIt = FlattenedIterator(Iterators)
result = list(FlattenedIt)

