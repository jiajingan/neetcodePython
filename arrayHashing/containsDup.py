#217. Contains Duplicate

def main(nums):
    #slow, only 5% faster maybe because the len and set operations?
    #time T(1)
    #space O(1)
    return len(set(nums)) < len(nums)

def faster(nums):
    #49% faster
    #time T(n)
    #space O(1)
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    nums1 = [1,2,3,4]
    nums2 = [1,1,1,3,3,4,3,2,4,2]
    numsList = [nums,nums1,nums2]
    for item in numsList:
        print(faster(item))