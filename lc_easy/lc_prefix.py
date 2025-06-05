'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
        ret = ""
        if(len(strs) < 2):
            return strs[0]
        arr_len = len(strs)
        ptr = 0
        while True:
            for i in range(1,arr_len):
                if(ptr < min(len(strs[i]), len(strs[0]))):
                    temp = strs[0][ptr]
                    if(len(strs[i]) > ptr and temp == strs[i][ptr]):
                        continue
                    else:
                        return ret
                else:
                    return ret
            ret = ret + strs[i][ptr]
            ptr+=1
        return ret

def lcp_best(strs: List[str]):
    if strs == None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]







if __name__ == '__main__':
    # print(longestCommonPrefix(["flower","flow","flight"]))
    print('--------')
    print(lcp_best(["a","b","c"]))