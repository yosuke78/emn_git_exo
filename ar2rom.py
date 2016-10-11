import unittest

def ar2rom(val):
    return 'i'

class Tests(unittest.TestCase):
    def test_1_to_i(self):
        self.assertEqual(ar2rom(1), 'i')

if __name__ == "__main__":
    unittest.main()
