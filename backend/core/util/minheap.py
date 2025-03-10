# 用于实现排行的最小堆
from heapq import heapify, heappush, heappushpop


class MinHeap:
    def __init__(self, top_n, h=[]):
        self.h = h[:]
        self.length = top_n
        heapify(self.h)

    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)

    def getTop(self):
        return sorted(self.h, reverse=True)

    def merge(self, other):
        """
        合并另一个堆
        @type other MinHeap
        """
        for elem in other.h:
            self.add(elem)

    def reset(self):
        self.h = []
        heapify(self.h)
