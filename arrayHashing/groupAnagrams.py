#49. Group Anagrams

from collections import defaultdict


def main(strs):
    #m is length of the list, n is length of word
    #time T(n*m)
    #space O(26*n) or O(n)
    hashMap = defaultdict(list) #key(pattern) -> list
    for item in strs:
        count = [0] * 26
        #since the list is all lower case, 26 char
        for char in item:
            #use ascii value then change list value to form patterns        
            count[ord(char)-ord('a')] += 1
        #changed tuple so map can take in key, key can not be list
        #if map has this pattern in map, if will append to the list
        hashMap[tuple(count)].append(item)    
    return hashMap.values()



if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]    
    strs1 = ["a"]
    strsList = [strs,strs1,strs2]
    for each in strsList:
        print(main(each))