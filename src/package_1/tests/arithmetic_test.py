import unittest

import package_1.arithmetic


class Test(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(package_1.arithmetic.add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
