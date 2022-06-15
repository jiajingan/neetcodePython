#1. Two Sum

def main(nums,target):
    #time T(n), for loop
    #space O(n), hashmap
    dict = {} #value -> index
    for i, n in enumerate(nums):
        diff = target - n
        #find the difference 
        if diff in dict:
            #use diff to find if it's in map 
            #return the previous index and the current index
            return [dict[diff], i]
        #if not add it 
        dict[n] = i
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    nums1 = [3,2,4]
    target1 = 6
    nums2 = [3,3]
    target2 = 6
    print(main(nums,target))
    print(main(nums1,target1))
    print(main(nums2,target2))