```bash
>>>  test = {1: [[(5, 10), (16, 21)]]}
>>> for r1, r2 in test[1][::-1]:
...     print(r1, r2)
...
16 21
5 10
>>> for k in test[1]:
...     r1, r2 = k[::-1]
...     print(r1, r2)
...
10 5
21 16
```