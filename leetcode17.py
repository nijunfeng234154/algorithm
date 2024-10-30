class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        def dfs(path, index):
            if index == len(digits):
                res.append(path)
                return
            
            ls = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
            for alpha in ls[int(digits[index])]:
                path = path+alpha
                dfs(path, index + 1)
                path = path[:-1]
                

        res = []
        dfs('', 0)
        return res
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.letterCombinations(""), [])

    def test_single_digit(self):
        self.assertEqual(sorted(self.solution.letterCombinations("2")), ["a", "b", "c"])

    def test_two_digits(self):
        self.assertEqual(sorted(self.solution.letterCombinations("23")), sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))

    def test_invalid_digit(self):
        self.assertEqual(self.solution.letterCombinations("1"), [])
        self.assertEqual(self.solution.letterCombinations("0"), [])

    def test_multiple_digits(self):
        self.assertEqual(sorted(self.solution.letterCombinations("234")), sorted([
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]))

if __name__ == '__main__':
    unittest.main()