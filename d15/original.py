import collections as c
from dataclasses import dataclass
def hash(string):
    current = 0
    for char in string:
        current = (current + ord(char))*17 % 256
    return current

print(sum(map(hash, open('d15/input.txt').read().split(','))))

@dataclass
class Node:
    _previous = None
    _next = None
    foc: int = None
    label: str = None

    def __eq__(self, __value: object) -> bool:
        return self.label == __value.label

boxes = c.defaultdict(dict)

d = open('d15/input.txt').read().split(',')
for val in d:
    splitter = '-' if '-' in val else '='
    if splitter == '-':
        label = val[:-1]
    else:
        label, foc = val.split(splitter)
        node = Node(foc=int(foc), label=label)
    box_nr = hash(label)
    #print(label, foc, splitter)
    #print(boxes)
    if label in boxes[box_nr]:
        next_node = boxes[box_nr][label]._next
        previous_node = boxes[box_nr][label]._previous
        if splitter == '=':
            # this is screwed
            # next_node needs to point to
            # new node with prev
            # previous_node need to point to
            # node with next
            node._next = next_node
            node._previous = previous_node
            boxes[box_nr][label] = node
            try:
                next_node._next._previous = node
                previous_node._next = node
            except AttributeError:
                boxes[box_nr]['last'] = node
                # solo node was there
                pass
        else:
            try:
                previous_node._next = next_node
            except AttributeError:
                # single element
                pass
            remove_node = boxes[box_nr][label]
            del boxes[box_nr][label]
            if remove_node == boxes[box_nr]['last']:
                if next_node:
                    boxes[box_nr]['last'] = next_node
                else:
                    del boxes[box_nr]
    elif splitter != '-' and node:
        try:
            node._next = boxes[box_nr]['last']
            boxes[box_nr]['last']._previous = node
            boxes[box_nr]['last'] = node
            boxes[box_nr][label] = node
        except KeyError:
            boxes[box_nr]['last'] = node
            boxes[box_nr][label] = node

print(boxes)
sum = 0
for i in boxes.keys():
    print('i', i)
    j = 0
    partial = 0
    try:
        _node = boxes[i]['last']
        while _node:
            print(_node._next)
            partial += (i+1)*(len(boxes[i]) - 1 - j)*_node.foc
            _node = _node._next
            j += 1
        print('partial', partial)
        sum += partial
    except KeyError:
        pass

print(sum)