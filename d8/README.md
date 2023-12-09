# Insights

To maximize learning rate I decided to look at reddit thread for solutions to p2. I was already looking at using LCM to find the least amount of steps. Seems like the obvious thing to think about when we need steps to a point to coincide, then a multiple of the amount of the steps to each point has to be in the total steps taken for all points to coincide.

The thing that made this take too long for me was that I didnt investigate the data. I couldnt square a solution in the general case where we can, from a starting point, hit multiple Z's.

But this input data was much simpler:

```python
a_starts = [k for k in nodes if k[-1] == 'A']
print(a_lcm := m.lcm(*map(find_z, a_starts)))

z_starts = [k for k in nodes if k[-1] == 'Z']
print(z_lcm := m.lcm(*map(find_z, z_starts)))

print(a_lcm == z_lcm)

# Output
> 8245452805243
> 8245452805243
> True
```

This wasnt sufficient to immediately use LCM as as a solution however. We needed to ensure that we land on Z from A at the first instruction. Testing this:

```python
print(all([s % len(instr) == 0 for s in map(find_z, a_starts)]))

# Output
> True
```

These two investigations into the data confirms that for this input LCM of all steps it takes for each start A to each end Z will be the solution. Quite tricky that such assumptions were backed into the problem, simplifying it greatly. On the other hand, if you are comfortable with these types of LCM problems you would most likely know what types of simplifications to look for.


Still not sure how to solve the general problem but to solve a similar problem one insight is important:

1. Once we recognize the LCM nature of the problem we can start looking at the data. Start with one node start. How many steps does it take to get to end point Z? Is it a multiple of instruction steps? How many steps til we are back at Z? - Simply answering the first and last question would reveal the allowed assumptions.


## TODO

Need to practice more common multiple/remainder problems to have a better instinct of how to use them and what types of assumptions can simplify problems of this nature.