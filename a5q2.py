from treenode import  treenode

def is_leaf(tnode):
    """
    Purpose:
        Determine if tnode is a leaf.
    Pre-conditions:
        :param tnode: a treenode
    Return:
        True if the tnode has zero children
    """
    return tnode.left is None and tnode.right is None


def to_string(tnode, level=0):
    """
    Produce a formatted string to represent the hierarchy of
    a tree.  Tree diagrams usually have the root at the top.
    Here the root is at the top left.
    - every data value appears on its own line
    - the levels of a tree are columns from left to right
    - nodes at the same level start in the same column
    - very long data values might cause the presentation to get messy
    - subtrees appear below a parent
      - left subtree immediately
      - right subtree after the entire left subtree
    Pre-conditions:
        :param tnode: a Binary tree (treenode or None)
        :param level: the level of the tnode (default value 0)
    Return:
        A string with the hierarchy of the tree.
    """
    if tnode is None:
        return 'EMPTY'
    else:
        result = '\t'*level
        result += str(tnode.data)
        if tnode.left is not None:
            result += '\n'+to_string(tnode.left, level+1)
        else:
            result += '\n'
        if tnode.right is not None:
            result += '\n'+to_string(tnode.right, level+1)
        return result


def subst(tnode, t, r):

    '''Purpose: To substitute a target value t with a replacement value r wherever it
     appears in the given tree

     Pre-conditions: A target data value, a replacement value, a treenode

     Post-conditions: Modifies tree node

     Returns: None'''

    if tnode is None:
        return

    else:

        subst(tnode.left,t,r)

        if tnode.data == t:

            tnode.data = r

        subst(tnode.right,t,r)

def copy(tnode):

    '''Purpose: To create an exact copy of the given tree, with completely new treenodes, but
    exactly the same data values, in exactly the same place

         Pre-conditions: A non-empty treenode

         Post-conditions: None

         Returns: A copy of a treennode'''

    if tnode is None:
        return None

    else:

        copyTree = treenode(tnode.data,tnode.left,tnode.right)
        copy(tnode.left)
        copy(tnode.right)

        return copyTree


def collect_data_inorder(tnode):

    '''Purpose: To collect all the data values in the given tre

         Pre-conditions: A non-empty treenode

         Post-conditions: None

         Returns: A list of treenode data in order'''

    if tnode is None:
        return None

    else:

        treeList = [collect_data_inorder(tnode.left),tnode.data,collect_data_inorder(tnode.right)]

        return treeList