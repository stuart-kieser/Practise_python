class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for letter in ransomNote:
            if letter not in magazine:
                return print(False)
            magazine = magazine.replace(letter, "", 1)
        return True


Solution.canConstruct(None, "a", "b")  # false
Solution.canConstruct(None, "aa", "ab")  # false
Solution.canConstruct(None, "aa", "aab")  # true
Solution.canConstruct(None, "baa", "aab")  # true
