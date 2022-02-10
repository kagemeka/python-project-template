import importlib.metadata
import pprint
import unittest

import pytest


@pytest.mark.skip(reason="run manually after `pip install .`")
class Test(unittest.TestCase):
    def test(self) -> None:

        entry_points = importlib.metadata.entry_points()

        for entry_point in entry_points["console_scripts"]:
            print(entry_point.name)

        for entry_point in entry_points["pseudo_package.plugin"]:
            print(entry_point.name)
            plugin = entry_point.load()
            plugin()

        pprint.pprint(entry_points)


if __name__ == "__main__":
    unittest.main()
