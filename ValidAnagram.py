class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = " ".join(sorted(s))
        t = " ".join(sorted(t))
        return s == t

#Better Time Complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        for ch in set(s):
            if s.count(ch)!=t.count(ch):
                return False
        return True