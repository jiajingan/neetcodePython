#242. Valid Anagram

import enum
from typing import Counter


def main(s,t):
    #time nlogn, sorted() is timsort
    #space O(1) or O(n)
    return sorted(s) == sorted(t)

def counterWay(s,t):
    #this method counts the repeated letters in s and t then compare
    
    return Counter(s) == Counter(t)

def counterNeetcode(s,t):
    #time T(n)
    #space O(n)
    if(len(s) != len(t)):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
    # print(countS)
    # print(countT)
    return countS == countT

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    a = "rat"
    b = "car"
    # print(main(s,t))
    # print(main(a,b))
    # print(counterWay(s,t))
    # print(counterWay(a,b))
    
    print(counterNeetcode(s,t))