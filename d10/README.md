# Insights

Dont puzzle while tired! :wink: 

Absolutely horrible solution w.r.t readability, clarity, efficiency, data duplication etc etc. I was too tired to refactor and improve as I went which ultimately lead to quite awful code which I will come back and improve a lot when I get the time.

The idea was clear and simple though as far as I can see. Part 1 was simply following the pipes and making sure you get the minimal steps. For part 2 I decided to go the opposite direction of how the question was phrased, namely calculate all the points outside of the loop remove those from the total together with the cycle points:

```python
total - cycle_points - outside | stray_pipes_in_cicle
```

## TODO

Refactor, cleanup, remove data duplication, optimize