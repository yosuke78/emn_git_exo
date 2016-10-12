import unittest

conversion_map = (
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1))


def ar2rom(val):
    res = ''
    for rom, ar in conversion_map:
        while val >= ar:
            res += rom
            val -= ar
    return res


class Tests(unittest.TestCase):
    def test_1_to_i(self):
        self.assertEqual(ar2rom(1), 'I')

    def test_2_to_ii(self):
        self.assertEqual(ar2rom(2), 'II')

    def test_3_to_iii(self):
        self.assertEqual(ar2rom(3), 'III')

    def test_4_to_iv(self):
        self.assertEqual(ar2rom(4), 'IV')

    def test_5_to_v(self):
        self.assertEqual(ar2rom(5), 'V')

    def test_9_to_ix(self):
        self.assertEqual(ar2rom(9), 'IX')

    def test_10_to_x(self):
        self.assertEqual(ar2rom(10), 'X')

    def test_20_to_xx(self):
        self.assertEqual(ar2rom(20), 'XX')

    def test_21_to_xxi(self):
        self.assertEqual(ar2rom(21), 'XXI')

if __name__ == "__main__":
    unittest.main()
