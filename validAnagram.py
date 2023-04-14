s = 'car'
t = 'rat'

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    sDict = {}
    tDict = {}
    for i in range(len(s)):
        if s[i] in sDict:
            sDict[s[i]] += 1
        else:
            sDict[s[i]] = 1
    for i in range(len(t)):
        if t[i] in tDict:
            tDict[t[i]] += 1
        else:
            tDict[t[i]] = 1

    for k in sDict:
        if sDict[k] != tDict.get(k,0):
            return False
    return True

print(isAnagram(s, t))