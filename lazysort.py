import typing
from random import randint
from heapq import merge
from itertools import chain, tee


def lazysort(l: list) -> typing.Iterator:
    # Stage 1
    stack = []
    current_list = iter(l)
    sentinel = object()
    first = next(current_list, sentinel)
    while first is not sentinel:
        sortedish, surplus = dropsort(chain((first,), current_list))
        stack.append(sortedish)
        current_list = surplus
        first = next(current_list, sentinel)

    # Stage 2
    if len(stack) < 2:  # the case where the list `l` is already sorted
        return iter(l)

    cur = merge(stack.pop(), stack.pop())
    while stack:
        cur = merge(cur, stack.pop())

    return cur


def dropsort(s: typing.Iterable):
    def result_iterator(seq: typing.Iterator):
        last_element = next(seq)
        yield last_element

        while True:
            current_element = next(seq)
            if current_element >= last_element:
                last_element = current_element
                yield last_element

    def surplus_iterator(seq: typing.Iterator):
        last_element = next(seq)

        while True:
            current_element = next(seq)
            if current_element >= last_element:
                last_element = current_element
            else:
                yield current_element

    it1, it2 = tee(s, 2)
    return result_iterator(it1), surplus_iterator(it2)


def main():
    l = [randint(1, 255) for _ in range(100)]
    print("lazysort is working eh?", list(lazysort(l)) == sorted(l))

    for e in lazysort(l):
        print("{:3}".format(e), end=" ")

if __name__ == '__main__':
    main()
