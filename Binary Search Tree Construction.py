
# Iterative approach

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    # INSERTION 
    # Average: O(log(N)) Time | O(1) Space || Worst Case: O(N) Time | O(1) Space
    def insert(self, value):
        currentNode = self # Variable to keep track of where we are
        while True:
            if value < currentNode.value: # Explore left
                if currentNode.left is None: # At end of branch
                    currentNode.left = BST(value) # Add the value there
                    break
                else: 
                    currentNode = currentNode.left
            else: # Explore right
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # SEARCH (contains)
    # Average: O(log(N)) Time | O(1) Space || Worst Case: O(N) Time | O(1) Space
    
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value: # Explore Left
                currentNode = currentNode.left
            elif value > currentNode.value: # Explore Right
                currentNode = currentNode.right
            else:
                return True 
        return False

    # DELETION 
    # Average: O(log(N)) Time | O(1) Space || Worst Case: O(N) Time | O(1) Space
    
    def remove(self, value, parentNode = None):
        currentNode = self 
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # Edge-Case1: Two Children nodes 
                # Looking for the smallest, left-most value of right sub-tree
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    # currentNode.value = smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                # Edge-Case2: root node has no parent node
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                    
                # Edge-Case3: 1 or no child nodes
                elif parentNode.left = currentNode: # Check if left or right child
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right = currentNode: # Check if left or right child
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

def getMinValue(self):
    currentNode = self
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode.value
                




