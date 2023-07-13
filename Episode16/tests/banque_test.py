import unittest

from banque import donne_des_sous


class DonneDesSousShould(unittest.TestCase):

    def test_return_4_when_a_is_1_and_b_is_1(self):
        self.assertEqual(donne_des_sous(1, 1), 4)

    def test_return_20_when_a_is_14_and_b_is_0(self):
        self.assertEqual(donne_des_sous(14, 0), 20)


if __name__ == '__main__':
    unittest.main()
