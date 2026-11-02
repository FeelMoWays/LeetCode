class Solution:
    def isPalindrome(self, s: str) -> bool:
        split_string = "".join([char.lower() for char in s if char.isalnum()])
        return split_string == split_string[::-1]