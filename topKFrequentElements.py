nums = [1,1,1,2,2,3] 
k = 2

def topKFrequentElements(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    for n, c in count.items():
        freq[n].append(c)
    
    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequentElements(nums, k))