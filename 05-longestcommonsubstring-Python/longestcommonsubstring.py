# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"
def longest(s1,s2,l1,l2):
    l = ["ab","AB"]
    
# def longestcommonsubstring(s1, s2):
#     l1 = len(s1)
#     l1 = len(s2)
#     c = ""
#     if l1 < l2:
#         l2,l1 = l1,l2
#         s1,s2 = s2,s1
#     for i in range(l2):
#         d = longest(s1,s2[i:],l1,l2)
#         if 
#     return longest