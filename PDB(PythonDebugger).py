import pdb
import unittest

"""
console:
python3 -m pdb "PDB(PythonDebugger.py"

PDB> next #move to next line
PDB>where #see call stack
PDB>list # show the code
PDB>quit #exit PDB
"""

#pdb.set_trace()


def is_palindrome(input):
    l1 = list(str(input))
    l2 = list(reversed(list(str(input))))
    print(l1, l2)
    if l1==l2:
        return True
    else:
        return False


class is_palindrome_tests(unittest.TestCase):

    def setUp(self):
        #self._input = "02022020" - True
        #self._input = 12321 - True
        self._input = 123 # False
        is_palindrome(self._input)

    def test_function_runs(self):
        is_palindrome(self._input)

    def test_correct_palindrome(self):
        self.assertFalse(is_palindrome(self._input))


if __name__ == "__main__":
    unittest.main()
    #print(is_palindrome(12321))
    #print(is_palindrome("02022020"))