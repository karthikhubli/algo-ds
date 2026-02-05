
"""


5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome( s: str) -> str:
    if len(s) <=1:
        return s
    longest_pal = ''
    size = len(s)
    start = 0
    end = 1
    while start < size-1:
        temp = s[start:end]
        if is_palidrome(temp):
            if len(longest_pal) < len(temp):
                longest_pal = temp
        if end < size:
            end +=1
        else:
            start += 1
            end = start + 1
    return longest_pal

def is_palidrome(s: str) -> bool:
    # print(s)
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end = end-1
    return True




def longestPalindrome_opt( s: str) -> str:
    res = ''
    resLen = 0

    for i in range(len(s)):
        # odd length
        left, right = i, i
        while left >= 0 and right < len(s):
            # print(f"odd {s[left]} -- {s[right]} || odd int {left} -- {right}")
            if s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = s[left:right + 1]
                    print("Updated odd")
            left -= 1
            right += 1

        # even length
        left, right = i, i + 1
        while left >= 0 and right < len(s):
            # print(f"even {s[left]} || {s[right]} || even int {left} -- {right}")
            if s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = s[left:right + 1]
                    print("Updated even")
            left -= 1
            right += 1
    return res

if __name__ == '__main__':
    """
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    """
    strs = ["aacbzxzbbcbcbb"]
    for s in strs:
        print(f"\n\nstring - {s} || palin - {longestPalindrome_opt(s)}")
        print(f"Not optimizzed - {longestPalindrome(s)}")

