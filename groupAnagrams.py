from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]

#medium

# Solution 1 : O(m.n logn) where m is items in list and n is length of each item
# def groupAnagrams(strs):
#     lookup = defaultdict(list)

#     for s in strs:
#         key = ''.join(sorted(list(s)))
#         lookup[key].append(s)
#         print(lookup)
    
#     output = []
#     for l in lookup.values():
#         output.append(l)
#     return output


# Solution 2 : O(m.n * 26) == O(m.n), better time complexity
def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
            print(tuple(count))
        res[tuple(count)].append(s)
    return res.values()

print(groupAnagrams(strs))

