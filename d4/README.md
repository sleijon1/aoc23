# Insights

I utilized an insight from d3 in using sets and then simple recursion for p2. The memoization isnt needed for p2 since runtime was <2s but why not make it go faster :wink:. Realized recursion wasnt actually needed for p2 either after looking at other solutions.

The reason why recursion isn't really needed for this problem:

Each card will only ever have cards that are further down in the card stack in its total card count. So,

```python
N = [1]*len(matches)
for i, n in enumerate(N):
    for j in range(matches[i+1]):
        N[i + j + 1] += N[i]
```

All we need to do is track the number of copies that exist for a given card. Since if cards above a card we are standing at in the stack have produced copies of a card below then they will have a copy of the current card as well. So we add as many copies that exist of the following card to the following cards count, which is this part: 
```python
N[i + j + 1] += N[i]
```

If we would need to look backwards in the card stack we would have a problem using the basic iterative approach.
