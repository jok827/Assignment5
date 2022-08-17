# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Defines a few example trees

import treenode as tn
import a5q2 as q2


atree = tn.treenode(2)
a = tn.treenode(7)
b = tn.treenode(5)
atree.left = a
atree.right =  b
c = tn.treenode(11)
d = tn.treenode(6)
a.left = c
a.right = d

# an empty tree with a bad pun: it's empty.  Say mtree out loud.  
mtree = None

# a tree with one node only.  Yes, a bad pun too.
ctree = tn.treenode('si')

# a larger more e-xtree-me tree
xtree = tn.treenode(5,
              tn.treenode(1,None,
                        tn.treenode(4,
                                  tn.treenode(3,tn.treenode(2,None,None),None),
                                  None)),
              tn.treenode(9,tn.treenode(8,tn.treenode(7,tn.treenode(6,None,None),None),None),
                          tn.treenode(1,tn.treenode(3,None,None),tn.treenode(3,None,None))))


# and you thought puns wouldn't get worse...
fibonatree = tn.treenode(5,tn.treenode(2,tn.treenode(1,None,None),
                                     tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None))),
                         tn.treenode(3,tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None)),
                                     tn.treenode(2,tn.treenode(1,None,None),
                                                 tn.treenode(1,tn.treenode(0,None,None),
                                                             tn.treenode(1,None,None)))))


# a tree with some meaning
expr_tree = tn.treenode('*',
                  tn.treenode('+',
                            tn.treenode('+',
                                      tn.treenode(2.0, None, None),
                                      tn.treenode(3.0, None, None)),
                            tn.treenode(3.0, None, None)),
                  tn.treenode('+',
                            tn.treenode(4.0, None, None),
                            tn.treenode('/',
                                      tn.treenode(2.0, None, None),
                                      tn.treenode('+',
                                                tn.treenode(89.0, None, None),
                                                tn.treenode(3.0, None, None)))))


bin_tree = tn.treenode(5,
                       tn.treenode(2,
                                   tn.treenode(1),
                                   tn.treenode(3)),
                       tn.treenode(8,
                                   tn.treenode(7,
                                               tn.treenode(6)),
                                   tn.treenode(9)))


#TESTING FOR SUBST####################################################################

q2.subst(expr_tree,'*','-')
if not expr_tree.data == '-':
    print(f'Error in subst, Expected: - Result: {expr_tree.data}')

if not expr_tree.right.data == '+':
    print(f'Error in subst, Expected: + Result: {expr_tree.right.data}')

if not expr_tree.left.data == '+':
    print(f'Error in subst, Expected: + Result: {expr_tree.left.data}')


q2.subst(mtree,'5','6')
if mtree is not None:
    print(f'Error in subst with empty tree, Expected: None Result: {mtree.data}')

q2.subst(ctree,'si','c')
if not ctree.data == 'c':
    print(f'Error in subst with single node, Expected: c Result: {mtree.data}')

#####################################################################################


#TESTING FOR COPY####################################################################

mtree_copy = q2.copy(mtree)

if not mtree_copy is None:
    print(f'Error in copy with empty tree, Expected: None Result: {mtree_copy}')

ctree_copy = q2.copy(ctree)
if not ctree_copy.data == ctree.data:
    print(f'Error in copy with single node, Expected: {ctree.data} Result: {ctree_copy.data}')

expr_tree_copy = q2.copy(expr_tree)
if expr_tree_copy is expr_tree:
    print('Error in copy, copy did not create a copy but instead referenced the other tree')

if not expr_tree_copy.right == expr_tree.right:
    print(f'Error in copy, Expected: {expr_tree.right} Result: {expr_tree_copy.right}')

#####################################################################################


#TESTING FOR COLLECT_DATA_INORDER#####################################################

mtree_list = q2.collect_data_inorder(mtree)
if not mtree_list == []:
    print(f'Error in copy with empty tree, Expected: None Result: {mtree_list}')


ctree_list = q2.collect_data_inorder(ctree)
if not ctree_list[0] == 'c':
    print(f'Error in copy with empty tree, Expected: c Result: {ctree_list}')



bin_tree_list = q2.collect_data_inorder(bin_tree)
bin_tree_copy_list = q2.collect_data_inorder(q2.copy(bin_tree))
bin_tree_copy_list.sort()
for item in range(len(bin_tree_list)):
    if not bin_tree_list[item] == bin_tree_copy_list[item]:
        print(f'Error in copy, Expected: {bin_tree_list[item]} Result: {bin_tree_copy_list[item]}')
#####################################################################################

#TESTING COUNT_SMALLER###############################################################


def run_test(function_name,expected, actual):
    if expected != actual:
        print(f'Error in {function_name}, Expected: {str(actual)} Result: {str(expected)}')


expected = 3
actual = q2.count_smaller(bin_tree, 5)
run_test("count_small", expected, actual)

expected = 0
actual = q2.count_smaller(mtree, 5)
run_test("count_small", expected, actual)

expected = 1
actual = q2.count_smaller(ctree, "z")
run_test("count_small", expected, actual)

#####################################################################################