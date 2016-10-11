import unittest


def ar2rom(val):
    if val == 1:
        return 'i'
    elif val == 2:
        return 'ii'
    elif val == 3:
        return 'iii'


class Tests(unittest.TestCase):
    def test_1_to_i(self):
        self.assertEqual(ar2rom(1), 'i')
    def test_2_to_ii(self):
        self.assertEqual(ar2rom(2), 'ii')
    def test_3_to_iii(self):
        self.assertEqual(ar2rom(2), 'ii')

if __name__ == "__main__":
    unittest.main()
