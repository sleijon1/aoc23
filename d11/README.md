# Insights

Easy day but got caught on a gotcha where I was adding together points between galaxies together with expansion which works for p1 since for each point in between that is also subject to expansion we need to add 1. 

What we want to do with expansion is f.e. node between two g's we want to add exp_level so for total length we want to add nodes_not_in_exp + (exp_level*nodes_in_exp)

So we have to separate out the nodes in exp from all the nodes in the range between two galaxies as to not double count those.

But, in the case of exp_level=1 you can make the mistake of counting
nodes as nodes_in_range + nodes_in_exp = nodes_not_in_exp + nodes_in_exp + nodes_in_exp since this is the same as 
nodes_not_in_exp + (exp_level*nodes_in_exp) for exp_level=2. You'll get the right result but when you try to generalize for exp_level>2 you'll get the wrong result.


## TODO 
make optimizations,
look at other solutions to see if I missed some simplification