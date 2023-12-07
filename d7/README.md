# Insights

The first important thing to think about for today was simply mapping over the input to an order that sorted will work with inherently. Then p2 was simply mapping J to 0 or 1 for the same reason. 

Another important insight I didnt utilize in my original solution which I found inspiration in from other solutions was utilizing the sort on multiple levels:

1. 
```python
def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

max(type(h.replace('1', c)) for c in h)
```
the reason this is clever is that this seemlessly deals with cases such
as AABB2 with almost as little code as `max(set(hand))`. That latter
doesnt cover AABB2 since AABB2 needs to be ranked above AABC2. The naive approach after realizing this is to then to identify the types by iteration which is what I did in my original solution.

2. 
```python
cards = [hand_with_joker, hand_without, bid]
sorted(cards), 
```
this sorting takes care of the "gotcha" of p2, namely that AJJJJ is a perfect ranking in the hand types but most likely quite low in the ranking within the hand type. Since sorted will sort on the first element and then the second we will get the ranking we need without having to separate the groups for separate ranking, and then appending. So this will deal with cases such as CJJJJ vs CCJJJ where they would draw in the `t(0)`-comparison but CCJJJ will rank over CJJJJ in the `t(1)`-comparison.

## Key abstraction

We can essentially think of each card as an object encompassed by 3 pieces of data: hand w jokers, hand w/o jokers, bid

Bid doesnt affect algorithm apart from sum step so can be ignored.

Since we want to sort the data we simply sort on the different data points of the object in prefered order, which was hwj->hwoj in this case. 

## Generalization

Whenever we can generalize the problem by adding data which is the case of both the 1st and 2nd case we can sometimes get much simpler code then doing the iteration. Seeing the generalization before iterating through the problem is the tricky part however, which I for one believe means you've seen reasonably similar problem before. Practice makes perfect.