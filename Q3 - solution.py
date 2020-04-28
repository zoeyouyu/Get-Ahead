# Longest path in the Tree
class Tree:
  def __init__(self, value, *children):
    self.value = value
    self.children = children


# We walk the tree by iterating throught it,
# yielding the length of the path ending at each node we encounter,
# then take the max of that.

def longest_path(tree):

  def rec(current, parent_value = 0, parent_path_length = 0):

    # Length of the longest chain this node is part of.
    current_path_length = (parent_path_length + 1
                           if current.value == parent_value + 1 else 1)

    # Emit the length of this node.
    yield current_path_length

    # Recurse into the children
    for child in current.children:
      # For each of the descendant nodes, emit their lengths as well
      for value in rec(child, current.value, current_path_length):
        yield value

  # Take the overall maximum length.
  return max(rec(tree))


# Tests

if __name__ == "__main__":
  assert longest_path(Tree(1)) == 1

  assert longest_path(
    Tree(1,
      Tree(2,
        Tree(4)),
      Tree(3))
    ) == 2

  assert longest_path(
    Tree(5,
      Tree(6),
      Tree(7,
        Tree(8,
          Tree(9,
            Tree(15),
            Tree(10))),
        Tree(12)))
      ) == 4
