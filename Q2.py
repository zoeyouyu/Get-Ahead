class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]
  
  def isempty(self):
    return self.items == []

  def size(self):
    return len(self.items)
  
def findsize(string):
  """A function that finds the size of the longest,
contiguous subtring of balanced parentheses."""
  s = Stack()
  
  index = 0
  bal_length = [0]
  length = 0
  
  while index < len(string):
    par = string[index]
    
    if par == "(":
      s.push(par)
      length += 1
      
    else:
      if not s.isempty():
        top = s.pop()
        if top == "(":
          length += 1
          
    if s.isempty():
        bal_length.append(length)
        length = 0
    
    index += 1
  return max(bal_length)

print(findsize("())(())"))
print(findsize(")(()))))((((()"))
print(findsize(""))
print(findsize(")))())"))
