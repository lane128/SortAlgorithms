#!/usr/bin/env python
#-*-coding:utf-8-*-
US=[4,1,5,3,6,9,2,8]

def heap_sort(lst):
    for start in range((len(lst)-2)/2,-1,-1):
        sift_down(lst,start,len(lst)-1)
    print lst
    for end in range(len(lst)-1,0,-1):
        lst[0],lst[end] = lst[end],lst[0]
        sift_down(lst,0,end-1)
    print lst
 
def sift_down(lst,start,end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:break
        if child+1 <= end and lst[child] < lst[child+1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root],lst[child] = lst[child],lst[root]
            root = child
        else:
            break
 
if __name__ == "__main__":
    heap_sort(US)
