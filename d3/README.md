# Insights

Once again I found hb4q's solution to d3 interesting. The assumptions made in that solution were quite bold but that actually lead me to an important insight for fast solution exploration:

1. Restrict solution space by making assumptions. Look for contradictions to those assumptions, if none can be found its a good place to start. Essentially - start with a simpler problem but try to rule out that it is not a different problem altogether.

Continuing,

2. Sets are useful for finding intersections with less code

3. Its typically helpful to define the infinite sets inversely

In this problem the number of different types of _symbols_ is infinitely large afawk. But any number will be in _{0, 9}_, adding _'.'_ to that set and we can describe all _symbols_ as _not_ that set. Using this we can parse all the information we need about the symbols succintly:

```python
chars = {(r, c) for r in range(len(board)) for c in range(len(board))
                if board[r][c] not in '01234566789.'}
```

Then, using _regex_ we can parse the digits easily. This is a more functional approach which contrasts the iterative approach of parsing char by char and buffering information.

Concluding, the succinct solution with bold assumptions is clean and very readable and I learned some things from reading it. But I do prefer a more general solution which is why I made my adjustments, there is still that one assumption in there that I would prefer to rule out. So I still prefer my original solution if I cleaned it up, but the optimal would be to rule out the assumption in the more succinct solution.

Anyhow, thats enough for today. At it again tmrw!