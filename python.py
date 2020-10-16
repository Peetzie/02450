import numpy as np

### Week 1 ###

# All data setes where loaded correctly. get_values() where changed to to_numpy()


### Week 2 ###

## Assignment 2.1.1 ##
# Yes the desired size requested was made.


## Assignment 2.1.2 ##
# Added changes to the script inside ex2_1_2


## Assignment 2.1.3 ##
# Looking at the graph, the threshold is overwritten within the 90%, therefore it is correct by looking at the data.
# To make 95%  4 or more principal components are needed.


## Assignment 2.1.4 ##
# The data is more spread, making it easier to apply rules for categorizing the data.
# in 2.1.2 the data is more connected, harder to visualize the different elements, however in 2.1.4 the data hs applied more spreading.


### Week 3 ###

## Assignment 3.1.1 ##
# Number of lines: 5
# Number of attributes -> 19 attributes .
# Createing a 2 dim list
l = 5
# Attriibutes 0 indexed
a = 19
words = ['dropped', 'eigenvalue', 'england', 'fifa', 'google', 'internet', 'link', 'matrix', 'model',
         'nonzero', 'p_ij', 'pages', 'problem', 'rank', 'ranking', 'solving', 'top', 'web', 'webpage']
array = (np.zeros((l, a)))
array[0, 4] = 1
array[0, 5] = 1
array[1, 10] = 1
array[1, 18] = 1
array[2, 4] = 1
array[2, 13] = 1
array[3, 14] = 1
array[3, 1] = 1
array[4, 2] = 1
array[4, 3] = 1
print(array)
import toolbo


## Assignment 3.1.2 ##
# The ex3.1.2 script found the following  to be relevant.
# Comparing the two arrays, the one generated is way larger. However some of the words we've listed seems to be corresponding.
# The larger size may be due to filler words included in the list.


# Assignment 3.1.3
# After processing "StopWords", the ammount of words decreased. It shows that the words chosen by the script and myself are correspeondig as the important words.
# The matrix is starting to look-alike.


## Assignment 3.1.4 ##
# Comparison wise theres a small difference, but the structure is pretty much the same though. 


