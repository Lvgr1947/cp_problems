# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"
def longestcommonsubstring(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    c1 = 0
    d = ""
    f= []
    if l1 > l2:
        l2,l1 = l1,l2
        s1,s2 = s2,s1
    for i in range(l1):
        if s1[i] in s2:
            c2 = 1
            j = s2.index(s2[i])
            e = s2[i]
            for k in range(j+1,l2):
                if s1[k] == s2[i+k-j]:
                    c2 += 1
                    e += s1[k]
                else:
                    break
            print(c,"c")
            if c1 == c2:
                f.append(d)
            elif c1 < c2:
                f = [e]
                c1 = c2
    f = sorted(f)
    return f[0]
print(longestcommonsubstring("abcdef", "abqrcdest"))