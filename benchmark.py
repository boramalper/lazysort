from timeit import Timer

import matplotlib.pyplot as plt


def main():
    std_setup = '''
from random import randint, seed

seed()
l = [randint(0, 255) for _ in range({})]
    '''

    lazy_setup = '''
from random import randint, seed
from lazysort import lazysort

seed()
l = [randint(0, 255) for _ in range({})]
    '''

    std_results = []
    lazy_results = []
    for power in range(1, 11):
        std_results.append(min(Timer('sorted(l)', setup=std_setup.format(2 ** power)).repeat(3, 1000)))
        lazy_results.append(min(Timer('list(lazysort(l))', setup=lazy_setup.format(2 ** power)).repeat(3, 1000)))

    plt.xlabel("Number of Integers")
    plt.ylabel("Total Number of Seconds Spent (1,000 times)")
    plt.axis([0, 2 ** 10, 0, max(lazy_results + [max(std_results)])])
    plt.plot([2 ** p for p in range(1, 11)], std_results, "r--", label="Timsort")
    plt.plot([2 ** p for p in range(1, 11)], lazy_results, "b--", label="lazysort")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    main()
