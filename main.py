from pyscript import display

A = {'burger', 'fries'}
B = {'burger', 'fries', 'tapsilog', 'siopao'}

# Using Set Operators
display((A <= B), target = "output1") #subset
display((A < B), target = "output1") #proper subset
display((B >= A), target = "output1") #superset
display((B > A), target = "output1") #proper superset

# Using set methods
display(A.issubset(B), target = "output1") #subset
display(A.issuperset(B), target = "output1") #superset