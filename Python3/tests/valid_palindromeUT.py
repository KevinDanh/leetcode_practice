import unittest
from solutions.valid_palindrome import Solution1

# Unit tests included in the same file
class TestSolution1(unittest.TestCase):
    def testIsPalindrome(self):
        self.assertEqual(Solution1.isPalindrome(self, "race a car"), False)
        self.assertEqual(Solution1.isPalindrome(self, "A man, a plan, a canal: Panama"), True)
        self.assertEqual(Solution1.isPalindrome(self, " "), True)

if __name__ == "__main__":
    unittest.main()
