import unittest
import os

def analyze_text(filename):
    with open(filename, "rt") as f:
        numLines = len(f.readlines())
        f.seek(0)
        counter = 0
        for line in f.readlines():
            counter+=len(list(line))

        print(numLines, counter)
        return numLines, counter

class TextAnalysisTests(unittest.TestCase):
    """ Tests for '' analyze_text() '' function """

    def setUp(self):
        """Fixture that creates a file for text methods to use."""
        self.filename = "Test_Analysis_test_file.txt"
        with open(self.filename, "wt") as f:
            f.writelines(["Now it's a time of corona virus.\n",
                         "It has created havoc across the globe."])

    def tearDown(self):
        "Fixture that deletes the files used by the test methods"
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 2)


    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 71)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if (__name__ == "__main__"):
    unittest.main()
