class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(list(filter(lambda a: a.isalnum(), s))).lower()
        print(word)
        print(word[::-1])
        return word == word[::-1]