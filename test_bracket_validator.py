import unittest
from bracket_validator import bracket_validator

class TestBracketValidator(unittest.TestCase):
    def test_valid_basic(self):
        self.assertTrue(bracket_validator("()"))
        self.assertTrue(bracket_validator("[]"))
        self.assertTrue(bracket_validator("{}"))

    def test_valid_nested(self):
        self.assertTrue(bracket_validator("([])"))
        self.assertTrue(bracket_validator("{[()]}"))
        
    def test_valid_with_other_chars(self):
        self.assertTrue(bracket_validator("a(b[c]{d})e"))
        
    def test_invalid_unclosed(self):
        self.assertFalse(bracket_validator("(()"))
        self.assertFalse(bracket_validator("{[("))

    def test_invalid_mismatched_pair(self):
        self.assertFalse(bracket_validator("([)]"))
        self.assertFalse(bracket_validator("(}"))

    def test_empty_string(self):
        self.assertTrue(bracket_validator(""))

    def test_only_non_brackets(self):
        self.assertTrue(bracket_validator("abc 123 def"))

if __name__ == '__main__':
    unittest.main()
